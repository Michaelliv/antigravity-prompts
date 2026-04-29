# `mcp_tool`

**Cortex step type:** `CortexStepMcpTool`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (13)

```proto
message CortexStepMcpTool {
  string server_name = 1;
  exa.codeium_common_pb.ChatToolCall tool_call = 2;
  exa.cortex_pb.McpServerInfo server_info = 4;
  string result_string = 3;
  string result_uri = 8;
  repeated exa.codeium_common_pb.ImageData images = 5;
  repeated exa.codeium_common_pb.Media media = 6;
  bool user_rejected = 7;
  exa.cortex_pb.StepRenderInfo render_info = 9;
  string progress_message = 10;
  double progress = 11;
  double progress_total = 12;
  repeated exa.cortex_pb.CortexStepMcpTool.MetadataEntry metadata = 13;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `images`
```
Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.
```
```
Optional absolute paths to the images to use in generation. You can pass in images here if you would like to edit or combine images. You can pass in artifact images and any images in the file system. Note: you cannot pass in more than 3 images.
```

### `media`
```
Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.
```
```
The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'.
```

### `metadata`
```
Metadata for the artifact, required when IsArtifact is true.
```
```
Metadata updates if updating an artifact file, leave blank if not updating an artifact. Should be updated if the content is changing meaningfully.
```
```
The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message).
```
