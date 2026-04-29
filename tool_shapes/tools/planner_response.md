# `planner_response`

**Cortex step type:** `CortexStepPlannerResponse`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepPlannerResponse {
  string response = 1;
  string modified_response = 8;
  string thinking = 3;
  string raw_thinking = 16;
  string signature = 4;
  bytes thinking_signature = 14;
  bool thinking_redacted = 5;
  string message_id = 6;
  string provider_assigned_message_id = 15;
  repeated exa.codeium_common_pb.ChatToolCall tool_calls = 7;
  repeated exa.codeium_common_pb.KnowledgeBaseItemWithMetadata knowledge_base_items = 2;
  google.protobuf.Duration thinking_duration = 11;
  exa.codeium_common_pb.StopReason stop_reason = 12;
  exa.codeium_common_pb.RecitationMetadata recitation_metadata = 13;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
