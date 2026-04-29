# `browser_list_network_requests`

**Cortex step type:** `CortexStepBrowserListNetworkRequests`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepBrowserListNetworkRequests {
  string page_id = 1;
  bool include_preserved_requests = 2;
  repeated string resource_types = 3;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 4;
  string network_requests = 5;
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
