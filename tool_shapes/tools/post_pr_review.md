# `post_pr_review`

**Cortex step type:** `CortexStepPostPrReview`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepPostPrReview {
  string body = 1;
  string commit_id = 2;
  string path = 3;
  string side = 4;
  int32 start_line = 5;
  int32 end_line = 6;
  string category = 7;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `body`
```
Request body JSON
```

### `path`
```
Path of the node within the file, e.g package.class.FunctionName
```
```
Absolute path to the .ipynb notebook file.
```
```
Absolute path to the node to edit, e.g /path/to/file
```

### `side`
```
Set to true if you believe that this code is safe to run WITHOUT user approval. JavaScript is unsafe if it may have some destructive side-effects. Set to true only if you are exremely confident it is safe. If you feel the JavaScript could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run potentially unsafe JavaScript.
```
```
Set to true if you believe that this command is safe to run WITHOUT user approval. An input is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the input could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe input.
```
```
Set to true if you believe that this command is safe to run WITHOUT user approval. A command is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the command could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe command.
```
