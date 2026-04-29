# `list_directory`

**Cortex step type:** `CortexStepListDirectory`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepListDirectory {
  string directory_path_uri = 1;
  repeated string children = 2;
  repeated exa.cortex_pb.ListDirectoryResult results = 3;
  bool dir_not_found = 4;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
