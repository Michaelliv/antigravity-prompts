# `browser_scroll_down`

**Cortex step type:** `CortexStepBrowserScrollDown`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepBrowserScrollDown {
  string page_id = 1;
  bool scroll_to_end = 2;
  bool scroll_by_element_index = 3;
  int32 element_index = 4;
  string browser_state_diff = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
