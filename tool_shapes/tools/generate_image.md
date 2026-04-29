# `generate_image`

**Cortex step type:** `CortexStepGenerateImage`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (6)

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

From `jsonschema_description:` tags in the binary, matched by field name.

### `prompt`
```
Title of the prompt section.
```
```
The text prompt to generate an image for.
```
```
Content of the prompt section.
```
