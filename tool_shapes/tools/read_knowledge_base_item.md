# `read_knowledge_base_item`

**Cortex step type:** `CortexStepReadKnowledgeBaseItem`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepReadKnowledgeBaseItem {
  string identifier = 1;
  exa.codeium_common_pb.KnowledgeBaseItem knowledge_base_item = 2;
  exa.opensearch_clients_pb.ConnectorType connector_type = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `identifier`
```
Unique identifier for the resource.
```
```
Name of the task that the browser subagent is performing. This is the identifier that groups the subagent steps together, but should still be a human readable name. This should read like a title, should be properly capitalized and human readable, example: 'Navigating to Example Page'. Replace URLs or non-human-readable expressions like CSS selectors or long text with human-readable terms like 'URL' or 'Page' or 'Submit Button'. Be very sure this task name represents a reasonable chunk of work. It should almost never be the entire user request. This should be the very first argument.
```
