# `compile_applet`

**Cortex step type:** `CortexStepCompileApplet`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (2)

```proto
message CortexStepCompileApplet {
  string error_message = 1;
  string logs = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `logs`
```
page_id of the Browser page to capture console logs of.
```
