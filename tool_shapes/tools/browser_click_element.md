# `browser_click_element`

**Cortex step type:** `CortexStepBrowserClickElement`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepBrowserClickElement {
  string page_id = 1;
  int32 index = 2;
  string description = 3;
  exa.browser_pb.ClickType click_type = 5;
  bool user_rejected = 4;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 6;
  string browser_state_diff = 7;
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

### `index`
```
index of the element to scroll on
```
```
Index of the annotated DOM element to click on.
```
```
Index of the annotated DOM element to input text into.
```

### `description`
```
A description of the changes that you are making to the file.
```
```
Human-readable description of the JavaScript to execute
```
```
Human-readable description of what this subagent does and when it should be used.
```
