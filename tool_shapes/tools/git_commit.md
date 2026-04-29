# `git_commit`

**Cortex step type:** `CortexStepGitCommit`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepGitCommit {
  exa.cortex_pb.PlanInput input = 1;
  string commit_message = 2;
  string commit_hash = 3;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `input`
```
The text to input into the element.
```
```
The page_id of the browser page to input text on.
```
```
Index of the annotated DOM element to input text into.
```
