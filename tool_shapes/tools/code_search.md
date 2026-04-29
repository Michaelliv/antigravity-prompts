# `code_search`

**Cortex step type:** `CortexStepCodeSearch`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepCodeSearch {
  string query = 1;
  bool only_paths = 6;
  bool allow_dirs = 7;
  repeated exa.cortex_pb.CodeSearchResults results = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `query`
```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```
```
If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality.
```
