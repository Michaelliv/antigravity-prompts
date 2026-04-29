# `browser_press_key`

**Cortex step type:** `CortexStepBrowserPressKey`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepBrowserPressKey {
  string page_id = 1;
  string key = 2;
  string text = 3;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 5;
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

### `key`
```
page_id of the Browser page to simulate a key press on
```
```
Text to type sequentially, character by character. Use this for typing regular text content like letters, numbers, and basic symbols. Each character will be typed individually in sequence. Only specify one of Key or Text - use Text for typing regular content, not for keyboard shortcuts or special keys like F1, Control+C, etc.
```
```
Name of the key/key combination to simulate. Examples of keys are: "F1" - "F12", "Digit0"- "Digit9", "KeyA"- "KeyZ", "Backquote", "Minus", "Equal", "Backslash", "Backspace", "Tab", "Delete", "Escape", "ArrowDown", "End", "Enter", "Home", "Insert", "PageDown", "PageUp", "ArrowRight", "ArrowUp", etc. This tool also supports combinations with modifiers (e.g., Control+Enter). Examples of modifiers are: "Shift", "Control", "Alt", "Meta", "ShiftLeft", "ControlOrMeta". "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. Only specify one of Key or Text - use Key for keyboard shortcuts and special keys.
```

### `text`
```
The text to input into the element.
```
```
The text prompt to generate an image for.
```
```
Whether to clear existing text before inputting. Default is false.
```
