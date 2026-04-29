#!/usr/bin/env python3
"""
Build a single authoritative tool-argument catalog from:
  1. byte-exact inline-shape structs (jsonschema_structs/)
  2. byte-exact rname-record field tables (recovered_field_tables/)
  3. cortex.proto messages (CortexStep* tool inputs)

Output: tool_shapes/catalog/<tool>.md  with:
  - canonical proto schema (from cortex.proto, if present)
  - recovered byte-exact field+tag entries that can be confidently
    attributed to this tool

Also: tool_shapes/catalog/_field_index.md  flat searchable index of every
recovered (name, tag) tuple in the binary.
"""
from __future__ import annotations
import re
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/michael/projects/antigravity-prompts')
BIN = Path('/Applications/Antigravity.app/Contents/Resources/app/extensions/antigravity/bin/language_server_macos_arm')
OUT = ROOT / 'tool_shapes' / 'catalog'

# import the field-walker module so we re-use parse_decoded_tag etc.
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from extract_field_tables import (  # type: ignore
    try_parse_field, walk_struct, parse_decoded_tag, find_cortex_step_near,
)


def load_proto_messages() -> dict[str, list[tuple[str, str, int, str]]]:
    """Return { 'CortexStepFoo': [(field_name, type, number, label), ...] }
    parsed from cortex.proto. We read the regenerated proto file already in
    the repo.
    """
    p = ROOT / 'protos/third_party/jetski/cortex_pb/cortex.proto'
    text = p.read_text()
    msgs: dict[str, list[tuple[str, str, int, str]]] = {}
    cur: str | None = None
    fields: list[tuple[str, str, int, str]] = []
    depth = 0
    for line in text.splitlines():
        stripped = line.strip()
        m = re.match(r'^message\s+(\w+)\s*\{', stripped)
        if m:
            cur = m.group(1); fields = []; depth = 1
            continue
        if cur is None:
            continue
        depth += line.count('{')
        depth -= line.count('}')
        if depth <= 0:
            if cur.startswith('CortexStep'):
                msgs[cur] = fields
            cur = None; fields = []
            continue
        # field line: "[label] type name = number;"
        # labels: optional, repeated
        fm = re.match(
            r'^(?:(optional|repeated)\s+)?'
            r'([\w\.]+)\s+(\w+)\s*=\s*(\d+)\s*;', stripped)
        if fm:
            label = fm.group(1) or ''
            ftype = fm.group(2)
            fname = fm.group(3)
            fnum = int(fm.group(4))
            fields.append((fname, ftype, fnum, label))
    return msgs


def snake(name: str) -> str:
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    return s.lower()


