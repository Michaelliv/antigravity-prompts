# `find_all_references`

**Cortex step type:** `CortexStepFindAllReferences`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepFindAllReferences {
  string absolute_uri = 1;
  string symbol = 2;
  uint32 line = 3;
  uint32 occurrence_index = 4;
  repeated exa.codeium_common_pb.LspReference references = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

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

### `references`
```
List of references related to this Knowledge Item
```
