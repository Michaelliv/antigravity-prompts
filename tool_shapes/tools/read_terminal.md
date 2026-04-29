# `read_terminal`

**Cortex step type:** `CortexStepReadTerminal`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepReadTerminal {
  string process_id = 1;
  string name = 2;
  string contents = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `name`
```
Name of the server to read the resource from.
```
```
Name of the server to list available resources from.
```
```
Type name of the subagent to invoke.
```

### `contents`
```
The code contents to write to the file.
```
```
Path to list contents of, should be absolute path to a directory
```
```
The window contents width in display independent pixels. Only used when WindowState is 'normal'.
```
