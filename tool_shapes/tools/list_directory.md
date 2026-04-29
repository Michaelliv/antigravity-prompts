# `list_directory`

**Cortex step type:** `CortexStepListDirectory`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepListDirectory {
  string directory_path_uri = 1;
  repeated string children = 2;
  repeated exa.cortex_pb.ListDirectoryResult results = 3;
  bool dir_not_found = 4;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
