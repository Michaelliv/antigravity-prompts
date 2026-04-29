# `cloud_sql_schema_update`

**Cortex step type:** `CortexStepCloudSQLSchemaUpdate`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCloudSQLSchemaUpdate {
  string error_message = 1;
  exa.cortex_pb.CloudSQLUpdateSchemaErrorCode rpc_error_code = 2;
  exa.cortex_pb.CloudSQLUpdateSchemaResult result = 3;
  string output = 4;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
