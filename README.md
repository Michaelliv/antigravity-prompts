# Antigravity prompts (extracted)

Prompts and templates extracted from Google Antigravity's native language-server binary.

## Source

- **Binary:** `/Applications/Antigravity.app/Contents/Resources/app/extensions/antigravity/bin/language_server_macos_arm`
- **Antigravity version:** 1.23.2 (build commit `15487b30…`, dated 2026-04-16)
- **Origin paths in the binary** (Go embed.FS): `google3/third_party/jetski/prompt/template_provider/templates/...`

The Electron extension (`dist/extension.js`) is a thin client and contains **no** model prompts. The native Go-built language server is the workhorse: it talks to `https://cloudcode-pa.googleapis.com` and assembles all prompts client-side from these templates before sending. Model-side system prompts are therefore embedded in this binary as Go `text/template` files compiled in via `embed.FS`.

## How extraction worked

1. Dumped every printable byte run (`[ -~\n\t]{200,}`) from the 93 MB Mach-O binary.
2. Filtered runs by prompt heuristics (`{{...}}`, `You are`, markdown headings, `<USER_REQUEST>`, etc.).
3. Trimmed each run at the first non-prompt boundary (Chroma syntax theme XML, protobuf descriptors, language-id soup).
4. Named files by content fingerprint and organized into folders.

## Directory layout

```
curated/
  system_prompts/      # Core agent system-prompt sections
    identity.tmpl
    identity_agent.tmpl
    identity_cascade_legacy.tmpl       # Windsurf/Codeium ancestor identity
    guidelines.tmpl                    # behavioral guidelines (with internal annotations)
    planning_mode.tmpl
    planning_mode_artifacts.tmpl
    batch_function_calling.tmpl
    artifacts_naming.md
    artifacts_organization.md
    knowledge_items_workflow.md
    knowledge_items_retrieval.md
    knowledge_items_other.md           # full KI generate/consolidate/delete behavior spec
    knowledge_items_examples.md
    sidecar_scripts.md
    conversation_logs.md
    reactive_wakeup.md
    cider_critique_guide.md            # Google-internal Critique/Gerrit assistant guide
  step_templates/      # How each tool-call step is rendered for the model
    run_command.tmpl
    send_command_input.tmpl
    default_status_output.tmpl
  subagent_prompts/    # Subagent / background-agent prompts
    background_agent_knowledge_extractor.md
    browser_subagent_actions.md
    parent_conversation_context.md
    persona_*.md
    subagent_task_handoff.tmpl
    subagent_task_short.tmpl
  envelopes/           # Wrappers around user/system messages
    ephemeral_message.md
    ephemeral_message_v2.md
  utility_prompts/     # Single-purpose helpers
    replacement_chunks_corrector.md
    failed_replacements.md
  reminders/           # Standalone reminder snippets injected on demand
    reminder_*.md
  misc/                # Lower-confidence / supporting templates

tool_shapes/           # Tool catalog: function + parameter descriptions, constraints
```

## Highlights

- **`system_prompts/identity.tmpl`** — the canonical opener: `You are Antigravity, a powerful agentic AI coding assistant designed by the Google Deepmind team working on Advanced Agentic Coding.`
- **`system_prompts/guidelines.tmpl`** — contains a real internal annotation: `Note(chmatthew, 2026-03-18): Added due to Opus 4.6 tendency to delete comments across a file.` (i.e. confirms Antigravity supports Claude Opus 4.6 and Google tracks behavior fixes per-model.)
- **`system_prompts/planning_mode.tmpl`** — full Planning Mode workflow (Research → Plan → Approval → Execute).
- **`system_prompts/knowledge_items_other.md`** — full Generate/Consolidate/Delete workflow for the persistent KI memory system (the "brain" / "knowledge" directories under `~/.gemini/antigravity/`).
- **`step_templates/run_command.tmpl`** — exactly how shell-command tool calls are rendered back into the conversation, including cancel/exit/background-snapshot branches.
- **`subagent_prompts/`** — separate persona prompts for: research subagent, browser subagent, background knowledge extractor, generic task subagent.
- **`utility_prompts/replacement_chunks_corrector.md`** — the prompt for a *separate* model that fixes failed file edits by reformatting `replacement_chunk` blocks.

## Models the binary references

From `state.vscdb` + binary strings:
- Gemini 3 Pro (High / Low), Gemini 3 Flash
- Claude Sonnet 4.5, Claude Sonnet 4.5 (Thinking), Claude Opus 4.5 (Thinking), Claude Opus 4.6 (per guidelines comment)
- GPT-OSS 120B (Medium)
- Internal: `claude-sonnet-4-5@20250929`, `MODEL_GOOGLE_GEMINI_INTERNAL_BYOM`, `MODEL_GOOGLE_GEMINI_INFINITYBLOOM`, `MODEL_GOOGLE_GEMINI_EXAMPLE_GEMAX_SAMPLER`

## Endpoints

- `https://cloudcode-pa.googleapis.com` — primary model API
- `https://antigravity-unleash.goog/api` — feature-flag service
- OAuth client ID: `884354919052-36trc1jjb3tguiac32ov6cod268c5blh.apps.googleusercontent.com`

## Caveats

- **Not byte-exact.** Each `.tmpl` was reconstructed from contiguous string runs. Adjacent embedded files (Chroma themes, JSON schemas, jQuery snippets) sometimes leak into the tail; we trim aggressively but a few files may include or omit trailing characters. For byte-exact extraction, parse the Go binary's `embed.FS` index directly (look up the `templates/` paths in the `name` table and follow the offset/length tuples).
- The `misc/` and `reminders/` directories include lower-confidence fragments — useful as evidence but not all are complete templates.
- Extraction was best-effort and relied on heuristics; the file count (~45 curated, 78 raw) likely undercounts the total templates the agent uses.

## Reproduce

```sh
# Re-run extraction
python3 - <<'PY'
import re
data = open('/Applications/Antigravity.app/Contents/Resources/app/extensions/antigravity/bin/language_server_macos_arm','rb').read()
for m in re.finditer(rb'[ -~\n\t]{200,}', data):
    s = m.group(0).decode('utf-8','replace')
    if 'You are Antigravity' in s or '{{- /*' in s:
        print(f'--- @{m.start():#x} len={len(s)} ---')
        print(s[:500])
PY
```

Extracted on 2026-04-29.
