# `agency_tool_call`

**Cortex step type:** `CortexStepAgencyToolCall`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepAgencyToolCall {
  string agent_name = 1;
  string function_name = 2;
  repeated google.protobuf.Any request_messages = 3;
  repeated google.protobuf.Any response_messages = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
