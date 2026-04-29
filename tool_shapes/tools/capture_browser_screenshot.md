# `capture_browser_screenshot`

**Cortex step type:** `CortexStepCaptureBrowserScreenshot`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (12)

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

From `jsonschema_description:` tags in the binary, matched by field name.

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

### `screenshot`
```
If true, saves the screenshot as an artifact.
```
```
page_id of the Browser page to capture a screenshot of.
```
```
If true, captures a screenshot of a specific element by index instead of the full viewport.
```
