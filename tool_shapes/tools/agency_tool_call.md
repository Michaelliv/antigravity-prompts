# `agency_tool_call`

**Cortex step type:** `CortexStepAgencyToolCall`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepAgencyToolCall {
  string agent_name = 1;
  string function_name = 2;
  repeated google.protobuf.Any request_messages = 3;
  repeated google.protobuf.Any response_messages = 4;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
