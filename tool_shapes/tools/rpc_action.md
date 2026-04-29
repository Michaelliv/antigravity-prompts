# `rpc_action`

**Cortex step type:** `CortexStepRPCAction`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepRPCAction {
  string service_name = 1;
  string method_name = 2;
  google.protobuf.Struct arguments = 3;
  string error_message = 4;
  google.protobuf.Struct result = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
