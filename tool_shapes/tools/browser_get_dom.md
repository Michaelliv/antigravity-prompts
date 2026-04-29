# `browser_get_dom`

**Cortex step type:** `CortexStepBrowserGetDom`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepBrowserGetDom {
  string page_id = 1;
  exa.codeium_common_pb.DOMTree dom_tree = 2;
  string serialized_dom_tree = 3;
  string serialized_dom_tree_uri = 5;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 4;
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
