# `view_content_chunk`

**Cortex step type:** `CortexStepViewContentChunk`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepViewContentChunk {
  string document_id = 5;
  int32 position = 2;
  exa.codeium_common_pb.KnowledgeBaseItem cropped_item = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `position`
```
If true, captures an extended screenshot starting from the current scroll position downward, up to 4000px or the end of page content, whichever is less. To capture content above or below this range, scroll first and then capture.
```
