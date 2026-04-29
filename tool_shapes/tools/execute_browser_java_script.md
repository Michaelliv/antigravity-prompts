# `execute_browser_java_script`

**Cortex step type:** `CortexStepExecuteBrowserJavaScript`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (13)

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

From `jsonschema_description:` tags in the binary, matched by field name.

### `title`
```
Human-readable title for the Knowledge Item
```
```
Title of the prompt section.
```
```
The question to ask the user. Do NOT add 'select all that apply' or similar text to the question title.
```

### `page_id`
```
page_id of the Browser page to read
```
```
page_id of the Browser page to perform the drag operation on
```
```
page_id of the Browser page to scroll.
```
