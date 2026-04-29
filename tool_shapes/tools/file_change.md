# `file_change`

**Cortex step type:** `CortexStepFileChange`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
