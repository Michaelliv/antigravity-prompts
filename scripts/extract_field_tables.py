#!/usr/bin/env python3
"""
Walk Go reflect 'name' tables in the language-server binary to recover
ordered field-name + tag tuples for every struct that has a
`jsonschema_description:` somewhere in its tags.

Encoding (Go runtime reflect/type.go: `name` object):

    [flag-byte] [name-len-varint] [name bytes] [tag-len-varint] [tag bytes]

Flag byte bits:
  bit 0 (0x01) = name is exported
  bit 1 (0x02) = followed by tag
  bit 2 (0x04) = name is embedded

In this binary, in-struct field names use 0x03 (exported+tag) almost
exclusively. The varints are short (single byte) for our cases.

Adjacent struct fields are packed back-to-back with no separator other
than the next field's flag byte.

We also try to associate each recovered struct with the closest
preceding `CortexStep<Name>` token from a `StepExtractor[*…CortexStep…]`
or `BrowserAction[*…CortexStep…]` neighborhood symbol.
"""
from __future__ import annotations
import re
import json
from pathlib import Path
from collections import defaultdict

BIN = Path('/Applications/Antigravity.app/Contents/Resources/app/extensions/antigravity/bin/language_server_macos_arm')
OUT_DIR = Path('/Users/michael/projects/antigravity-prompts/tool_shapes/recovered_field_tables')

