# `invoke_subagent`

**Cortex step type:** `CortexStepInvokeSubagent`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
