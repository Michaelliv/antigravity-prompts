# `click_browser_pixel`

**Cortex step type:** `CortexStepClickBrowserPixel`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepClickBrowserPixel {
  string page_id = 1;
  int32 x = 2;
  int32 y = 3;
  exa.browser_pb.ClickType click_type = 7;
  bool user_rejected = 4;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 5;
  exa.codeium_common_pb.Media screenshot_with_click_feedback = 6;
  string browser_state_diff = 8;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
