# `search_knowledge_base`

**Cortex step type:** `CortexStepSearchKnowledgeBase`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

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

From `jsonschema_description:` tags in the binary, matched by field name.
