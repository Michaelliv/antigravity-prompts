# `proposal_feedback`

**Cortex step type:** `CortexStepProposalFeedback`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepProposalFeedback {
  exa.cortex_pb.AcknowledgementType acknowledgement_type = 1;
  uint32 target_step_index = 2;
  exa.cortex_pb.ReplacementChunk replacement_chunk = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
