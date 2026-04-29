# `checkpoint`

**Cortex step type:** `CortexStepCheckpoint`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCheckpoint {
  uint32 checkpoint_index = 1;
  bool intent_only = 9;
  uint32 included_step_index_start = 11;
  uint32 included_step_index_end = 12;
  string conversation_title = 10;
  string user_intent = 4;
  string session_summary = 5;
  string code_change_summary = 6;
  bool model_summarization_failed = 16;
  bool used_fallback_summary = 17;
  repeated exa.cortex_pb.ArtifactSnapshot artifact_snapshots = 14;
  repeated string conversation_log_uris = 15;
  repeated exa.cortex_pb.TrajectoryFileDiff trajectory_file_diffs = 18;
  repeated string user_requests = 19;
  repeated exa.cortex_pb.SubagentSnapshot subagent_snapshots = 20;
  repeated exa.cortex_pb.TaskSnapshot running_task_snapshots = 21;
  repeated uint32 included_step_indices = 3;
  string memory_summary = 8;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
