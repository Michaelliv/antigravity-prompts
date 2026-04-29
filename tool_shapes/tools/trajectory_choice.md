# `trajectory_choice`

**Cortex step type:** `CortexStepTrajectoryChoice`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepTrajectoryChoice {
  repeated string proposal_trajectory_ids = 1;
  int32 choice = 2;
  string reason = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
