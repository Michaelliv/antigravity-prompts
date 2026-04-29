# `browser_resize_window`

**Cortex step type:** `CortexStepBrowserResizeWindow`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (7)

Field names recovered from `(*CortexStepBrowserResizeWindow).Get*` symbols (includes both inputs and outputs).

- `BrowserStateDiff`
- `Height`
- `PageId`
- `PageMetadata`
- `UserRejected`
- `Width`
- `WindowState`


## Parameter descriptions (4)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
page_id of the Browser page to resize.
```

### 2.
```
The window contents width in display independent pixels. Only used when WindowState is 'normal'.
```

### 3.
```
The window contents height in display independent pixels. Only used when WindowState is 'normal'.
```

### 4.
```
The window state to set. Options: 'normal' (resizable window with specified width/height), 'minimized' (window minimized to taskbar), 'maximized' (window is full screen but shows taskbar), 'fullscreen' (window fills entire screen and hides taskbar). Width and Height are only used when WindowState is 'normal'. Generally you should prefer 'maximized'. If the user asks to make the window smaller or a particular size, use 'normal'. When resetting the window size, prefer 'maximized' instead of 'normal' with specific width/height values. 'minimized' and 'fullscreen' are somewhat jarring, so you should only use these when the user explicitly asks for it.
```
