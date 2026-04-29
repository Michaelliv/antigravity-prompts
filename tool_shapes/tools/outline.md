# `outline`

**Cortex step type:** `CortexStepOutline`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepOutline {
  uint32 step_number = 1;
  string action_name = 2;
  string json_args = 3;
  repeated uint32 parent_step_numbers = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
