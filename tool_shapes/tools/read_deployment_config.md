# `read_deployment_config`

**Cortex step type:** `CortexStepReadDeploymentConfig`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (9)

```proto
message CortexStepReadDeploymentConfig {
  string project_path = 1;
  string deployment_config_uri = 2;
  exa.codeium_common_pb.WebAppDeploymentConfig deployment_config = 3;
  repeated string missing_file_uris = 4;
  bool will_upload_node_modules = 5;
  bool will_upload_dist = 6;
  repeated string ignore_file_uris = 7;
  uint32 num_files_to_upload = 8;
  repeated string env_file_uris = 9;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
