# `CodeToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (17)

```proto
message CodeToolConfig {
  repeated string disable_extensions = 1;
  bool allow_edit_gitignore = 6;
  repeated string file_allowlist = 12;
  repeated string dir_allowlist = 17;
  bool apply_edits = 2;
  bool only_show_incremental_diff_zone = 11;
  bool skip_await_lint_errors = 15;
  exa.cortex_pb.AutoFixLintsConfig auto_fix_lints_config = 5;
  exa.cortex_pb.ReplaceContentToolConfig replace_content_tool_config = 4;
  bool classify_edit = 13;
  bool provide_importance = 16;
  bool skip_replace_content_validation = 9;
  bool override_allow_action_on_unsaved_file = 8;
  bool use_sed_edit = 18;
  bool use_replace_content_edit_tool = 3;
  bool use_replace_content_propose_code = 10;
  bool run_proposal_extension_verifier = 14;
}
```
