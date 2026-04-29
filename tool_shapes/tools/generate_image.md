# `generate_image`

**Cortex step type:** `CortexStepGenerateImage`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepGenerateImage {
  string prompt = 1;
  repeated string image_paths = 2;
  string image_name = 4;
  exa.codeium_common_pb.ImageData generated_image = 3;
  string model_name = 5;
  exa.codeium_common_pb.Media generated_media = 6;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
