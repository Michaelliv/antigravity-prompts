# `command_status`

**Cortex step type:** `CortexStepCommandStatus`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCommandStatus {
  string command_id = 1;
  uint32 output_character_count = 8;
  uint32 wait_duration_seconds = 10;
  exa.cortex_pb.CortexStepStatus status = 2;
  string combined = 9;
  string delta = 12;
  int32 exit_code = 5;
  exa.cortex_pb.CortexErrorDetails error = 6;
  uint32 waited_duration_seconds = 11;
  string stdout = 3;
  string stderr = 4;
  exa.cortex_pb.CommandOutputPriority output_priority = 7;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
