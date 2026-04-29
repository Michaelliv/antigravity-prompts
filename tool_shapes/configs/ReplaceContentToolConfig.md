# `ReplaceContentToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (9)

```proto
message ReplaceContentToolConfig {
  float max_fuzzy_edit_distance_fraction = 1;
  bool allow_partial_replacement_success = 2;
  uint32 view_file_recency_max_distance = 3;
  bool enable_fuzzy_sandwich_match = 4;
  exa.cortex_pb.FastApplyFallbackConfig fast_apply_fallback_config = 5;
  exa.cortex_pb.ReplaceToolVariant tool_variant = 6;
  bool show_triggered_memories = 8;
  bool disable_allow_multiple = 9;
  bool use_line_range = 10;
}
```
