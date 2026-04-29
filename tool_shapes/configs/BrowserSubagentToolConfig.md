# `BrowserSubagentToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (13)

```proto
message BrowserSubagentToolConfig {
  exa.cortex_pb.BrowserSubagentMode mode = 1;
  exa.codeium_common_pb.Model browser_subagent_model = 2;
  bool use_detailed_converter = 3;
  int32 suggested_max_tool_calls = 4;
  bool disable_onboarding = 5;
  exa.cortex_pb.SubagentReminderMode subagent_reminder_mode = 6;
  int32 max_context_tokens = 7;
  exa.cortex_pb.BrowserSubagentContextConfig context_config = 8;
  exa.cortex_pb.DOMExtractionConfig dom_extraction_config = 9;
  bool disable_screenshot = 10;
  exa.cortex_pb.LowLevelToolsConfig low_level_tools_config = 11;
  bool enable_scratchpad = 12;
  bool include_ci_prompt = 13;
}
```
