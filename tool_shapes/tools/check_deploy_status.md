# `check_deploy_status`

**Cortex step type:** `CortexStepCheckDeployStatus`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

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

From `jsonschema_description:` tags in the binary, matched by field name.
