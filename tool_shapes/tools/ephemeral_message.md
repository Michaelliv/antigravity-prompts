# `ephemeral_message`

**Cortex step type:** `CortexStepEphemeralMessage`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepEphemeralMessage {
  string content = 1;
  repeated exa.codeium_common_pb.Media media = 2;
  repeated string triggered_heuristics = 3;
  repeated exa.codeium_common_pb.Media attachments = 4;
  string dom_tree_uri = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `content`
```
The message content.
```
```
URL to read content from
```
```
Content of the prompt section.
```

### `media`
```
Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.
```
```
The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'.
```
