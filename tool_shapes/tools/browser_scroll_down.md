# `browser_scroll_down`

**Cortex step type:** `CortexStepBrowserScrollDown`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

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
