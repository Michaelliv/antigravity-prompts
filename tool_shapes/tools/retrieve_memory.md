# `retrieve_memory`

**Cortex step type:** `CortexStepRetrieveMemory`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
