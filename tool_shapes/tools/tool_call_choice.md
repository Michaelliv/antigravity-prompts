# `tool_call_choice`

**Cortex step type:** `CortexStepToolCallChoice`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepToolCallChoice {
  repeated exa.codeium_common_pb.ChatToolCall proposal_tool_calls = 1;
  uint32 choice = 2;
  string reason = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
