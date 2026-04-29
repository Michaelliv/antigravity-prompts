# `notify_user`

**Cortex step type:** `CortexStepNotifyUser`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepNotifyUser {
  repeated string review_absolute_uris = 1;
  string notification_content = 2;
  bool is_blocking = 3;
  float confidence_score = 4;
  string confidence_justification = 5;
  bool should_auto_proceed = 8;
  string diffs_uri = 6;
  bool ask_for_user_feedback = 7;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
