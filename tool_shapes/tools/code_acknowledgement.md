# `code_acknowledgement`

**Cortex step type:** `CortexStepCodeAcknowledgement`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepCodeAcknowledgement {
  bool is_accept = 3;
  string written_feedback = 4;
  exa.cortex_pb.CodeAcknowledgementScope acknowledgement_scope = 5;
  repeated exa.cortex_pb.CodeAcknowledgementInfo code_acknowledgement_infos = 7;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