NAME_CHARS = set(b'_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
TAG_PRINTABLE = set(range(32, 127)) | {0x09}  # tab too


def read_varint(buf: bytes, i: int) -> tuple[int, int]:
    """Decode unsigned varint, return (value, bytes_consumed)."""
    v = 0; shift = 0; n = 0
    while i + n < len(buf):
        b = buf[i + n]; n += 1
        v |= (b & 0x7F) << shift
        if not (b & 0x80):
            return v, n
        shift += 7
        if shift > 28:
            break
    return -1, n


def try_parse_field(data: bytes, off: int) -> tuple[dict, int] | None:
    """Try to parse one Go reflect-name encoded field starting at `off`.

    Returns (parsed, length_in_bytes) or None.
    """
    if off >= len(data):
        return None
    flag = data[off]
    # Accept exported (1), exported+tag (3), exported+embedded (5),
    # exported+tag+embedded (7). Reject everything else.
    if flag not in (1, 3, 5, 7):
        return None
    has_tag = bool(flag & 0x02)

    nlen, n_n = read_varint(data, off + 1)
    if nlen <= 0 or nlen > 96:
        return None
    name_start = off + 1 + n_n
    if name_start + nlen > len(data):
        return None
    name = data[name_start:name_start + nlen]
    # Names: ASCII identifier characters (allow `.` for some embedded cases)
    if not all(b in NAME_CHARS or b == 0x2E for b in name):
        return None

    cur = name_start + nlen
    tag = b''
    if has_tag:
        tlen, n_t = read_varint(data, cur)
        if tlen <= 0 or tlen > 4096:
            return None
        tag_start = cur + n_t
        if tag_start + tlen > len(data):
            return None
        tag = data[tag_start:tag_start + tlen]
        # tags must be entirely printable
        if not all(b in TAG_PRINTABLE for b in tag):
            return None
        cur = tag_start + tlen

    return ({
        'flag': flag,
        'name': name.decode('ascii'),
        'tag': tag.decode('ascii') if tag else '',
    }, cur - off)


def parse_decoded_tag(tag: str) -> dict[str, str]:
    """Parse a Go struct tag into its key:value pairs."""
    out: dict[str, str] = {}
    i = 0
    while i < len(tag):
        while i < len(tag) and tag[i] in ' \t':
            i += 1
        m = re.match(r'([A-Za-z_]\w*):"', tag[i:])
        if not m:
            break
        key = m.group(1)
        i += m.end()
        v: list[str] = []
        while i < len(tag):
            c = tag[i]
            if c == '\\' and i + 1 < len(tag):
                v.append(tag[i + 1]); i += 2
            elif c == '"':
                i += 1; break
            else:
                v.append(c); i += 1
        out[key] = ''.join(v)
    return out


def is_jsonschema_field(tag: str) -> bool:
    """True if this field's tag belongs to a jsonschema/tool-arg struct.

    These tags use `jsonschema:`, `jsonschema_description:`,
    `jsonschema_required:`, or plain `json:`. They never have `protobuf:`
    (those are proto-generated types in adjacent rodata).

    Empty tags are EXCLUDED here — in this binary, untagged rname records
    are usually Go runtime type-name strings (`*foo.Bar[...]`) packed in the
    same rodata, not real struct fields.
    """
    if not tag:
        return False
    if 'protobuf:' in tag:
        return False
    if 'jsonschema' in tag or tag.startswith('json:') or ' json:' in tag:
        return True
    return False


def walk_struct(data: bytes, anchor_off: int) -> tuple[list[dict], int, int]:
    """Walk forward and backward from anchor_off (= a field's flag byte)
    parsing successive field records of the SAME struct. We stop on any
    parse that crosses into protobuf-tag territory (different parent type).
    Returns (fields, lo, hi).
    """
    fields: list[dict] = []
    cur = anchor_off
    while True:
        r = try_parse_field(data, cur)
        if r is None:
            break
        f, n = r
        if not is_jsonschema_field(f['tag']):
            break
        f['offset'] = cur
        fields.append(f)
        cur += n
    fwd_end = cur

    prepend: list[dict] = []
    earliest = anchor_off
    LIMIT = max(0, anchor_off - 4096)
    while True:
        found = None
        for cand in range(earliest - 1, LIMIT - 1, -1):
            r = try_parse_field(data, cand)
            if r is None:
                continue
            f, n = r
            if cand + n == earliest and is_jsonschema_field(f['tag']):
                f['offset'] = cand
                found = f
                earliest = cand
                break
        if found is None:
            break
        prepend.append(found)
    prepend.reverse()
    return prepend + fields, earliest, fwd_end


def find_cortex_step_near(data: bytes, lo: int, hi: int, win: int = 2048) -> str | None:
    """Search for a CortexStep<Name> token within [lo-win, hi+win]."""
    region = data[max(0, lo - win):min(len(data), hi + win)]
    m = re.search(rb'CortexStep([A-Z][A-Za-z0-9]+)', region)
    return m.group(1).decode('ascii') if m else None


def find_jetski_type_near(data: bytes, lo: int, hi: int, win: int = 2048) -> str | None:
    """Search for a `tools.<lower>...Args` or jetski/cortex/tools/.../<Name>Args
    style type name within [lo-win, hi+win]."""
    region = data[max(0, lo - win):min(len(data), hi + win)]
    # patterns like `cortex/tools/foo/foo.barToolArgs` or `tools.fooArgs`
    candidates = []
    for rx in [
        rb'cortex/tools/[\w/]+/(\w+)\.(\w+Args[A-Za-z0-9_]*)',
        rb'cortex/tools/[\w/]+/(\w+)\.(\w*Tool[A-Za-z0-9_]*)',
    ]:
        for m in re.finditer(rx, region):
            candidates.append(m.group(2).decode('ascii'))
    if candidates:
        # the closest to mid is best — return the most frequent one
        from collections import Counter
        return Counter(candidates).most_common(1)[0][0]
    return None


def main() -> None:
    data = BIN.read_bytes()
    needle = b'jsonschema_description:'

    # find every tag offset
    starts: list[int] = []
    i = 0
    while True:
        j = data.find(needle, i)
        if j < 0: break
        starts.append(j); i = j + 1

    # For each occurrence, walk back a few bytes to find the field's
    # flag byte (just before the namelen+name+taglen sequence). Try each
    # flag-byte candidate at j-2..j-200 that yields a successful parse
    # whose tag CONTAINS 'jsonschema_description:'.
    # Then walk that struct.
    structs: dict[tuple[int, int], list[dict]] = {}
    for j in starts:
        # search candidate flag positions
        anchor = None
        for cand in range(j - 1, max(j - 220, 0), -1):
            r = try_parse_field(data, cand)
            if r is None:
                continue
            f, n = r
            if 'jsonschema_description:' in f['tag'] and cand + n > j:
                anchor = cand; break
        if anchor is None:
            continue
        if any(lo <= anchor < hi for (lo, hi) in structs):
            continue
        fields, lo, hi = walk_struct(data, anchor)
        # filter: only fields with at least an ascii name (drop trash)
        if not fields:
            continue
        # Reject if the cluster has zero fields with jsonschema_description
        if not any('jsonschema_description:' in f['tag'] for f in fields):
            continue
        structs[(lo, hi)] = fields

    print(f'Recovered {len(structs)} field clusters')

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # tool name -> entries
    by_tool: dict[str, list] = defaultdict(list)
    summary: list[dict] = []
    for (lo, hi), fields in sorted(structs.items()):
        step = find_cortex_step_near(data, lo, hi)
        typ = find_jetski_type_near(data, lo, hi)
        key = step or typ or f'unknown_{lo:#x}'
        by_tool[key].append({
            'offset_lo': lo, 'offset_hi': hi,
            'fields': fields, 'step': step, 'jetski_type': typ,
        })
        summary.append({
            'tool': key, 'lo': lo, 'hi': hi,
            'field_count': len(fields),
            'desc_count': sum(1 for f in fields if 'jsonschema_description:' in f['tag']),
        })

    for tool, entries in sorted(by_tool.items()):
        path = OUT_DIR / f'{tool}.md'
        n = 2
        while path.exists():
            path = OUT_DIR / f'{tool}_{n}.md'; n += 1
        out = []
        out.append(f'# `{tool}` recovered field table\n')
        out.append('Recovered from Go reflect-name records in language-server binary.\n')
        for ent in entries:
            out.append(f'## Cluster @ {ent["offset_lo"]:#x}–{ent["offset_hi"]:#x}')
            if ent['step']:
                out.append(f'- Likely cortex step: `CortexStep{ent["step"]}`')
            if ent['jetski_type']:
                out.append(f'- Likely Go arg type: `{ent["jetski_type"]}`')
            out.append('')
            out.append('| field | flag | tag |')
            out.append('|---|---|---|')
            for f in ent['fields']:
                out.append(f'| `{f["name"]}` | {f["flag"]:#x} | `{f["tag"]}` |')
            out.append('')
            # decoded
            out.append('### Parsed tags')
            out.append('')
            for f in ent['fields']:
                pt = parse_decoded_tag(f['tag']) if f['tag'] else {}
                out.append(f'**`{f["name"]}`**')
                if pt:
                    for k, v in pt.items():
                        out.append(f'- `{k}` = `{v}`')
                else:
                    out.append('_(no parsable tag pairs)_')
                out.append('')
        path.write_text('\n'.join(out))

    # write index
    idx = ['# Recovered field tables', '']
    idx.append(f'{len(summary)} struct field clusters recovered by walking Go '
               'reflect-name records in the language-server binary, anchored on '
               '`jsonschema_description:` tag occurrences.\n')
    idx.append('| tool | fields | descriptions | offset |')
    idx.append('|---|---:|---:|---|')
    for s in sorted(summary, key=lambda x: x['tool']):
        idx.append(f'| `{s["tool"]}` | {s["field_count"]} | {s["desc_count"]} | '
                   f'{s["lo"]:#x} |')
    (OUT_DIR / 'README.md').write_text('\n'.join(idx) + '\n')

    # also write a flat JSON for scripts/tooling
    (OUT_DIR / 'all.json').write_text(json.dumps({
        'structs': [{
            'tool': s['tool'], 'offset_lo': s['lo'], 'offset_hi': s['hi'],
            'field_count': s['field_count'], 'desc_count': s['desc_count'],
        } for s in summary]
    }, indent=2) + '\n')


if __name__ == '__main__':
    main()
