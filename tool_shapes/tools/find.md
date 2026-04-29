# `find`

**Cortex step type:** `CortexStepFind`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
