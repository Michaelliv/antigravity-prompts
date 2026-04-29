# `propose_code`

**Cortex step type:** `CortexStepProposeCode`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (4)

Field names recovered from `(*CortexStepProposeCode).Get*` symbols (includes both inputs and outputs).

- `ActionResult`
- `ActionSpec`
- `CodeInstruction`
- `MarkdownLanguage`


## Parameter descriptions (12)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Set to true to request user feedback on this artifact.
```

### 2.
```
A description of the changes that you are making to the file.
```

### 3.
```
Metadata for the artifact, required when IsArtifact is true.
```

### 4.
```
Set this to true when creating an artifact file.
```

### 5.
```
Markdown language for the code block, e.g 'python' or 'javascript'
```

### 6.
```
The target file to modify. Always specify the target file as the very first argument.
```

### 7.
```
Classification of the edit. Examples include "Continuing the user's work", "Bug fix", and "Documentation".
```

### 8.
```
Type of artifact: 'implementation_plan', 'walkthrough', 'task', or 'other'.
```

### 9.
```
Brief, user-facing explanation of what this change did. Focus on non-obvious rationale, design decisions, or important context. Don't just restate what the code does.
```

### 10.
```
Detailed multi-line summary of the artifact file, after edits have been made. Summary does not need to mention the artifact name and should focus on the contents and purpose of the artifact.
```

### 11.
```
A measure of how important and relevant the edit is to the user's task. Use 'high' for edits directly addressing the main request or fixing critical issues, 'medium' for supporting changes, 'low' for minor improvements. enum=high,medium,low
```

### 12.
```
If applicable, IDs of lint errors this edit aims to fix (they'll have been given in recent IDE feedback). If you believe the edit could fix lints, do specify lint IDs; if the edit is wholly unrelated, do not. A rule of thumb is, if your edit was influenced by lint feedback, include lint IDs. Exercise honest judgement here.
```
