# `ViewFileToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (9)

```proto
message ViewFileToolConfig {
  bool allow_view_gitignore = 7;
  bool split_outline_tool = 8;
  bool show_triggered_memories = 13;
  uint32 max_lines_per_view = 14;
  bool include_line_numbers = 15;
  repeated string dir_allowlist = 16;
  uint32 max_total_outline_bytes = 9;
  uint32 max_bytes_per_outline_item = 11;
  uint32 show_full_file_bytes = 10;
}
```
