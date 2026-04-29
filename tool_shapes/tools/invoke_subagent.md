# `invoke_subagent`

**Cortex step type:** `CortexStepInvokeSubagent`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepInvokeSubagent {
  repeated exa.cortex_pb.SubagentSpec subagents = 9;
  repeated exa.cortex_pb.SubagentResult results = 10;
  string subagent_name = 1;
  string prompt = 2;
  string conversation_id = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `subagents`
```
A 2-5 word description of the subagent's role. Should read similar to a job title, e.g. 'Codebase Researcher', 'Database Debugger', etc. Should also be detailed enough to distinguish between different subagents who might share similar purposes.
```

### `prompt`
```
Title of the prompt section.
```
```
The text prompt to generate an image for.
```
```
Content of the prompt section.
```

### `conversation_id`
```
Type of reference (e.g., file, conversation_id, url)
```
