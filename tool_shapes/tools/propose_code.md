# `propose_code`

**Cortex step type:** `CortexStepProposeCode`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepProposeCode {
  exa.cortex_pb.ActionSpec action_spec = 1;
  exa.cortex_pb.ActionResult action_result = 2;
  string code_instruction = 3;
  string markdown_language = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
