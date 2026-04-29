# `artifact_summary`

**Cortex step type:** `CortexStepArtifactSummary`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (1)

```proto
message CortexStepArtifactSummary {
  string summary = 1;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `summary`
```
One paragraph summary of the Knowledge Item
```
```
Detailed multi-line summary of the artifact file, after edits have been made. Summary does not need to mention the artifact name and should focus on the contents and purpose of the artifact.
```
```
A short, user-friendly summary of the task (1-2 sentences max). This will be displayed to the user in the UI instead of the full task description. Should be concise and describe the goal at a high level.
```
