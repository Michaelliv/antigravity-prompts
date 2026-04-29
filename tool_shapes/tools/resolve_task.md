# `resolve_task`

**Cortex step type:** `CortexStepResolveTask`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepResolveTask {
  string absolute_uri = 1;
  string title = 2;
  string description = 3;
  bool user_rejected = 4;
  exa.cortex_pb.TaskResolution resolution = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `title`
```
Human-readable title for the Knowledge Item
```
```
Title of the prompt section.
```
```
The question to ask the user. Do NOT add 'select all that apply' or similar text to the question title.
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
