# `deploy_web_app`

**Cortex step type:** `CortexStepDeployWebApp`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (17)

```proto
message CortexStepDeployWebApp {
  string project_path = 1;
  string subdomain = 2;
  string project_id = 11;
  string framework = 3;
  bool user_confirmed = 4;
  repeated exa.cortex_pb.CortexStepDeployWebApp.FileUploadStatusEntry file_upload_status = 5;
  exa.codeium_common_pb.AntigravityDeployment deployment = 6;
  string deployment_config_uri = 7;
  exa.codeium_common_pb.WebAppDeploymentConfig deployment_config_output = 8;
  string subdomain_for_project_id = 12;
  string subdomain_user_specified = 13;
  string subdomain_used = 9;
  exa.codeium_common_pb.DeployTarget deploy_target_for_project_id = 15;
  exa.codeium_common_pb.DeployTarget deploy_target_user_specified = 16;
  exa.codeium_common_pb.DeployTarget deploy_target_used = 17;
  string project_id_used = 14;
  string claim_url = 10;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
