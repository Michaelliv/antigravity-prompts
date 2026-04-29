# `execute_notebook`

**Cortex step type:** `CortexStepExecuteNotebook`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepExecuteNotebook {
  string tool_name = 1;
  exa.cortex_pb.CortexStepExecuteNotebook.Args args = 2;
  exa.cortex_pb.CortexStepExecuteNotebook.Reply reply = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
