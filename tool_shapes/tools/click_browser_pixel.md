# `click_browser_pixel`

**Cortex step type:** `CortexStepClickBrowserPixel`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (8)

Field names recovered from `(*CortexStepClickBrowserPixel).Get*` symbols (includes both inputs and outputs).

- `BrowserStateDiff`
- `ClickType`
- `PageId`
- `PageMetadata`
- `ScreenshotWithClickFeedback`
- `UserRejected`
- `X`
- `Y`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Y coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 2.
```
X coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 3.
```
Type of click to perform: 'left', 'right', or 'double'. If not specified or left empty, a left click will be performed.
```
