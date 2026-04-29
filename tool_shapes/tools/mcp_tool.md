# `mcp_tool`

**Cortex step type:** `CortexStepMcpTool`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepMcpTool {
  string server_name = 1;
  exa.codeium_common_pb.ChatToolCall tool_call = 2;
  exa.cortex_pb.McpServerInfo server_info = 4;
  string result_string = 3;
  string result_uri = 8;
  repeated exa.codeium_common_pb.ImageData images = 5;
  repeated exa.codeium_common_pb.Media media = 6;
  bool user_rejected = 7;
  exa.cortex_pb.StepRenderInfo render_info = 9;
  string progress_message = 10;
  double progress = 11;
  double progress_total = 12;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
