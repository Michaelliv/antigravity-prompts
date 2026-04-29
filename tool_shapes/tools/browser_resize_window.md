# `browser_resize_window`

**Cortex step type:** `CortexStepBrowserResizeWindow`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepBrowserResizeWindow {
  string page_id = 1;
  int32 width = 2;
  int32 height = 3;
  exa.browser_pb.WindowState window_state = 6;
  bool user_rejected = 4;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 5;
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

### `width`
```
The window contents width in display independent pixels. Only used when WindowState is 'normal'.
```
```
The window state to set. Options: 'normal' (resizable window with specified width/height), 'minimized' (window minimized to taskbar), 'maximized' (window is full screen but shows taskbar), 'fullscreen' (window fills entire screen and hides taskbar). Width and Height are only used when WindowState is 'normal'. Generally you should prefer 'maximized'. If the user asks to make the window smaller or a particular size, use 'normal'. When resetting the window size, prefer 'maximized' instead of 'normal' with specific width/height values. 'minimized' and 'fullscreen' are somewhat jarring, so you should only use these when the user explicitly asks for it.
```

### `height`
```
The window contents height in display independent pixels. Only used when WindowState is 'normal'.
```
```
The window state to set. Options: 'normal' (resizable window with specified width/height), 'minimized' (window minimized to taskbar), 'maximized' (window is full screen but shows taskbar), 'fullscreen' (window fills entire screen and hides taskbar). Width and Height are only used when WindowState is 'normal'. Generally you should prefer 'maximized'. If the user asks to make the window smaller or a particular size, use 'normal'. When resetting the window size, prefer 'maximized' instead of 'normal' with specific width/height values. 'minimized' and 'fullscreen' are somewhat jarring, so you should only use these when the user explicitly asks for it.
```
