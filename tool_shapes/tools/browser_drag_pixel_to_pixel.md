# `browser_drag_pixel_to_pixel`

**Cortex step type:** `CortexStepBrowserDragPixelToPixel`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepBrowserDragPixelToPixel {
  string page_id = 1;
  repeated exa.codeium_common_pb.Point2 waypoints = 2;
  bool user_rejected = 6;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 7;
  repeated exa.codeium_common_pb.Media screenshots_with_drag_feedback = 8;
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
