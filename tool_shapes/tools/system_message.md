# `system_message`

**Cortex step type:** `CortexStepSystemMessage`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepSystemMessage {
  string message = 1;
  exa.cortex_pb.StepRenderInfo render_info = 2;
  string event_type = 3;
  exa.cortex_pb.AgentMessage agent_message = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `message`
```
The message content.
```
```
The ID of the message to read. Required when Action is 'read'.
```
```
The recipient ID to send the message to, e.g. a subagent conversation ID.
```
