# `write_blob`

**Cortex step type:** `CortexStepWriteBlob`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepWriteBlob {
  string blob_id = 1;
  string target_path = 2;
  string error_message = 3;
  int64 bytes_written = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
