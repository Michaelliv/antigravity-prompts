# `workspace_api`

**Cortex step type:** `CortexStepWorkspaceAPI`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepWorkspaceAPI {
  string url = 1;
  string http_method = 2;
  string body = 3;
  string description = 4;
  int32 status_code = 5;
  string response = 6;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
