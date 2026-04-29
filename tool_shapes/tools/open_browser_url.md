# `open_browser_url`

**Cortex step type:** `CortexStepOpenBrowserUrl`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepOpenBrowserUrl {
  string url = 1;
  string page_id_to_replace = 8;
  exa.cortex_pb.AutoRunDecision auto_run_decision = 2;
  bool user_rejected = 3;
  string page_id = 4;
  exa.codeium_common_pb.KnowledgeBaseItem web_document = 5;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 6;
  exa.codeium_common_pb.ImageData screenshot = 7;
  exa.codeium_common_pb.Media media_screenshot = 10;
  string browser_state_diff = 9;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
