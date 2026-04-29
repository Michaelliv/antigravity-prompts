# `write_to_file`

**Cortex step type:** `CortexStepWriteToFile`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (5)

Field names recovered from `(*CortexStepWriteToFile).Get*` symbols (includes both inputs and outputs).

- `AcknowledgementType`
- `CodeContent`
- `Diff`
- `FileCreated`
- `TargetFileUri`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The target file to create and write code to.
```

### 2.
```
The code contents to write to the file.
```

### 3.
```
Set this to true to overwrite an existing file. WARNING: This will replace the entire file contents. Only use when you explicitly intend to overwrite. Otherwise, use a code edit tool to modify existing files.
```
