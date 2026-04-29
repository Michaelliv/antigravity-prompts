# `compile`

**Cortex step type:** `CortexStepCompile`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (8)

```proto
message CortexStepCompile {
  exa.cortex_pb.CortexStepCompileTool tool = 1;
  string input_spec = 2;
  repeated exa.cortex_pb.CortexStepCompile.OptionsEntry options = 3;
  string target = 4;
  string artifact_path = 5;
  bool artifact_is_executable = 6;
  repeated exa.cortex_pb.CortexStepCompileDiagnostic errors = 7;
  repeated exa.cortex_pb.CortexStepCompileDiagnostic warnings = 8;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `tool`
```
List of tool names available to the subagent. If empty, inherits default tools.
```
```
The request ID to retrieve details for. This ID can be obtained from the list_network_requests tool.
```
```
A single contiguous chunk to replace. For non-contiguous edits, use the multi_replace_file_content tool instead.
```

### `options`
```
direction of the scroll. Options are left, right, up, down
```
```
Mouse button to press. Options are 'left', 'right', or 'middle'.
```
```
Mouse button to release. Options are 'left', 'right', or 'middle'.
```

### `target`
```
The target file to create and write code to.
```
```
The content to replace the target content with.
```
```
The target file to modify. Always specify the target file as the very first argument.
```

### `errors`
```
If applicable, IDs of lint errors this edit aims to fix (they'll have been given in recent IDE feedback). If you believe the edit could fix lints, do specify lint IDs; if the edit is wholly unrelated, do not. A rule of thumb is, if your edit was influenced by lint feedback, include lint IDs. Exercise honest judgement here.
```
