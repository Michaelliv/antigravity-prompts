# `compile_diagnostic`

**Cortex step type:** `CortexStepCompileDiagnostic`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepCompileDiagnostic {
  string message = 1;
  string path = 2;
  uint32 line = 3;
  uint32 column = 4;
  string symbol = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `message`
```
The message content.
```
```
The ID of the message to read. Required when Action is 'read'.
```
```
The recipient ID to send the message to, e.g. a subagent conversation ID.
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

### `line`
```
The exact command line string to execute.
```
```
Detailed multi-line summary of the artifact file, after edits have been made. Summary does not need to mention the artifact name and should focus on the contents and purpose of the artifact.
```
```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```
