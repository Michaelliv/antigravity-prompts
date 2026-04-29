# `lint_diff`

**Cortex step type:** `CortexStepLintDiff`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (2)

```proto
message CortexStepLintDiff {
  exa.cortex_pb.LintDiffType type = 1;
  exa.codeium_common_pb.CodeDiagnostic lint = 2;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `type`
```
Optional, type filter, enum=file,directory,any
```
```
Type name of the subagent to invoke.
```
```
Type of reference (e.g., file, conversation_id, url)
```

### `lint`
```
If applicable, IDs of lint errors this edit aims to fix (they'll have been given in recent IDE feedback). If you believe the edit could fix lints, do specify lint IDs; if the edit is wholly unrelated, do not. A rule of thumb is, if your edit was influenced by lint feedback, include lint IDs. Exercise honest judgement here.
```
