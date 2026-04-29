# `open_browser_url`

**Cortex step type:** `CortexStepOpenBrowserUrl`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (10)

Field names recovered from `(*CortexStepOpenBrowserUrl).Get*` symbols (includes both inputs and outputs).

- `AutoRunDecision`
- `BrowserStateDiff`
- `MediaScreenshot`
- `PageId`
- `PageIdToReplace`
- `PageMetadata`
- `Screenshot`
- `Url`
- `UserRejected`
- `WebDocument`


## Parameter descriptions (2)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The URL to open in the user's browser.
```

### 2.
```
An existing page ID which will be replaced with this new URL. You should provide a page_id in almost all cases. To open a new page, set this field to 'new_page'. IMPORTANT: Opening a new page should be extremely rare and only done if you are explicitly instructed to keep multiple pages open simultaneously. By default, always replace the most recently used page or any page not critical to your current task.
```
