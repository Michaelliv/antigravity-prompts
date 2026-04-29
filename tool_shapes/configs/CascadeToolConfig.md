# `CascadeToolConfig`

**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (32)

```proto
message CascadeToolConfig {
  exa.cortex_pb.MqueryToolConfig mquery = 1;
  exa.cortex_pb.CodeToolConfig code = 2;
  exa.cortex_pb.IntentToolConfig intent = 3;
  exa.cortex_pb.GrepToolConfig grep = 4;
  exa.cortex_pb.FindToolConfig find = 5;
  exa.cortex_pb.RunCommandToolConfig run_command = 8;
  exa.cortex_pb.KnowledgeBaseSearchToolConfig knowledge_base_search = 9;
  exa.cortex_pb.ViewFileToolConfig view_file = 10;
  exa.cortex_pb.SuggestedResponseConfig suggested_response = 11;
  exa.cortex_pb.SearchWebToolConfig search_web = 13;
  exa.cortex_pb.MemoryToolConfig memory = 14;
  exa.cortex_pb.McpToolConfig mcp = 16;
  exa.cortex_pb.ListDirToolConfig list_dir = 19;
  exa.cortex_pb.ViewCodeItemToolConfig view_code_item = 20;
  exa.cortex_pb.ReadKnowledgeBaseItemToolConfig read_knowledge_base_item = 21;
  exa.cortex_pb.CommandStatusToolConfig command_status = 23;
  exa.cortex_pb.AntigravityBrowserToolConfig antigravity_browser = 25;
  exa.cortex_pb.TrajectorySearchToolConfig trajectory_search = 28;
  exa.cortex_pb.CodeSearchToolConfig code_search = 31;
  exa.cortex_pb.InternalSearchToolConfig internal_search = 32;
  exa.cortex_pb.NotifyUserConfig notify_user = 33;
  exa.cortex_pb.BrowserSubagentToolConfig browser_subagent = 34;
  exa.cortex_pb.TaskBoundaryToolConfig task_boundary = 35;
  exa.cortex_pb.FinishToolConfig finish = 36;
  exa.cortex_pb.WorkspaceAPIToolConfig workspace_api = 37;
  exa.cortex_pb.NotebookEditToolConfig notebook_edit = 38;
  exa.cortex_pb.InvokeSubagentToolConfig invoke_subagent = 39;
  exa.cortex_pb.GenerateImageToolConfig generate_image = 40;
  exa.cortex_pb.AskQuestionToolConfig ask_question = 41;
  exa.cortex_pb.PermissionConfig permission_config = 42;
  exa.cortex_pb.ToolDescriptionOverrideMap description_override_map = 22;
  bool disable_simple_research_tools = 29;
}
```
