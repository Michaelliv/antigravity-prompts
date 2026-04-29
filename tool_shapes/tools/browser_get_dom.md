# `browser_get_dom`

**Cortex step type:** `CortexStepBrowserGetDom`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (5)

Field names recovered from `(*CortexStepBrowserGetDom).Get*` symbols (includes both inputs and outputs).

- `DomTree`
- `PageId`
- `PageMetadata`
- `SerializedDomTree`
- `SerializedDomTreeUri`


## Parameter descriptions (4)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Index of the annotated DOM element to click on.
```

### 2.
```
page_id of the Browser page to get the DOM tree of
```

### 3.
```
Index of the annotated DOM element to input text into.
```

### 4.
```
The index of the element to capture (required if CaptureByElementIndex is true). Get the index using browser_get_dom.
```
