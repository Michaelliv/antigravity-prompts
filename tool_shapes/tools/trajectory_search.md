# `trajectory_search`

**Cortex step type:** `CortexStepTrajectorySearch`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepTrajectorySearch {
  string id = 1;
  string query = 2;
  exa.cortex_pb.TrajectorySearchIdType id_type = 3;
  repeated exa.context_module_pb.CciWithSubrangeWithRetrievalMetadata chunks = 4;
  exa.cortex_pb.TrajectoryDescription trajectory_description = 5;
  uint32 total_chunks = 6;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
