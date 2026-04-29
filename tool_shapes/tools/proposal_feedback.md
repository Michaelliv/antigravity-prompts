# `proposal_feedback`

**Cortex step type:** `CortexStepProposalFeedback`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepProposalFeedback {
  exa.cortex_pb.AcknowledgementType acknowledgement_type = 1;
  uint32 target_step_index = 2;
  exa.cortex_pb.ReplacementChunk replacement_chunk = 3;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
