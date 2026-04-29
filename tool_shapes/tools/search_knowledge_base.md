# `search_knowledge_base`

**Cortex step type:** `CortexStepSearchKnowledgeBase`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepSearchKnowledgeBase {
  repeated string queries = 1;
  exa.opensearch_clients_pb.TimeRange time_range = 3;
  repeated exa.opensearch_clients_pb.ConnectorType connector_types = 4;
  repeated string aggregate_ids = 7;
  repeated exa.codeium_common_pb.KnowledgeBaseGroup knowledge_base_groups = 2;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
