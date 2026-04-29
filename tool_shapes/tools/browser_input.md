# `browser_input`

**Cortex step type:** `CortexStepBrowserInput`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepBrowserInput {
  string page_id = 1;
  int32 index = 2;
  string text = 3;
  bool press_enter = 4;
  bool clear_text = 5;
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

### `text`
```
The text to input into the element.
```
```
The text prompt to generate an image for.
```
```
Whether to clear existing text before inputting. Default is false.
```
