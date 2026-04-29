# `install_applet_package`

**Cortex step type:** `CortexStepInstallAppletPackage`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepInstallAppletPackage {
  string package_name = 1;
  string error_message = 2;
  string logs = 3;
  bool is_dev_dependency = 4;
  repeated string package_names = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `logs`
```
page_id of the Browser page to capture console logs of.
```
