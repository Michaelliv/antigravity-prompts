# `run_extension_code`

**Cortex step type:** `CortexStepRunExtensionCode`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepRunExtensionCode {
  string code = 1;
  string language = 2;
  bool model_wants_auto_run = 6;
  string user_facing_explanation = 7;
  string output = 3;
  bool user_rejected = 4;
  exa.cortex_pb.RunExtensionCodeAutoRunDecision auto_run_decision = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `code`
```
The target file to create and write code to.
```
```
The code contents to write to the file.
```
```
Markdown language for the code block, e.g 'python' or 'javascript'
```

### `language`
```
Markdown language for the code block, e.g 'python' or 'javascript'
```

### `output`
```
The command ID from a previous run_command call. This is returned in the run_command output.
```
```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```
