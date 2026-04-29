# `GrepToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message GrepToolConfig {
  uint32 max_grep_results = 1;
  bool include_cci_in_result = 2;
  uint32 num_full_source_ccis = 3;
  uint32 max_bytes_per_cci = 4;
  bool allow_access_gitignore = 6;
  bool use_code_search = 7;
  bool disable_fallback_to_local_execution = 8;
}
```
