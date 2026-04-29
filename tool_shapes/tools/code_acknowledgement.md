# `code_acknowledgement`

**Cortex step type:** `CortexStepCodeAcknowledgement`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCodeAcknowledgement {
  bool is_accept = 3;
  string written_feedback = 4;
  exa.cortex_pb.CodeAcknowledgementScope acknowledgement_scope = 5;
  repeated exa.cortex_pb.CodeAcknowledgementInfo code_acknowledgement_infos = 7;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
