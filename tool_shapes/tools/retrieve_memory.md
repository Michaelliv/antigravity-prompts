# `retrieve_memory`

**Cortex step type:** `CortexStepRetrieveMemory`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (8)

```proto
message CortexStepRetrieveMemory {
  bool run_subagent = 1;
  bool add_user_memories = 8;
  string cascade_memory_summary = 2;
  string user_memory_summary = 3;
  string reason = 4;
  bool show_reason = 5;
  repeated exa.cortex_pb.CortexMemory retrieved_memories = 6;
  bool blocking = 7;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
