# `open_browser_url`

**Cortex step type:** `CortexStepOpenBrowserUrl`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (10)

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

From `jsonschema_description:` tags in the binary, matched by field name.

### `url`
```
URL to read content from
```
```
The URL to open in the user's browser.
```
```
Type of reference (e.g., file, conversation_id, url)
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
