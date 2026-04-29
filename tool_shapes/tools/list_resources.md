# `list_resources`

**Cortex step type:** `CortexStepListResources`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepListResources {
  string server_name = 1;
  string cursor = 2;
  repeated exa.cortex_pb.McpResource resources = 3;
  string next_cursor = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `cursor`
```
x-coordinate of the pixel to move the mouse cursor to.
```
```
y-coordinate of the pixel to move the mouse cursor to.
```
```
page_id of the Browser page to move the mouse cursor to.
```

### `resources`
```
Name of the server to list available resources from.
```
