# `browser_mouse_up`

**Cortex step type:** `CortexStepBrowserMouseUp`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepBrowserMouseUp {
  string page_id = 1;
  string button = 2;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 3;
  string browser_state_diff = 4;
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

### `button`
```
page_id of the Browser page to press the mouse button on
```
```
page_id of the Browser page to release the mouse button on
```
```
Mouse button to press. Options are 'left', 'right', or 'middle'.
```
