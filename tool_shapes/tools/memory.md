# `memory`

**Cortex step type:** `CortexStepMemory`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepMemory {
  string memory_id = 1;
  exa.cortex_pb.CortexMemory memory = 2;
  exa.cortex_pb.CortexMemory prev_memory = 4;
  exa.cortex_pb.MemoryActionType action = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `memory`
```
Number of characters to view. Make this as small as possible to avoid excessive memory usage.
```

### `action`
```
The input to send to the task. Required when Action is 'send_input'.
```
```
The ID of the message to read. Required when Action is 'read'.
```
```
The type of cell: 'code', 'markdown', or 'raw'. Required for 'add' action.
```
