# `MqueryToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (9)

```proto
message MqueryToolConfig {
  exa.codeium_common_pb.MQueryConfig m_query_config = 1;
  exa.codeium_common_pb.Model m_query_model = 2;
  uint32 max_tokens_per_m_query = 3;
  int32 num_items_full_source = 4;
  int32 max_lines_per_snippet = 5;
  bool enable_search_in_file_tool = 6;
  bool allow_access_gitignore = 7;
  bool disable_semantic_codebase_search = 8;
  bool force_disable = 9;
}
```
