# `write_to_file`

**Cortex step type:** `CortexStepWriteToFile`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepWriteToFile {
  string target_file_uri = 1;
  repeated string code_content = 2;
  exa.diff_action_pb.DiffBlock diff = 3;
  bool file_created = 4;
  exa.cortex_pb.AcknowledgementType acknowledgement_type = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
