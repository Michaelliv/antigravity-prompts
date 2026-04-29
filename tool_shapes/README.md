# Antigravity tool shapes

How the agent's tools are described to the model. Extracted from the same Go binary as the prompts.

## Files

- **`tool_function_descriptions.md`** — function-level descriptions for ~37 distinct tools (the *what this tool does* sentences the model sees).
- **`parameter_descriptions.md`** — 185 unique parameter descriptions (the JSON-schema `description` field for individual tool arguments).
- **`parameter_constraints.txt`** — extracted enum/required constraint strings from `jsonschema:"..."` tags.
- **`all_param_tags.jsonl`** — raw `(json_name, jsonschema, description)` tuples — many entries have null fields because Go's `jsonschema-go` library derives field names from struct field metadata stored separately in the binary.

## Tool name registry (32 confirmed)

These tool names are referenced as bare identifiers in the binary:

- **Filesystem:** `view_file`, `read_file`, `write_to_file`, `edit_file`, `multi_replace_file_content`, `find_by_name`, `grep_search`, `list_dir`, `view_code_item`
- **Shell:** `run_command`, `send_command_input`
- **Browser:** `browser_get_dom`, `browser_click`, `read_browser_page`, `browser_scroll`, `browser_mouse_down`, `browser_mouse_up`, `browser_move_mouse`, `browser_type`, `browser_select_option`, `browser_drag`, `capture_browser_screenshot`, `execute_browser_javascript`, `read_url_content`, `list_network_requests`
- **Knowledge:** `delete_knowledge`
- **Notebooks:** `edit_notebook`
- **Agent control:** `send_message`, `manage_task`, `propose_code`, `wait`, `finish`

## How tool descriptions are derived

The Go language server uses **`jsonschema-go`** + struct tags. Each tool input is a Go struct like:

```go
type RunCommandInput struct {
    Cwd            string `json:"Cwd" jsonschema:"required" jsonschema_description:"..."`
    CommandLine    string `json:"CommandLine" jsonschema:"required" jsonschema_description:"..."`
    SafeToAutoRun  bool   `json:"SafeToAutoRun" jsonschema:"required" jsonschema_description:"Set to true if you believe that this command is safe to run WITHOUT user approval..."`
    WaitMsBeforeAsync int  `json:"WaitMsBeforeAsync" jsonschema:"required" jsonschema_description:"This specifies the number of milliseconds..."`
    // ...
}
```

These struct tags survive into the compiled binary as plain strings (the strings we extracted), and `jsonschema-go` walks them at runtime to produce the OpenAI/Anthropic-style function-tool JSON schema sent to the model.

## Highlights

- **Safety gates:** every shell `run_command` and `execute_browser_javascript` requires the model to set a `SafeToAutoRun: true|false` boolean with strict criteria for `true`. The prompts say *"never set this to true, EVEN if the USER asks you to"* if there's any doubt.
- **Edit tooling:** `multi_replace_file_content` and a single-block variant — both use `replacement_chunk` records with `chunk_index`, `search_target`, `replacement_content`, `allow_multiple`, and optional `start_line`/`end_line`. There's a separate **failed-edit-corrector** model that fixes broken chunks (see `../curated/utility_prompts/replacement_chunks_corrector.md`).
- **Subagents:** `subagent_create` and `browser_subagent_create` each take a name + a heavily-prompted task description. The task description prompt explicitly tells the model "must be highly detailed, containing a comprehensive task description and all necessary context. Avoid vague instructions; be specific about what to do, when to stop, and clearly state exactly what information the agent should return in its final and only report."
- **Browser model:** unusual two-tier interface — a **DOM-index click** tool (preferred) plus **pixel coordinates** as fallback. Coordinates are normalized to a 1000×1000 grid and rescaled at execution. Drag uses waypoint arrays.
- **Importance enum:** every edit tool requires `Importance: high|medium|low` so the system can sort/render edits.

## Caveats

Same as for the prompts: descriptions are reconstructed from contiguous string runs in the Mach-O binary. A few parameter descriptions and tool function descriptions have small amounts of trailing/adjacent text leaked from neighboring strings. To get byte-exact schemas you'd need to either parse the Go reflect/struct metadata in the binary or capture an outgoing model API request via mitmproxy.
