# `read_browser_page`

**Cortex step type:** `CortexStepReadBrowserPage`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepReadBrowserPage {
  string page_id = 1;
  exa.codeium_common_pb.KnowledgeBaseItem web_document = 2;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 3;
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
