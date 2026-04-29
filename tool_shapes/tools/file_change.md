# `file_change`

**Cortex step type:** `CortexStepFileChange`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (8)

```proto
message CortexStepFileChange {
  string absolute_path_uri = 1;
  exa.cortex_pb.FileChangeType file_change_type = 2;
  repeated exa.cortex_pb.ReplacementChunk replacement_chunks = 3;
  string instruction = 5;
  exa.diff_action_pb.DiffBlock diff = 4;
  repeated exa.cortex_pb.ReplacementChunkInfo replacement_infos = 6;
  exa.cortex_pb.FastApplyFallbackInfo fast_apply_fallback_info = 7;
  bool overwrite = 8;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `overwrite`
```
Set this to true to overwrite an existing file. WARNING: This will replace the entire file contents. Only use when you explicitly intend to overwrite. Otherwise, use a code edit tool to modify existing files.
```
