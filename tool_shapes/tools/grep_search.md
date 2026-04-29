# `grep_search`

**Cortex step type:** `CortexStepGrepSearch`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (15)

```proto
message CortexStepGrepSearch {
  string search_path_uri = 11;
  string query = 1;
  bool match_per_line = 8;
  repeated string includes = 2;
  bool case_insensitive = 9;
  bool allow_access_gitignore = 13;
  bool is_regex = 14;
  repeated exa.cortex_pb.GrepSearchResult results = 4;
  uint32 total_results = 7;
  string raw_output = 3;
  string command_run = 10;
  bool no_files_searched = 12;
  bool timed_out = 15;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 16;
  string grep_error = 5;
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
