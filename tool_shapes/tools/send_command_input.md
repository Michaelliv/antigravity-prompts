# `send_command_input`

**Cortex step type:** `CortexStepSendCommandInput`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepSendCommandInput {
  string command_id = 1;
  string input = 2;
  bool should_auto_run = 3;
  bool terminate = 6;
  int64 wait_ms = 7;
  bool user_rejected = 4;
  exa.cortex_pb.AutoRunDecision auto_run_decision = 5;
  exa.cortex_pb.RunCommandOutput output = 8;
  bool running = 9;
  int32 exit_code = 10;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
