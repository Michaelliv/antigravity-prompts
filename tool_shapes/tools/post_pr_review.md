# `post_pr_review`

**Cortex step type:** `CortexStepPostPrReview`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepPostPrReview {
  string body = 1;
  string commit_id = 2;
  string path = 3;
  string side = 4;
  int32 start_line = 5;
  int32 end_line = 6;
  string category = 7;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
