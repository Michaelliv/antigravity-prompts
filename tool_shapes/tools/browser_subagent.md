# `browser_subagent`

**Cortex step type:** `CortexStepBrowserSubagent`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepBrowserSubagent {
  string task = 1;
  string reused_subagent_id = 9;
  string recording_name = 7;
  repeated exa.codeium_common_pb.Media media = 11;
  string result = 2;
  string task_name = 3;
  string task_summary = 13;
  string recording_path = 4;
  exa.cortex_pb.RecordingGenerationStatus recording_generation_status = 6;
  string subagent_id = 8;
  bool skipped = 10;
  string scratchpad_path = 12;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
