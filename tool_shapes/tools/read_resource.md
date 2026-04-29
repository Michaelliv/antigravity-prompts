# `read_resource`

**Cortex step type:** `CortexStepReadResource`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepReadResource {
  string server_name = 1;
  string uri = 2;
  repeated exa.codeium_common_pb.McpResourceContent contents = 3;
  bool skipped_non_image_binary_content = 4;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
