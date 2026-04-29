# `grep_search`

**Cortex step type:** `CortexStepGrepSearch`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
