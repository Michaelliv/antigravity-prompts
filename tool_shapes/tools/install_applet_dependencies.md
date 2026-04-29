# `install_applet_dependencies`

**Cortex step type:** `CortexStepInstallAppletDependencies`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (2)

```proto
message CortexStepInstallAppletDependencies {
  string error_message = 1;
  string logs = 2;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `logs`
```
page_id of the Browser page to capture console logs of.
```
