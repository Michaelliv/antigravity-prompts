# `view_code_item`

**Cortex step type:** `CortexStepViewCodeItem`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepViewCodeItem {
  string absolute_uri = 1;
  repeated string node_paths = 4;
  repeated exa.codeium_common_pb.CodeContextItem ccis = 5;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 6;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
