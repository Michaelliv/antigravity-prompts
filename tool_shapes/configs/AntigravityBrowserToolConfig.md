# `AntigravityBrowserToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (26)

```proto
message AntigravityBrowserToolConfig {
  bool enabled = 1;
  exa.cortex_pb.AutoRunDecision auto_run_decision = 2;
  exa.cortex_pb.CaptureBrowserScreenshotToolConfig capture_browser_screenshot = 3;
  exa.cortex_pb.BrowserSubagentToolConfig browser_subagent = 4;
  exa.cortex_pb.ClickBrowserPixelToolConfig click_browser_pixel = 5;
  exa.cortex_pb.BrowserStateDiffingConfig browser_state_diffing_config = 10;
  exa.cortex_pb.BrowserListNetworkRequestsToolConfig browser_list_network_requests_tool_config = 18;
  exa.cortex_pb.BrowserGetNetworkRequestToolConfig browser_get_network_request_tool_config = 19;
  exa.cortex_pb.BrowserToolSetMode tool_set_mode = 6;
  bool disable_open_url = 7;
  bool is_eval_mode = 9;
  exa.codeium_common_pb.BrowserJsExecutionPolicy browser_js_execution_policy = 11;
  bool disable_actuation_overlay = 12;
  bool variable_wait_tool = 13;
  exa.codeium_common_pb.BrowserJsAutoRunPolicy browser_js_auto_run_policy = 8;
  exa.cortex_pb.BrowserWindowSize initial_browser_window_size = 14;
  exa.cortex_pb.DOMExtractionConfig dom_extraction_config = 15;
  bool disable_workspace_api = 16;
  bool open_page_in_background = 17;
  bool use_antigravity_as_browser_prompting = 20;
  bool enable_refresh_tool = 21;
  bool disable_read_browser_page = 22;
  bool use_extended_timeout = 23;
  bool log_timeout_errors_instead_of_sentry = 24;
  bool skip_permission_checks = 25;
  bool display_on_crd = 26;
}
```
