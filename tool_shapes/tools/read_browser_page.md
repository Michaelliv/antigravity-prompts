# `read_browser_page`

**Cortex step type:** `CortexStepReadBrowserPage`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepReadBrowserPage {
  string page_id = 1;
  exa.codeium_common_pb.KnowledgeBaseItem web_document = 2;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 3;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
