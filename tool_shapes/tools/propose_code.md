# `propose_code`

**Cortex step type:** `CortexStepProposeCode`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepProposeCode {
  exa.cortex_pb.ActionSpec action_spec = 1;
  exa.cortex_pb.ActionResult action_result = 2;
  string code_instruction = 3;
  string markdown_language = 4;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
