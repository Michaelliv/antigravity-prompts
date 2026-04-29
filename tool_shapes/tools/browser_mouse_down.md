# `browser_mouse_down`

**Cortex step type:** `CortexStepBrowserMouseDown`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepBrowserMouseDown {
  string page_id = 1;
  string button = 2;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 3;
  string browser_state_diff = 4;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
