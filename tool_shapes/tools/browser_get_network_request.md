# `browser_get_network_request`

**Cortex step type:** `CortexStepBrowserGetNetworkRequest`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepBrowserGetNetworkRequest {
  string page_id = 1;
  string request_id = 2;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 3;
  string network_request_details = 4;
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
