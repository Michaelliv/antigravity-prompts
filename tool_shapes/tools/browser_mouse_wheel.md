# `browser_mouse_wheel`

**Cortex step type:** `CortexStepBrowserMouseWheel`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepBrowserMouseWheel {
  string page_id = 1;
  int32 x = 2;
  int32 y = 3;
  int32 dx = 4;
  int32 dy = 5;
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

### `x`
```
x-coordinate of the pixel to move the mouse cursor to.
```
```
X coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions.
```
```
X coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### `y`
```
y-coordinate of the pixel to move the mouse cursor to.
```
```
Y coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions.
```
```
Y coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```
