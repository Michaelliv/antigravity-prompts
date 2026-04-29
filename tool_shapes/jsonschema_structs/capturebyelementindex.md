# `ToJsonSchemaString` struct @ 0x3036188

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- **embedded** `google3/third_party/jetski/cortex/tools/browser/browser.captureBrowserScreenshotToolArgsNoDOM`

- `CaptureByElementIndex` _bool_
  - `jsonschema_description` = `If true, captures a screenshot of a specific element by index instead of the full viewport.`

- `ElementIndex` _int32_
  - `jsonschema_description` = `The index of the element to capture (required if CaptureByElementIndex is true). Get the index using browser_get_dom.`

## Raw body

```
 google3/third_party/jetski/cortex/tools/browser/browser.captureBrowserScreenshotToolArgsNoDOM; CaptureByElementIndex bool "jsonschema_description:\"If true, captures a screenshot of a specific element by index instead of the full viewport.\""; ElementIndex int32 "jsonschema_description:\"The index of the element to capture (required if CaptureByElementIndex is true). Get the index using browser_get_dom.\"" 
```
