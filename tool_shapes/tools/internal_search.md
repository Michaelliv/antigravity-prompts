# `internal_search`

**Cortex step type:** `CortexStepInternalSearch`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (2)

```proto
message CortexStepInternalSearch {
  string query = 1;
  repeated exa.cortex_pb.InternalSearchResults results = 2;
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
