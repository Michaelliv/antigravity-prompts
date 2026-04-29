# `RunCommandToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (13)

```proto
message RunCommandToolConfig {
  uint32 max_chars_command_stdout = 1;
  bool force_disable = 2;
  exa.cortex_pb.AutoCommandConfig auto_command_config = 3;
  bool enable_ide_terminal_execution = 4;
  bool force_go_terminal_execution = 12;
  string shell_name = 5;
  string shell_path = 6;
  uint32 max_timeout_ms = 7;
  string shell_setup_script = 10;
  bool forbid_search_commands = 11;
  bool enable_pty = 13;
  bool enable_persistent_mode = 14;
  bool enable_midterm_output_processor = 8;
}
```
