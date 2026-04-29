# `search_web`

**Cortex step type:** `CortexStepSearchWeb`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepSearchWeb {
  string query = 1;
  string domain = 3;
  repeated exa.codeium_common_pb.KnowledgeBaseItem web_documents = 2;
  string web_search_url = 4;
  string summary = 5;
  exa.codeium_common_pb.ThirdPartyWebSearchConfig third_party_config = 6;
  exa.cortex_pb.SearchWebType search_type = 7;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
