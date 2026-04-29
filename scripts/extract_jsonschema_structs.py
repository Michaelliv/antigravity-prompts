#!/usr/bin/env python3
from __future__ import annotations
"""
Extract byte-exact tool-argument structs from the Antigravity language server.

Strategy: scan the binary for Go generic instantiation symbol strings of the
form

    google3/.../utils.ToJsonSchemaString[go.shape.struct { ... }]
    google3/.../utils.ParseToolArgs[go.shape.struct { ... }]

These symbols are emitted for every tool whose argument struct is converted
to a JSON Schema at runtime. The body inside `go.shape.struct { ... }` is the
exact field list with types and Go reflect tags (json, jsonschema, etc.).

We:
  1. find all such symbols
  2. parse the inline struct body
  3. resolve embedded named types (e.g. `tools.TabCodeEditArgs`) by locating
     a separate `go.shape.struct` definition for them in the binary
  4. emit one Markdown file per recovered struct
"""
import re
import json
import os
import sys
from pathlib import Path
from collections import defaultdict

BIN = Path('/Applications/Antigravity.app/Contents/Resources/app/extensions/antigravity/bin/language_server_macos_arm')
OUT_DIR = Path('/Users/michael/projects/antigravity-prompts/tool_shapes/jsonschema_structs')


def find_runs(data: bytes) -> list[tuple[int, str]]:
    """Return printable-ASCII runs >= 40 chars with their start offsets."""
    return [(m.start(), m.group().decode('utf-8', 'replace'))
            for m in re.finditer(rb'[ -~]{40,}', data)]


def split_balanced(body: str, sep: str = ';') -> list[str]:
    """Split top-level by `sep`, ignoring sep inside [], {}, and ""."""
    out, buf, depth, in_q = [], [], 0, False
    i = 0
    while i < len(body):
        c = body[i]
        if c == '\\' and i + 1 < len(body):
            buf.append(c); buf.append(body[i + 1]); i += 2; continue
        if c == '"':
            in_q = not in_q
            buf.append(c); i += 1; continue
        if not in_q:
            if c in '[{':
                depth += 1
            elif c in ']}':
                depth -= 1
            elif c == sep and depth == 0:
                out.append(''.join(buf).strip())
                buf = []
                i += 1
                continue
        buf.append(c); i += 1
    if buf:
        out.append(''.join(buf).strip())
    return [x for x in out if x]


TAG_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parse_struct_body(body: str) -> list[dict]:
    """Parse contents of `struct { ... }`.

    Each field is one of:
        Name Type "tag"
        Name Type
        EmbeddedTypeName            (e.g. google3/.../foo.Bar)
        *EmbeddedTypeName
    """
    fields = []
    for raw in split_balanced(body, ';'):
        if not raw:
            continue
        # capture trailing `"..."` tag (with escaped quotes) if present
        tag_match = re.search(r'"((?:[^"\\]|\\.)*)"\s*$', raw)
        tag_str = ''
        head = raw
        if tag_match:
            tag_str = tag_match.group(1)
            head = raw[:tag_match.start()].strip()

        # head is now `Name Type` or just `EmbeddedType`
        # Tokenize: capture an identifier or *identifier then the rest is type
        m = re.match(
            r'^(?P<name>\*?[A-Za-z_][\w./\[\]]*)(?:\s+(?P<typ>.+))?$',
            head, re.S)
        if not m:
            continue
        name = m.group('name')
        typ = (m.group('typ') or '').strip()

        if not typ:
            # embedded type
            fields.append({
                'kind': 'embedded',
                'type': name.lstrip('*'),
                'pointer': name.startswith('*'),
                'tag': decode_go_tag(tag_str),
                'tag_raw': tag_str,
            })
        else:
            fields.append({
                'kind': 'field',
                'name': name,
                'type': typ,
                'tag': decode_go_tag(tag_str),
                'tag_raw': tag_str,
            })
    return fields


def decode_go_tag(tag_str: str) -> dict[str, str]:
    """Parse a Go reflect tag string like
        json:\"foo\" jsonschema:\"required\" jsonschema_description:\"X\"
    where the literal escapes are present (we already pulled it out of an
    outer quoted string). We accept both raw and \\\"-escaped variants.
    """
    if not tag_str:
        return {}
    # Unescape \" -> "
    tag = tag_str.replace('\\"', '"').replace('\\\\', '\\')
    out = {}
    i = 0
    while i < len(tag):
        # skip whitespace
        while i < len(tag) and tag[i] in ' \t':
            i += 1
        # key
        m = re.match(r'([A-Za-z_][\w]*):"', tag[i:])
        if not m:
            break
        key = m.group(1)
        i += m.end()
        # value: read until unescaped "
        v = []
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


# ---- top-level extraction ----

SHAPE_RE = re.compile(r'go\.shape\.struct\s*\{')


def find_struct_at(s: str, idx: int) -> str | None:
    """Given `s` containing 'go.shape.struct {' starting at idx, return the
    body up to the matching `}`. Quotes and brackets are tracked."""
    open_paren = s.find('{', idx)
    if open_paren < 0:
        return None
    depth = 1
    i = open_paren + 1
    in_q = False
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            i += 2; continue
        if c == '"':
            in_q = not in_q
        elif not in_q:
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return s[open_paren + 1:i]
        i += 1
    return None


