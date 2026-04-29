# `check_deploy_status`

**Cortex step type:** `CortexStepCheckDeployStatus`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCheckDeployStatus {
  string antigravity_deployment_id = 1;
  exa.codeium_common_pb.AntigravityDeployment deployment = 2;
  exa.codeium_common_pb.DeploymentBuildStatus build_status = 3;
  string build_error = 4;
  string build_logs = 5;
  bool is_claimed = 6;
  string claim_url = 7;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
