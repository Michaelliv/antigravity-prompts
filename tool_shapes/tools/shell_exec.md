# `shell_exec`

**Cortex step type:** `CortexStepShellExec`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepShellExec {
  string command = 1;
  int32 exit_code = 2;
  string output = 3;
  string error_message = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `command`
```
ID of the command to get status for
```
```
The current working directory for the command
```
```
The exact command line string to execute.
```

### `output`
```
The command ID from a previous run_command call. This is returned in the run_command output.
```
```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```
