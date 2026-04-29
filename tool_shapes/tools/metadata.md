# `metadata`

**Cortex step type:** `CortexStepMetadata`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepMetadata {
  uint32 step_generation_version = 21;
  google.protobuf.Timestamp created_at = 1;
  google.protobuf.Timestamp viewable_at = 6;
  google.protobuf.Timestamp finished_generating_at = 7;
  google.protobuf.Timestamp last_completed_chunk_at = 22;
  google.protobuf.Timestamp started_at = 32;
  google.protobuf.Timestamp completed_at = 8;
  exa.cortex_pb.CortexStepSource source = 3;
  exa.codeium_common_pb.ChatToolCall tool_call = 4;
  exa.codeium_common_pb.ChatToolCall modified_tool_call = 29;
  repeated string arguments_order = 5;
  exa.codeium_common_pb.ModelUsageStats model_usage = 9;
  repeated exa.cortex_pb.RetryInfo retry_infos = 28;
  float model_cost = 10;
  exa.codeium_common_pb.Model generator_model = 11;
  exa.codeium_common_pb.ModelOrAlias requested_model = 13;
  exa.codeium_common_pb.ModelInfo model_info = 24;
  string execution_id = 12;
  int32 flow_credits_used = 14;
  int32 prompt_credits_used = 15;
  repeated exa.cortex_pb.CortexStepCreditReason non_standard_credit_reasons = 18;
  repeated exa.codeium_common_pb.ChatToolCall tool_call_choices = 16;
  string tool_call_choice_reason = 17;
  exa.cortex_pb.CortexRequestSource cortex_request_source = 19;
  int32 tool_call_output_tokens = 23;
  exa.cortex_pb.SourceTrajectoryStepInfo source_trajectory_step_info = 20;
  exa.cortex_pb.SnapshotMetadata snapshot_metadata = 25;
  exa.cortex_pb.CortexStepInternalMetadata internal_metadata = 26;
  bool wait_for_previous_tools = 27;
  string tool_summary = 30;
  string tool_action = 31;
  bool is_interrupting_step = 33;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
