#!/usr/bin/env python3
"""
Finalize tool_shapes/ as a clean, honest catalog:

1. Rewrite all `tool_shapes/tools/<tool>.md` to keep ONLY the canonical proto
   schema (from cortex.proto). Remove the buggy "Field descriptions" section
   which used global field-name matching across structurally distinct
   namespaces and produced misleading attributions.

2. Build a single byte-exact field index `tool_shapes/byte_exact_field_index.md`
   listing every `(field_name, tag)` recovered from Go reflect-name records,
   un-attributed (because attribution from static signals is unreliable; see
   header for why).

3. Drop superseded files:
     tool_shapes/_unmatched_descriptions.md   (replaced by the index)
     tool_shapes/catalog/                     (heuristic experiment, removed)
"""
from __future__ import annotations
import re
import shutil
from pathlib import Path
import sys

ROOT = Path('/Users/michael/projects/antigravity-prompts')
sys.path.insert(0, str(ROOT / 'scripts'))
from extract_field_tables import (  # type: ignore
    try_parse_field, walk_struct, parse_decoded_tag,
)

BIN = Path('/Applications/Antigravity.app/Contents/Resources/app/extensions/antigravity/bin/language_server_macos_arm')


def load_proto_messages() -> dict[str, list[tuple[str, str, int, str]]]:
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
        fm = re.match(
            r'^(?:(optional|repeated)\s+)?'
            r'([\w\.]+)\s+(\w+)\s*=\s*(\d+)\s*;', stripped)
        if fm:
            fields.append((fm.group(3), fm.group(2), int(fm.group(4)),
                           fm.group(1) or ''))
    return msgs


def snake(name: str) -> str:
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    return s.lower()


def rewrite_tool_pages(msgs: dict) -> None:
    out_dir = ROOT / 'tool_shapes' / 'tools'
    # Wipe existing markdown files (they have the bad attributions).
    for p in out_dir.glob('*.md'):
        p.unlink()

    for step, fs in sorted(msgs.items()):
        slug = snake(step.replace('CortexStep', '', 1))
        if not slug:
            continue
        lines: list[str] = []
        lines.append(f'# `{slug}`\n')
        lines.append(f'**Cortex step type:** `{step}`\n')
        lines.append('**Source:** `third_party/jetski/cortex_pb/cortex.proto` '
                     '(byte-exact, recovered from the embedded '
                     '`FileDescriptorProto`)\n')
        lines.append('## Proto schema\n')
        lines.append('```proto')
        lines.append(f'message {step} ' + '{')
        for fname, ft, fn, label in fs:
            lab = (label + ' ') if label else ''
            lines.append(f'  {lab}{ft} {fname} = {fn};')
        lines.append('}')
        lines.append('```\n')
        lines.append('## Field descriptions\n')
        lines.append('See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) '
                     'for byte-exact `(field_name, jsonschema tag)` records '
                     'recovered from Go reflect-name tables in the binary. '
                     'Cortex-step proto messages and JSON-schema tool-arg '
                     'structs are different namespaces, so a clean static '
                     'attribution from one to the other is not possible. '
                     'Match by reading the description text against this '
                     'tool\'s purpose.\n')
        (out_dir / f'{slug}.md').write_text('\n'.join(lines))


def collect_recovered() -> list[dict]:
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
        for f in fields:
            entries.append({
                'name': f['name'],
                'tag': f['tag'],
                'offset': f['offset'],
                'parsed': parse_decoded_tag(f['tag']),
            })
    return entries


def write_field_index(entries: list[dict]) -> None:
    out = ROOT / 'tool_shapes' / 'byte_exact_field_index.md'
    lines: list[str] = []
    lines.append('# Byte-exact field index\n')
    lines.append(f'**{len(entries)}** verbatim `(field_name, struct-tag)` '
                 'records recovered from Go reflect-name tables in the '
                 'Antigravity language-server binary. Each row is a real '
                 'field in some tool\'s argument struct, with its raw Go '
                 'reflect tag string exactly as the compiler emitted it. '
                 'These tags are what the language server feeds to '
                 'jsonschema generation when it builds tool descriptors '
                 'for the model.\n')
    lines.append('## Why this is unattributed\n')
    lines.append(
        'Cortex-step proto messages (`CortexStep<X>` in `cortex.proto`) '
        'describe the *outcome state* of a tool call \u2014 what gets stored '
        'in the trajectory \u2014 not the JSON-schema *input args* the '
        'model fills in. The actual arg structs (e.g. `tools.runCommandArgs`, '
        '`notebook.editNotebookArgs`) live in a separate Go object hierarchy. '
        'They share neither field names nor object identity with the proto '
        'messages, so static signals (proto field-name match, rodata '
        'proximity to a `CortexStep<X>` token) routinely yield false '
        'positives. Earlier attempts to auto-attribute produced confidently '
        'wrong rows like *"Mouse button to release."* assigned to '
        '`CortexStepCaptureBrowserConsoleLogs`. The honest move is to '
        'present the recovered records flat. Attribution requires reading '
        'the descriptive text and is best done by a human or LLM with the '
        'tool\'s purpose in mind.\n')
    lines.append('## Records\n')
    lines.append('| field | tag | binary offset |')
    lines.append('|---|---|---:|')
    for e in sorted(entries, key=lambda x: (x['name'], x['tag'])):
        tag = e['tag'].replace('|', r'\|')
        lines.append(f'| `{e["name"]}` | `{tag}` | {e["offset"]:#x} |')
    out.write_text('\n'.join(lines) + '\n')


def main() -> None:
    msgs = load_proto_messages()
    print(f'Loaded {len(msgs)} CortexStep* proto messages')
    rewrite_tool_pages(msgs)
    print(f'Rewrote {len(msgs)} per-tool proto-only pages')

    entries = collect_recovered()
    print(f'Recovered {len(entries)} byte-exact (name, tag) entries')
    write_field_index(entries)

    # remove superseded artifacts
    superseded = [
        ROOT / 'tool_shapes' / '_unmatched_descriptions.md',
    ]
    for p in superseded:
        if p.exists():
            p.unlink()
            print(f'Removed superseded {p.relative_to(ROOT)}')

    cat_dir = ROOT / 'tool_shapes' / 'catalog'
    if cat_dir.exists():
        shutil.rmtree(cat_dir)
        print(f'Removed superseded {cat_dir.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
