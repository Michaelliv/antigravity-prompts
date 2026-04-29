# `lookup_knowledge_base`

**Cortex step type:** `CortexStepLookupKnowledgeBase`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepLookupKnowledgeBase {
  repeated string urls = 1;
  repeated string document_ids = 2;
  repeated exa.codeium_common_pb.KnowledgeBaseItemWithMetadata knowledge_base_items = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `urls`
```
Name of the task that the browser subagent is performing. This is the identifier that groups the subagent steps together, but should still be a human readable name. This should read like a title, should be properly capitalized and human readable, example: 'Navigating to Example Page'. Replace URLs or non-human-readable expressions like CSS selectors or long text with human-readable terms like 'URL' or 'Page' or 'Submit Button'. Be very sure this task name represents a reasonable chunk of work. It should almost never be the entire user request. This should be the very first argument.
```