def collect_recovered() -> list[dict]:
    """Walk the binary again to collect every (name, tag, offset) tuple
    we can recover. Returns flat list of dicts."""
    data = BIN.read_bytes()
    needle = b'jsonschema_description:'
    starts: list[int] = []
    i = 0
    while True:
        j = data.find(needle, i)
        if j < 0:
            break
        starts.append(j); i = j + 1

    seen_ranges: list[tuple[int, int]] = []
    entries: list[dict] = []
    for j in starts:
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
        if any(lo <= anchor < hi for (lo, hi) in seen_ranges):
            continue
        fields, lo, hi = walk_struct(data, anchor)
        seen_ranges.append((lo, hi))
        # also try to recover a parent CortexStep nearby
        step = find_cortex_step_near(data, lo, hi, win=2048)
        for f in fields:
            entries.append({
                'name': f['name'],
                'tag': f['tag'],
                'offset': f['offset'],
                'cluster': (lo, hi),
                'cortex_step_hint': step,
                'parsed': parse_decoded_tag(f['tag']),
            })
    return entries


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    proto_msgs = load_proto_messages()
    print(f'Loaded {len(proto_msgs)} CortexStep* proto messages')

    recovered = collect_recovered()
    print(f'Recovered {len(recovered)} byte-exact (name, tag) entries')

    # also load inline-shape structs we already extracted
    inline_dir = ROOT / 'tool_shapes' / 'jsonschema_structs'
    inline_files: dict[str, str] = {}
    if inline_dir.exists():
        for p in inline_dir.glob('*.md'):
            if p.name == 'README.md':
                continue
            inline_files[p.stem] = p.read_text()

    # ----- attribution: by field-name match against proto -----
    # For each recovered entry, list which CortexStep messages contain a
    # field with the SAME snake-case name. If exactly one match, attribute.
    name_to_steps: dict[str, list[str]] = defaultdict(list)
    for step, fs in proto_msgs.items():
        for fname, _t, _n, _l in fs:
            name_to_steps[fname].append(step)

    # CONSERVATIVE attribution: only attribute when BOTH signals agree.
    #
    # Why so strict? cortex.proto's CortexStep<X> messages describe the
    # *outcome state* of a tool call (what's stored in the trajectory),
    # not the JSON-schema input args. The actual arg structs (e.g.
    # `tools.runCommandArgs`, `notebook.editNotebookArgs`) are a separate
    # object hierarchy. Matching only by proto-field name routinely yields
    # false positives (e.g. attributing 'Mouse button to release.' to
    # CortexStepCaptureBrowserConsoleLogs because both happen to have a
    # 'Button' field).
    #
    # Therefore we only mark a record as attributed when:
    #   (proto-field-name match)  AND  (spatial CortexStep hint == that step)
    by_step: dict[str, list[dict]] = defaultdict(list)
    unattributed: list[dict] = []
    for e in recovered:
        proto_candidates = set(name_to_steps.get(snake(e['name']), []))
        hinted = f'CortexStep{e["cortex_step_hint"]}' if e['cortex_step_hint'] else None
        if hinted and hinted in proto_candidates:
            e['attributed_to'] = hinted
            by_step[hinted].append(e)
        else:
            e['attributed_to'] = None
            unattributed.append(e)

    # ----- emit per-tool catalog markdown -----
    for step, fs in sorted(proto_msgs.items()):
        tool_slug = snake(step.replace('CortexStep', '', 1))
        if not tool_slug:
            continue
        lines = []
        lines.append(f'# `{tool_slug}` (`{step}`)\n')
        lines.append('Authoritative tool-argument catalog. Combines:\n')
        lines.append('- canonical proto schema (recovered from `cortex.proto`)\n')
        lines.append('- byte-exact `(field, tag)` recovered from Go reflect '
                     'rname records in the binary, when attributable\n')
        lines.append('## Proto schema\n')
        lines.append('```proto')
        lines.append(f'message {step} ' + '{')
        for fname, ft, fn, label in fs:
            lab = (label + ' ') if label else ''
            lines.append(f'  {lab}{ft} {fname} = {fn};')
        lines.append('}')
        lines.append('```\n')

        # byte-exact recoveries
        attr = [e for e in by_step.get(step, []) if e['attributed_to'] == step]
        if attr:
            lines.append('## Recovered byte-exact field tags\n')
            seen = set()
            for e in attr:
                key = (e['name'], e['tag'])
                if key in seen:
                    continue
                seen.add(key)
                lines.append(f'### `{e["name"]}` (binary offset {e["offset"]:#x})')
                lines.append('')
                lines.append('Raw tag:')
                lines.append('```')
                lines.append(e['tag'])
                lines.append('```')
                lines.append('Decoded:')
                lines.append('')
                for k, v in e['parsed'].items():
                    lines.append(f'- `{k}` = `{v}`')
                lines.append('')
        else:
            lines.append('## Recovered byte-exact field tags\n')
            lines.append('_(no `jsonschema_description:` tags attributable to this tool '
                         'were recovered from the binary)_\n')

        (OUT / f'{tool_slug}.md').write_text('\n'.join(lines))

    # ----- flat field index, ordered by tag content for readability -----
    idx = ['# Recovered field index', '']
    idx.append(f'**{len(recovered)}** byte-exact `(field_name, tag)` records '
               'recovered from Go reflect-name tables in the language-server '
               'binary. Each row is a real field that exists in some tool\'s '
               'argument struct, with its raw Go reflect tag string verbatim.\n')
    idx.append('**Attribution is intentionally conservative.** A record is '
               'tagged with a `CortexStep<X>` only when both signals agree: '
               'the field name matches a proto field of that step in '
               '`cortex.proto`, AND a `CortexStep<X>` token appears within '
               '~2KB of the field\'s rodata position. Records where the '
               'signals disagree or only one fires are left as '
               '`_unattributed_`.\n')
    idx.append('Why? `CortexStep<X>` proto messages describe the *outcome '
               'state* of a tool call. The actual JSON-schema *input args* '
               'live in separate Go structs (e.g. `tools.runCommandArgs`, '
               '`notebook.editNotebookArgs`). A name-only match between the '
               'two namespaces routinely yields false positives.\n')
    idx.append('## Attributed records\n')
    attributed = [e for e in recovered if e['attributed_to']]
    idx.append(f'_{len(attributed)} of {len(recovered)} records have a high-confidence attribution._\n')
    idx.append('| attributed_to | field | tag |')
    idx.append('|---|---|---|')
    for e in sorted(attributed, key=lambda x: (x['attributed_to'], x['name'])):
        tag = e['tag'].replace('|', r'\|')
        idx.append(f'| `{e["attributed_to"]}` | `{e["name"]}` | `{tag}` |')
    idx.append('')
    idx.append('## Unattributed records\n')
    idx.append(f'_{len(unattributed)} byte-exact records whose owning tool '
               'could not be confidently determined from static signals. The '
               'tags are nevertheless real and verbatim; matching them to '
               'tools requires reading the descriptive text._\n')
    idx.append('| field | tag |')
    idx.append('|---|---|')
    for e in sorted(unattributed, key=lambda x: (x['name'], x['tag'])):
        tag = e['tag'].replace('|', r'\|')
        idx.append(f'| `{e["name"]}` | `{tag}` |')
    (OUT / '_field_index.md').write_text('\n'.join(idx) + '\n')

    # summary: how many tools got at least one tag
    covered = {step for step, es in by_step.items() if any(e['attributed_to'] == step for e in es)}
    print(f'Tools with >=1 attributed byte-exact tag: {len(covered)} / {len(proto_msgs)}')
    print(f'Unattributed records: {len(unattributed)}')


if __name__ == '__main__':
    main()
