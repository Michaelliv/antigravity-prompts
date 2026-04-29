# `memory`

**Cortex step type:** `CortexStepMemory`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepMemory {
  string memory_id = 1;
  exa.cortex_pb.CortexMemory memory = 2;
  exa.cortex_pb.CortexMemory prev_memory = 4;
  exa.cortex_pb.MemoryActionType action = 3;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
