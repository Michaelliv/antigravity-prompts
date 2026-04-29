# `compile`

**Cortex step type:** `CortexStepCompile`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCompile {
  exa.cortex_pb.CortexStepCompileTool tool = 1;
  string input_spec = 2;
  string target = 4;
  string artifact_path = 5;
  bool artifact_is_executable = 6;
  repeated exa.cortex_pb.CortexStepCompileDiagnostic errors = 7;
  repeated exa.cortex_pb.CortexStepCompileDiagnostic warnings = 8;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
