# `find`

**Cortex step type:** `CortexStepFind`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (14)

```proto
message CortexStepFind {
  string search_directory = 10;
  string pattern = 1;
  repeated string excludes = 3;
  exa.cortex_pb.FindResultType type = 4;
  int32 max_depth = 5;
  repeated string extensions = 12;
  bool full_path = 13;
  string truncated_output = 14;
  uint32 truncated_total_results = 15;
  uint32 total_results = 7;
  string raw_output = 11;
  string command_run = 9;
  repeated string includes = 2;
  string find_error = 8;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `pattern`
```
The search term or pattern to look for within files.
```
```
Optional, Pattern to search for, supports glob format
```
```
Optional, whether the full absolute path must match the glob pattern, default: only filename needs to match. Take care when specifying glob patterns with this flag on, e.g when FullPath is on, pattern '*.py' will not match to the file '/foo/bar.py', but pattern '**/*.py' will match.
```

### `type`
```
Optional, type filter, enum=file,directory,any
```
```
Type name of the subagent to invoke.
```
```
Type of reference (e.g., file, conversation_id, url)
```

### `extensions`
```
Optional, file extensions to include (without leading .), matching paths must match at least one of the included extensions
```
