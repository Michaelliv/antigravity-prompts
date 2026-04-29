# `lint_applet`

**Cortex step type:** `CortexStepLintApplet`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepLintApplet {
  int32 exit_code = 1;
  string output = 2;
  string error_message = 3;
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
