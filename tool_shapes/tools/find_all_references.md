# `find_all_references`

**Cortex step type:** `CortexStepFindAllReferences`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepFindAllReferences {
  string absolute_uri = 1;
  string symbol = 2;
  uint32 line = 3;
  uint32 occurrence_index = 4;
  repeated exa.codeium_common_pb.LspReference references = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
