# `workspace_a_p_i`

**Cortex step type:** `CortexStepWorkspaceAPI`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (6)

```proto
message CortexStepWorkspaceAPI {
  string url = 1;
  string http_method = 2;
  string body = 3;
  string description = 4;
  int32 status_code = 5;
  string response = 6;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `url`
```
URL to read content from
```
```
The URL to open in the user's browser.
```
```
Type of reference (e.g., file, conversation_id, url)
```

### `body`
```
Request body JSON
```

### `description`
```
A description of the changes that you are making to the file.
```
```
Human-readable description of the JavaScript to execute
```
```
Human-readable description of what this subagent does and when it should be used.
```

### `response`
```
The text for each option, formatted as the user's response. Must have at least 2 options. Do NOT add an 'Other' option to questions.
```
