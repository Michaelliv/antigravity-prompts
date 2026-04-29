# `task_boundary`

**Cortex step type:** `CortexStepTaskBoundary`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepTaskBoundary {
  string task_name = 1;
  string task_status = 2;
  string task_summary = 3;
  string task_summary_with_citations = 4;
  string delta_summary = 6;
  string delta_summary_with_citations = 7;
  exa.cortex_pb.AgentMode mode = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
