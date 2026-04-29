# `mquery`

**Cortex step type:** `CortexStepMquery`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepMquery {
  exa.cortex_pb.PlanInput input = 1;
  repeated exa.context_module_pb.CciWithSubrangeWithRetrievalMetadata ccis = 2;
  uint32 num_tokens_processed = 3;
  uint32 num_items_scored = 4;
  exa.cortex_pb.SemanticCodebaseSearchType search_type = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `input`
```
The text to input into the element.
```
```
The page_id of the browser page to input text on.
```
```
Index of the annotated DOM element to input text into.
```
