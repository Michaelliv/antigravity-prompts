# `browser_click_element`

**Cortex step type:** `CortexStepBrowserClickElement`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (7)

Field names recovered from `(*CortexStepBrowserClickElement).Get*` symbols (includes both inputs and outputs).

- `BrowserStateDiff`
- `ClickType`
- `Description`
- `Index`
- `PageId`
- `PageMetadata`
- `UserRejected`


## Parameter descriptions (2)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The page_id of the browser page to click on.
```

### 2.
```
Element name only (2-4 words, noun phrase). NOT an action sentence. Examples: 'Username Field', 'Submit Button', 'Login Link'. Never include verbs like 'clicking' or phrases like 'to focus'.
```
