# `mquery`

**Cortex step type:** `CortexStepMquery`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepMquery {
  exa.cortex_pb.PlanInput input = 1;
  repeated exa.context_module_pb.CciWithSubrangeWithRetrievalMetadata ccis = 2;
  uint32 num_tokens_processed = 3;
  uint32 num_items_scored = 4;
  exa.cortex_pb.SemanticCodebaseSearchType search_type = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
