# `user_input`

**Cortex step type:** `CortexStepUserInput`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepUserInput {
  repeated exa.codeium_common_pb.TextOrScopeItem items = 3;
  string user_response = 2;
  exa.context_module_pb.ContextModuleResult active_user_state = 4;
  repeated exa.codeium_common_pb.ArtifactComment artifact_comments = 7;
  repeated exa.codeium_common_pb.FileDiffComment file_diff_comments = 10;
  repeated exa.codeium_common_pb.FileComment file_comments = 11;
  bool is_queued_message = 6;
  exa.chat_client_server_pb.ChatClientRequestStreamClientType client_type = 8;
  exa.cortex_pb.CascadeConfig user_config = 12;
  exa.cortex_pb.CascadeConfig last_user_config = 13;
  string query = 1;
  repeated exa.codeium_common_pb.ImageData images = 5;
  repeated exa.codeium_common_pb.Media media = 9;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