def extract_all(data: bytes) -> dict:
    """Return {
        'tools':   { caller_symbol: parsed_struct_dict },
        'named':   { qualified_type_name: parsed_struct_dict },
    }"""
    runs = find_runs(data)
    tools = {}
    named = defaultdict(list)

    # Two patterns of interest:
    # (a) ToJsonSchemaString[go.shape.struct { ... }]   ← per-tool top-level args
    # (b) (T).method or constructor strings that contain `tools.Foo` followed by
    #     `go.shape.struct { ... }` defining `tools.Foo`'s body

    for off, s in runs:
        for sym in ('ToJsonSchemaString[', 'ParseToolArgs['):
            pos = 0
            while True:
                p = s.find(sym, pos)
                if p < 0:
                    break
                pos = p + 1
                # locate the go.shape.struct that opens after this
                m = SHAPE_RE.search(s, p)
                if not m or m.start() > p + 200:
                    continue
                body = find_struct_at(s, m.start())
                if body is None:
                    continue
                # Caller-symbol context: anything before sym, up to last newline
                key = f'{sym.rstrip("[")}@{off:#x}+{p}'
                fields = parse_struct_body(body)
                tools[key] = {
                    'symbol': sym.rstrip('['),
                    'offset': off + p,
                    'raw_body': body,
                    'fields': fields,
                }

    # Also search for explicit definitions of tools.Foo via the
    # symbol pattern: '<package>.<Name>' followed by a `go.shape.struct { ... }`
    # that begins right after 'go.shape.' in a generic instantiation tied to
    # that named type. We do a simpler heuristic: scan for occurrences of
    # 'go.shape.<package>.<Name>' but Go usually emits the body inline only
    # when the struct is anonymous. For named types the runtime metadata is
    # in __go_type, which we already know is unparseable here.
    # Instead, look for the field-tag substrings appearing in close proximity
    # to the named type token to reconstruct a probable mapping.

    return {'tools': tools, 'named': dict(named)}


def slugify(s: str) -> str:
    s = re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_').lower()
    return s or 'unnamed'


def render_md(entry: dict) -> str:
    lines = []
    sym = entry['symbol']
    lines.append(f'# `{sym}` struct @ {entry["offset"]:#x}\n')
    lines.append('Recovered byte-exact from a Go generic instantiation symbol in the\n'
                 'language-server binary. This is the JSON-schema-source struct passed\n'
                 'to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.\n')
    lines.append('## Fields\n')
    for f in entry['fields']:
        if f['kind'] == 'embedded':
            ptr = '*' if f.get('pointer') else ''
            lines.append(f'- **embedded** `{ptr}{f["type"]}`')
            if f['tag']:
                for k, v in f['tag'].items():
                    lines.append(f'  - `{k}` = `{v}`')
        else:
            lines.append(f'- `{f["name"]}` _{f["type"]}_')
            for k, v in f['tag'].items():
                lines.append(f'  - `{k}` = `{v}`')
        lines.append('')
    lines.append('## Raw body\n')
    lines.append('```')
    lines.append(entry['raw_body'])
    lines.append('```\n')
    return '\n'.join(lines)


def main():
    data = BIN.read_bytes()
    result = extract_all(data)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # group by raw_body so equivalent ToJsonSchemaString/ParseToolArgs pairs
    # become one file
    groups = defaultdict(list)
    for k, v in result['tools'].items():
        groups[v['raw_body']].append(v)

    summary = []
    for body, entries in groups.items():
        first = entries[0]
        # Find a meaningful name. Prefer the first explicit field name; fall
        # back to first embedded type's basename.
        name = None
        for f in first['fields']:
            if f['kind'] == 'field':
                name = f['name']; break
        if name is None and first['fields']:
            name = first['fields'][0]['type'].split('/')[-1].split('.')[-1]
        if name is None:
            name = 'empty'
        slug = slugify(name)
        # disambiguate
        path = OUT_DIR / f'{slug}.md'
        n = 2
        while path.exists():
            path = OUT_DIR / f'{slug}_{n}.md'; n += 1
        path.write_text(render_md(first))
        summary.append({
            'file': path.name,
            'symbols': sorted({e['symbol'] for e in entries}),
            'fields': [(f.get('name') or f.get('type', '?')) for f in first['fields']],
            'tag_count': sum(len(f['tag']) for f in first['fields']),
        })

    # write index
    idx = ['# Recovered JSON-schema source structs', '']
    idx.append(f'{len(summary)} unique struct shapes recovered from '
               '`ToJsonSchemaString[…]` / `ParseToolArgs[…]` generic '
               'instantiation symbols in the language-server binary.\n')
    idx.append('| file | symbols | # fields | # tags |')
    idx.append('|---|---|---:|---:|')
    for s in sorted(summary, key=lambda x: x['file']):
        syms = ', '.join(f'`{x}`' for x in s['symbols'])
        idx.append(f'| [{s["file"]}]({s["file"]}) | {syms} | {len(s["fields"])} | {s["tag_count"]} |')
    (OUT_DIR / 'README.md').write_text('\n'.join(idx) + '\n')

    print(f'Wrote {len(summary)} struct files to {OUT_DIR}')


if __name__ == '__main__':
    main()
