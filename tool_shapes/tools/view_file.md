# `view_file`

**Cortex step type:** `CortexStepViewFile`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (14)

Field names recovered from `(*CortexStepViewFile).Get*` symbols (includes both inputs and outputs).

- `AbsolutePathUri`
- `BinaryData`
- `Content`
- `EndLine`
- `FilePermissionRequest`
- `IsInjectedReminder`
- `IsSkillFile`
- `MediaData`
- `NumBytes`
- `NumLines`
- `RawContent`
- `SkillMetadata`
- `StartLine`
- `TriggeredMemories`


## Parameter descriptions (5)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Path to file to view. Must be an absolute path.
```

### 2.
```
Number of characters to view. Make this as small as possible to avoid excessive memory usage.
```

### 3.
```
Optional. Startline to view, 1-indexed as usual, inclusive. This value must be less than or equal to EndLine.
```

### 4.
```
Optional. Endline to view, 1-indexed as usual, inclusive. This value must be greater than or equal to StartLine.
```

### 5.
```
Optional. Set to true only when reading a file to execute its instructions for a task. Set to false if the purpose is to edit, preview, or manage the file.
```
