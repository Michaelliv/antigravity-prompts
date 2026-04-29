# `set_up_cloud_sql`

**Cortex step type:** `CortexStepSetUpCloudSql`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepSetUpCloudSql {
  string error_message = 1;
  exa.cortex_pb.SetUpCloudSqlErrorCode rpc_error_code = 2;
  exa.cortex_pb.SetUpCloudSqlResult result = 3;
  exa.cortex_pb.SetUpCloudSqlAppConfig app_config = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
