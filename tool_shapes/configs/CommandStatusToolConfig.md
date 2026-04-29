# `CommandStatusToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CommandStatusToolConfig {
  bool use_delta = 1;
  int32 max_output_characters = 2;
  int32 min_output_characters = 3;
  int32 max_wait_duration_seconds = 4;
  int32 output_stabilization_duration_seconds = 5;
  bool enable_input_detection = 6;
  exa.codeium_common_pb.Model input_detection_model = 7;
}
```
