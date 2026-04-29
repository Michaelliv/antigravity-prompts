# `generator_metadata`

**Cortex step type:** `CortexStepGeneratorMetadata`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
