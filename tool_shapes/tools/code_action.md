# `code_action`

**Cortex step type:** `CortexStepCodeAction`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (22)

```proto
message CortexStepCodeAction {
  exa.cortex_pb.ActionSpec action_spec = 1;
  exa.cortex_pb.ActionResult action_result = 2;
  bool use_fast_apply = 4;
  exa.cortex_pb.AcknowledgementType acknowledgement_type = 5;
  exa.cortex_pb.CodeHeuristicFailure heuristic_failure = 7;
  string code_instruction = 8;
  repeated exa.codeium_common_pb.CodeDiagnostic lint_errors = 11;
  repeated exa.codeium_common_pb.CodeDiagnostic persistent_lint_errors = 12;
  repeated exa.cortex_pb.ReplacementChunkInfo replacement_infos = 13;
  repeated string lint_error_ids_aiming_to_fix = 14;
  exa.cortex_pb.FastApplyFallbackInfo fast_apply_fallback_info = 15;
  bool target_file_has_carriage_returns = 16;
  bool target_file_has_all_carriage_returns = 17;
  repeated exa.cortex_pb.CortexStepCompileDiagnostic introduced_errors = 18;
  string triggered_memories = 19;
  bool is_artifact_file = 21;
  int32 artifact_version = 22;
  exa.codeium_common_pb.ArtifactMetadata artifact_metadata = 23;
  bool is_knowledge_file = 24;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 25;
  string description = 26;
  string markdown_validation_error = 27;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `description`
```
A description of the changes that you are making to the file.
```
```
Human-readable description of the JavaScript to execute
```
```
Human-readable description of what this subagent does and when it should be used.
```
