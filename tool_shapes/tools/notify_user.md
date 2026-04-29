# `notify_user`

**Cortex step type:** `CortexStepNotifyUser`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (8)

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

From `jsonschema_description:` tags in the binary, matched by field name.
