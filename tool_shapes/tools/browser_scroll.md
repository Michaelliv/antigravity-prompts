# `browser_scroll`

**Cortex step type:** `CortexStepBrowserScroll`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (8)

Field names recovered from `(*CortexStepBrowserScroll).Get*` symbols (includes both inputs and outputs).

- `BrowserStateDiff`
- `Direction`
- `ElementIndex`
- `PageId`
- `PixelsScrolledX`
- `PixelsScrolledY`
- `ScrollByElementIndex`
- `ScrollToEnd`


## Parameter descriptions (4)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
page_id of the Browser page to scroll.
```

### 2.
```
page_id of the Browser page to scroll on
```

### 3.
```
if true, scroll in the direction to the end of the selected element/page. For example, if direction is down, would scroll to the bottom of the element/page.
```

### 4.
```
if true, scroll by the element with the given index; the scroll is performed via executing a mouseWheel event on the pixel at the middle of the element.. Otherwise scroll the entire page; in this case, if 0 pixels are scrolled, the page is likely not scrollable and the tool call should be retried by scrolling a DOM element.
```
