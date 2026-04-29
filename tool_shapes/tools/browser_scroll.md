# `browser_scroll`

**Cortex step type:** `CortexStepBrowserScroll`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepBrowserScroll {
  string page_id = 1;
  exa.browser_pb.ScrollDirection direction = 2;
  bool scroll_to_end = 3;
  bool scroll_by_element_index = 4;
  int32 element_index = 5;
  int32 pixels_scrolled_x = 6;
  int32 pixels_scrolled_y = 7;
  string browser_state_diff = 8;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
