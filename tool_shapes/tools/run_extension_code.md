# `run_extension_code`

**Cortex step type:** `CortexStepRunExtensionCode`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepRunExtensionCode {
  string code = 1;
  string language = 2;
  bool model_wants_auto_run = 6;
  string user_facing_explanation = 7;
  string output = 3;
  bool user_rejected = 4;
  exa.cortex_pb.RunExtensionCodeAutoRunDecision auto_run_decision = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
