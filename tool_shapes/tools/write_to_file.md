# `write_to_file`

**Cortex step type:** `CortexStepWriteToFile`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepWriteToFile {
  string target_file_uri = 1;
  repeated string code_content = 2;
  exa.diff_action_pb.DiffBlock diff = 3;
  bool file_created = 4;
  exa.cortex_pb.AcknowledgementType acknowledgement_type = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
