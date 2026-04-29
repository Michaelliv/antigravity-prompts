# `user_input`

**Cortex step type:** `CortexStepUserInput`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (13)

```proto
message CortexStepUserInput {
  repeated exa.codeium_common_pb.TextOrScopeItem items = 3;
  string user_response = 2;
  exa.context_module_pb.ContextModuleResult active_user_state = 4;
  repeated exa.codeium_common_pb.ArtifactComment artifact_comments = 7;
  repeated exa.codeium_common_pb.FileDiffComment file_diff_comments = 10;
  repeated exa.codeium_common_pb.FileComment file_comments = 11;
  bool is_queued_message = 6;
  exa.chat_client_server_pb.ChatClientRequestStreamClientType client_type = 8;
  exa.cortex_pb.CascadeConfig user_config = 12;
  exa.cortex_pb.CascadeConfig last_user_config = 13;
  string query = 1;
  repeated exa.codeium_common_pb.ImageData images = 5;
  repeated exa.codeium_common_pb.Media media = 9;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `query`
```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```
```
If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality.
```

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
