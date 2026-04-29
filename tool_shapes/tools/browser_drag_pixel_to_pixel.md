# `browser_drag_pixel_to_pixel`

**Cortex step type:** `CortexStepBrowserDragPixelToPixel`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (5)

Field names recovered from `(*CortexStepBrowserDragPixelToPixel).Get*` symbols (includes both inputs and outputs).

- `PageId`
- `PageMetadata`
- `ScreenshotsWithDragFeedback`
- `UserRejected`
- `Waypoints`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
X coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 2.
```
Y coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 3.
```
A series of pixel coordinates defining the drag path. When this tool call is executed, the first waypoint will be clicked, then the mouse will be dragged to each subsequent waypoint in the provided order, and finally the mouse will be released at the last waypoint.
```
