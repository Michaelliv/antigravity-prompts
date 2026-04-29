# `generate_image`

**Cortex step type:** `CortexStepGenerateImage`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (6)

Field names recovered from `(*CortexStepGenerateImage).Get*` symbols (includes both inputs and outputs).

- `GeneratedImage`
- `GeneratedMedia`
- `ImageName`
- `ImagePaths`
- `ModelName`
- `Prompt`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The text prompt to generate an image for.
```

### 2.
```
Name of the generated image to save. Should be all lowercase with underscores, describing what the image contains. Maximum 3 words. Example: 'login_page_mockup'
```

### 3.
```
Optional absolute paths to the images to use in generation. You can pass in images here if you would like to edit or combine images. You can pass in artifact images and any images in the file system. Note: you cannot pass in more than 3 images.
```
