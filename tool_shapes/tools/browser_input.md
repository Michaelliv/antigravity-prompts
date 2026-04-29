# `browser_input`

**Cortex step type:** `CortexStepBrowserInput`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (7)

Field names recovered from `(*CortexStepBrowserInput).Get*` symbols (includes both inputs and outputs).

- `BrowserStateDiff`
- `ClearText`
- `Index`
- `PageId`
- `PageMetadata`
- `PressEnter`
- `Text`


## Parameter descriptions (5)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Whether to clear existing text before inputting. Default is false.
```

### 2.
```
Whether to press Enter after inputting the text. Default is false.
```

### 3.
```
page_id of the Browser page to simulate a key press on
```

### 4.
```
Text to type sequentially, character by character. Use this for typing regular text content like letters, numbers, and basic symbols. Each character will be typed individually in sequence. Only specify one of Key or Text - use Text for typing regular content, not for keyboard shortcuts or special keys like F1, Control+C, etc.
```

### 5.
```
Name of the key/key combination to simulate. Examples of keys are: "F1" - "F12", "Digit0"- "Digit9", "KeyA"- "KeyZ", "Backquote", "Minus", "Equal", "Backslash", "Backspace", "Tab", "Delete", "Escape", "ArrowDown", "End", "Enter", "Home", "Insert", "PageDown", "PageUp", "ArrowRight", "ArrowUp", etc. This tool also supports combinations with modifiers (e.g., Control+Enter). Examples of modifiers are: "Shift", "Control", "Alt", "Meta", "ShiftLeft", "ControlOrMeta". "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. Only specify one of Key or Text - use Key for keyboard shortcuts and special keys.
```
