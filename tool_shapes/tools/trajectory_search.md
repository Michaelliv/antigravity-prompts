# `trajectory_search`

**Cortex step type:** `CortexStepTrajectorySearch`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (6)

```proto
message CortexStepTrajectorySearch {
  string id = 1;
  string query = 2;
  exa.cortex_pb.TrajectorySearchIdType id_type = 3;
  repeated exa.context_module_pb.CciWithSubrangeWithRetrievalMetadata chunks = 4;
  exa.cortex_pb.TrajectoryDescription trajectory_description = 5;
  uint32 total_chunks = 6;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `id`
```
ID of the command to get status for
```
```
The ID of the message to read. Required when Action is 'read'.
```
```
The recipient ID to send the message to, e.g. a subagent conversation ID.
```

### `query`
```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```
```
If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality.
```

### `chunks`
```
A list of chunks to replace. It is best to provide multiple chunks for non-contiguous edits if possible. This must be a JSON array, not a string.
```
