# `brain_update`

**Cortex step type:** `CortexStepBrainUpdate`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepBrainUpdate {
  exa.cortex_pb.BrainEntryType entry_type = 1;
  exa.cortex_pb.BrainUpdateTrigger trigger = 3;
  repeated exa.cortex_pb.BrainEntryDelta deltas = 2;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
