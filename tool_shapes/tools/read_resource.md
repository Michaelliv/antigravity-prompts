# `read_resource`

**Cortex step type:** `CortexStepReadResource`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepReadResource {
  string server_name = 1;
  string uri = 2;
  repeated exa.codeium_common_pb.McpResourceContent contents = 3;
  bool skipped_non_image_binary_content = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `uri`
```
The action to perform: 'list' (list all running tasks), 'kill' (cancel the task), 'status' (check the task status and log URI), 'send_input' (send input to a running task).
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
