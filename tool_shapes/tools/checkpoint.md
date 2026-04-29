# `checkpoint`

**Cortex step type:** `CortexStepCheckpoint`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (19)

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
  repeated exa.cortex_pb.CortexStepCheckpoint.EditedFileMapEntry edited_file_map = 7;
  repeated uint32 included_step_indices = 3;
  string memory_summary = 8;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
