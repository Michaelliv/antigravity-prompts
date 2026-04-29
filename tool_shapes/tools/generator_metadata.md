# `generator_metadata`

**Cortex step type:** `CortexStepGeneratorMetadata`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepGeneratorMetadata {
  repeated uint32 step_indices = 2;
  exa.cortex_pb.ChatModelMetadata chat_model = 1;
  exa.cortex_pb.InjectedResponseMetadata injected = 7;
  exa.cortex_pb.CascadePlannerConfig planner_config = 3;
  string execution_id = 4;
  string error = 5;
  repeated int32 mendel_experiment_ids = 8;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `error`
```
If true, multiple occurrences of 'targetContent' will be replaced by 'replacementContent' if they are found. Otherwise if multiple occurences are found, an error will be returned.
```
```
The exact string to be replaced. This must be the exact character-sequence to be replaced, including whitespace. Be very careful to include any leading whitespace otherwise this will not work at all. This must be a unique substring within the file, or else it will error.
```
