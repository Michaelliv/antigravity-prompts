# `ephemeral_message`

**Cortex step type:** `CortexStepEphemeralMessage`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepEphemeralMessage {
  string content = 1;
  repeated exa.codeium_common_pb.Media media = 2;
  repeated string triggered_heuristics = 3;
  repeated exa.codeium_common_pb.Media attachments = 4;
  string dom_tree_uri = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
