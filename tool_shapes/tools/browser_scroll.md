# `browser_scroll`

**Cortex step type:** `CortexStepBrowserScroll`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (8)

```proto
message CortexStepBrowserScroll {
  string page_id = 1;
  exa.browser_pb.ScrollDirection direction = 2;
  bool scroll_to_end = 3;
  bool scroll_by_element_index = 4;
  int32 element_index = 5;
  int32 pixels_scrolled_x = 6;
  int32 pixels_scrolled_y = 7;
  string browser_state_diff = 8;
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

### `direction`
```
direction of the scroll. Options are left, right, up, down
```
```
if true, scroll in the direction to the end of the selected element/page. For example, if direction is down, would scroll to the bottom of the element/page.
```
