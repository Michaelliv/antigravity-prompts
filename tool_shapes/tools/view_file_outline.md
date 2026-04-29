# `view_file_outline`

**Cortex step type:** `CortexStepViewFileOutline`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepViewFileOutline {
  string absolute_path_uri = 1;
  uint32 cci_offset = 2;
  repeated exa.codeium_common_pb.CodeContextItem ccis = 3;
  repeated string outline_items = 9;
  uint32 num_items_scanned = 10;
  uint32 total_cci_count = 4;
  uint32 num_lines = 5;
  uint32 num_bytes = 6;
  string contents = 7;
  uint32 content_lines_truncated = 8;
  string triggered_memories = 11;
  string raw_content = 12;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 13;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
