# `run_command`

**Cortex step type:** `CortexStepRunCommand`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepRunCommand {
  string command_line = 23;
  string proposed_command_line = 25;
  string cwd = 2;
  uint64 wait_ms_before_async = 12;
  bool should_auto_run = 15;
  string requested_terminal_id = 17;
  bool sandbox_override = 27;
  bool run_persistent = 28;
  bool blocking = 11;
  string command_id = 13;
  int32 exit_code = 6;
  bool user_rejected = 14;
  exa.cortex_pb.AutoRunDecision auto_run_decision = 16;
  string terminal_id = 18;
  exa.cortex_pb.RunCommandOutput combined_output = 21;
  exa.cortex_pb.RunCommandOutput combined_output_snapshot = 26;
  bool used_ide_terminal = 22;
  string raw_debug_output = 24;
  string command = 1;
  repeated string args = 3;
  string stdout = 4;
  string stderr = 5;
  string stdout_buffer = 7;
  string stderr_buffer = 8;
  uint32 stdout_lines_above = 9;
  uint32 stderr_lines_above = 10;
  exa.cortex_pb.RunCommandOutput stdout_output = 19;
  exa.cortex_pb.RunCommandOutput stderr_output = 20;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
