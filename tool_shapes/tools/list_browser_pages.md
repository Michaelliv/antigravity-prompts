# `list_browser_pages`

**Cortex step type:** `CortexStepListBrowserPages`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (1)

```proto
message CortexStepListBrowserPages {
  repeated exa.codeium_common_pb.BrowserPageMetadata pages = 1;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `pages`
```
An existing page ID which will be replaced with this new URL. You should provide a page_id in almost all cases. To open a new page, set this field to 'new_page'. IMPORTANT: Opening a new page should be extremely rare and only done if you are explicitly instructed to keep multiple pages open simultaneously. By default, always replace the most recently used page or any page not critical to your current task.
```
