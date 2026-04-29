# `view_code_item`

**Cortex step type:** `CortexStepViewCodeItem`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (4)

```proto
message CortexStepViewCodeItem {
  string absolute_uri = 1;
  repeated string node_paths = 4;
  repeated exa.codeium_common_pb.CodeContextItem ccis = 5;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 6;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
