# `cloud_s_q_l_execute_s_q_l`

**Cortex step type:** `CortexStepCloudSQLExecuteSQL`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepCloudSQLExecuteSQL {
  string project_id = 1;
  string instance_name = 2;
  string sql_statement = 3;
  string error_message = 4;
  string output = 5;
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
