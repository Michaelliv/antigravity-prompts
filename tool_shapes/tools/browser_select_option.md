# `browser_select_option`

**Cortex step type:** `CortexStepBrowserSelectOption`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepBrowserSelectOption {
  string page_id = 1;
  int32 index = 2;
  string value = 3;
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

### `value`
```
Value of the reference
```
```
The value or text of the option to select from the dropdown.
```
```
Optional. Startline to view, 1-indexed as usual, inclusive. This value must be less than or equal to EndLine.
```
