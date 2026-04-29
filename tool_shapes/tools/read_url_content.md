# `read_url_content`

**Cortex step type:** `CortexStepReadUrlContent`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (6)

```proto
message CortexStepReadUrlContent {
  string url = 1;
  exa.codeium_common_pb.KnowledgeBaseItem web_document = 2;
  string resolved_url = 3;
  uint32 latency_ms = 4;
  bool user_rejected = 5;
  string content_path = 6;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `url`
```
URL to read content from
```
```
The URL to open in the user's browser.
```
```
Type of reference (e.g., file, conversation_id, url)
```
