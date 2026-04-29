# `capture_browser_screenshot`

**Cortex step type:** `CortexStepCaptureBrowserScreenshot`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (12)

Field names recovered from `(*CortexStepCaptureBrowserScreenshot).Get*` symbols (includes both inputs and outputs).

- `AutoRunDecision`
- `CaptureBeyondViewport`
- `CaptureByElementIndex`
- `ElementIndex`
- `MediaScreenshot`
- `PageId`
- `PageMetadata`
- `SaveScreenshot`
- `Screenshot`
- `ScreenshotName`
- `ScreenshotViewport`
- `UserRejected`


## Parameter descriptions (5)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
If true, saves the screenshot as an artifact.
```

### 2.
```
page_id of the Browser page to capture a screenshot of.
```

### 3.
```
If true, captures a screenshot of a specific element by index instead of the full viewport.
```

### 4.
```
Name of the screenshot to save. Should be all lowercase with underscores, describing what the screenshot contains. Maximum 3 words. Example: 'login_page_error'
```

### 5.
```
If true, captures an extended screenshot starting from the current scroll position downward, up to 4000px or the end of page content, whichever is less. To capture content above or below this range, scroll first and then capture.
```
