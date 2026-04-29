# `view_file`

**Cortex step type:** `CortexStepViewFile`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (14)

```proto
message CortexStepViewFile {
  string absolute_path_uri = 1;
  uint32 start_line = 2;
  uint32 end_line = 3;
  string content = 4;
  bool is_skill_file = 17;
  exa.cortex_pb.SkillMetadata skill_metadata = 18;
  string raw_content = 9;
  exa.codeium_common_pb.ImageData binary_data = 14;
  exa.codeium_common_pb.Media media_data = 15;
  string triggered_memories = 10;
  uint32 num_lines = 11;
  uint32 num_bytes = 12;
  bool is_injected_reminder = 13;
  exa.cortex_pb.FilePermissionInteractionSpec file_permission_request = 16;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `content`
```
The message content.
```
```
URL to read content from
```
```
Content of the prompt section.
```
