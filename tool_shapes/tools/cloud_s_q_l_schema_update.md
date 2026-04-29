# `cloud_s_q_l_schema_update`

**Cortex step type:** `CortexStepCloudSQLSchemaUpdate`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepCloudSQLSchemaUpdate {
  string error_message = 1;
  exa.cortex_pb.CloudSQLUpdateSchemaErrorCode rpc_error_code = 2;
  exa.cortex_pb.CloudSQLUpdateSchemaResult result = 3;
  string output = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `output`
```
The command ID from a previous run_command call. This is returned in the run_command output.
```
```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```
