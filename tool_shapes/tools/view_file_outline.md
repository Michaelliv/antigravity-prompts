# `view_file_outline`

**Cortex step type:** `CortexStepViewFileOutline`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (13)

```proto
message CortexStepViewFileOutline {
  string absolute_path_uri = 1;
  uint32 cci_offset = 2;
  repeated exa.codeium_common_pb.CodeContextItem ccis = 3;
  repeated string outline_items = 9;
  uint32 num_items_scanned = 10;
  uint32 total_cci_count = 4;
  uint32 num_lines = 5;
  uint32 num_bytes = 6;
  string contents = 7;
  uint32 content_lines_truncated = 8;
  string triggered_memories = 11;
  string raw_content = 12;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 13;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

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
