# `capture_browser_screenshot`

**Cortex step type:** `CortexStepCaptureBrowserScreenshot`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepCaptureBrowserScreenshot {
  string page_id = 1;
  bool save_screenshot = 7;
  string screenshot_name = 10;
  bool capture_by_element_index = 8;
  int32 element_index = 9;
  bool capture_beyond_viewport = 12;
  bool user_rejected = 2;
  exa.codeium_common_pb.ImageData screenshot = 3;
  exa.codeium_common_pb.Media media_screenshot = 11;
  exa.codeium_common_pb.Viewport screenshot_viewport = 13;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 4;
  exa.cortex_pb.AutoRunDecision auto_run_decision = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
