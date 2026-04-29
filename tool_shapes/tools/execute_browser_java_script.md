# `execute_browser_java_script`

**Cortex step type:** `CortexStepExecuteBrowserJavaScript`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepExecuteBrowserJavaScript {
  string title = 9;
  string page_id = 1;
  string javascript_source = 2;
  string javascript_description = 3;
  bool should_auto_run = 10;
  exa.cortex_pb.BrowserActionWaitingReason waiting_reason = 13;
  bool user_rejected = 4;
  exa.codeium_common_pb.ImageData screenshot_end = 5;
  exa.codeium_common_pb.Media media_screenshot_end = 12;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 6;
  uint64 execution_duration_ms = 7;
  string javascript_result = 8;
  string browser_state_diff = 11;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
