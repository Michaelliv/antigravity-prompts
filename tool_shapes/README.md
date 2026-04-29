# Antigravity tool shapes

Tool input schemas reverse-engineered from the Antigravity language-server
binary. Two complementary sources are combined here — see *Source of truth*
below for what each one really represents.

## Source of truth

There are **two** distinct kinds of "tool shape" inside the binary, and
they are not the same object:

1. **Cortex-step proto messages** (`CortexStep<X>` in `cortex.proto`). These
   describe the **outcome state** of a tool call — the structured record
   that gets stored in the trajectory after the tool runs. Recovered
   byte-exact from a `FileDescriptorProto` blob embedded in the Go binary.
   `protodump`/`redress`/GoReSym all fail on it because of Edition 2024
   features in the file; the Python `protobuf` library parses it
   partially-but-richly enough to recover every message and field.

2. **JSON-schema tool-arg Go structs** (e.g. `tools.runCommandArgs`,
   `notebook.editNotebookArgs`). These are what the model fills in when
   calling a tool. They live in a separate Go object hierarchy with
   their own field names. Recovered byte-exact from two locations in
   the binary:
   - `utils.ToJsonSchemaString[go.shape.struct {…}]` and
     `utils.ParseToolArgs[go.shape.struct {…}]` generic-instantiation
     symbols, which carry the full inline struct body for anonymous
     argument structs.
   - Go reflect-name records in rodata, which carry per-named-type
     `(flag, name, tag)` triples for field-by-field arg structs.

The two namespaces share neither identity nor field-name conventions, so
you can't statically attribute a recovered tool-arg field to a specific
`CortexStep<X>` message with confidence. The flat
[`byte_exact_field_index.md`](byte_exact_field_index.md) presents the
recovered tags un-attributed; map them to tools by reading the
description text.

## Stats

- 421 proto message types (in `cortex.proto`)
- 70 enums
- 118 `CortexStep*` tool-output messages (one Markdown stub each)
- 37 `*ToolConfig` server-side configs
- 31 byte-exact inline tool-arg structs (`jsonschema_structs/`)
- 122 byte-exact rname clusters (`recovered_field_tables/`)
- 179 byte-exact `(field, tag)` pairs (`byte_exact_field_index.md`)

## Files

- [`byte_exact_field_index.md`](byte_exact_field_index.md) — **canonical**
  flat catalog of every recovered `(field_name, jsonschema-tag)` pair, with
  binary offsets. Un-attributed by design.
- `tools/*.md` — one file per `CortexStep*` proto message: just the
  proto schema. Field-description attribution intentionally omitted; see
  `byte_exact_field_index.md` instead.
- `jsonschema_structs/*.md` — byte-exact tool-arg structs whose body was
  inlined in a `ToJsonSchemaString[go.shape.struct {…}]` symbol
  (anonymous structs only).
- `recovered_field_tables/*.md` — byte-exact rname-record clusters,
  including their binary offsets and a (best-effort, sometimes wrong)
  spatial guess at a parent `CortexStep<X>` token nearby.
- `configs/*.md` — `*ToolConfig` server-side configs (timeouts,
  force-disable, etc.) recovered from `cortex.proto`.
- `../protos/third_party/jetski/cortex_pb/cortex.proto` — full
  reconstructed proto file.
- `../protos/third_party/jetski/cortex_pb/cortex.fdproto.bin` — binary
  FileDescriptorProto (use with `protoc --descriptor_set_in`).
- `../protos/third_party/jetski/cortex_pb/cortex.textproto` — textproto
  dump of the FileDescriptorProto.

## Tool inventory

- [`agency_tool_call`](tools/agency_tool_call.md) — `CortexStepAgencyToolCall` (4 fields)
- [`artifact_summary`](tools/artifact_summary.md) — `CortexStepArtifactSummary` (1 fields)
- [`ask_question`](tools/ask_question.md) — `CortexStepAskQuestion` (1 fields)
- [`brain_update`](tools/brain_update.md) — `CortexStepBrainUpdate` (3 fields)
- [`browser_click_element`](tools/browser_click_element.md) — `CortexStepBrowserClickElement` (7 fields)
- [`browser_drag_pixel_to_pixel`](tools/browser_drag_pixel_to_pixel.md) — `CortexStepBrowserDragPixelToPixel` (5 fields)
- [`browser_get_dom`](tools/browser_get_dom.md) — `CortexStepBrowserGetDom` (5 fields)
- [`browser_get_network_request`](tools/browser_get_network_request.md) — `CortexStepBrowserGetNetworkRequest` (4 fields)
- [`browser_input`](tools/browser_input.md) — `CortexStepBrowserInput` (7 fields)
- [`browser_list_network_requests`](tools/browser_list_network_requests.md) — `CortexStepBrowserListNetworkRequests` (5 fields)
- [`browser_mouse_down`](tools/browser_mouse_down.md) — `CortexStepBrowserMouseDown` (4 fields)
- [`browser_mouse_up`](tools/browser_mouse_up.md) — `CortexStepBrowserMouseUp` (4 fields)
- [`browser_mouse_wheel`](tools/browser_mouse_wheel.md) — `CortexStepBrowserMouseWheel` (7 fields)
- [`browser_move_mouse`](tools/browser_move_mouse.md) — `CortexStepBrowserMoveMouse` (5 fields)
- [`browser_press_key`](tools/browser_press_key.md) — `CortexStepBrowserPressKey` (5 fields)
- [`browser_refresh_page`](tools/browser_refresh_page.md) — `CortexStepBrowserRefreshPage` (3 fields)
- [`browser_resize_window`](tools/browser_resize_window.md) — `CortexStepBrowserResizeWindow` (7 fields)
- [`browser_scroll`](tools/browser_scroll.md) — `CortexStepBrowserScroll` (8 fields)
- [`browser_scroll_down`](tools/browser_scroll_down.md) — `CortexStepBrowserScrollDown` (5 fields)
- [`browser_scroll_up`](tools/browser_scroll_up.md) — `CortexStepBrowserScrollUp` (5 fields)
- [`browser_select_option`](tools/browser_select_option.md) — `CortexStepBrowserSelectOption` (5 fields)
- [`browser_subagent`](tools/browser_subagent.md) — `CortexStepBrowserSubagent` (12 fields)
- [`capture_browser_console_logs`](tools/capture_browser_console_logs.md) — `CortexStepCaptureBrowserConsoleLogs` (3 fields)
- [`capture_browser_screenshot`](tools/capture_browser_screenshot.md) — `CortexStepCaptureBrowserScreenshot` (12 fields)
- [`check_deploy_status`](tools/check_deploy_status.md) — `CortexStepCheckDeployStatus` (7 fields)
- [`checkpoint`](tools/checkpoint.md) — `CortexStepCheckpoint` (19 fields)
- [`click_browser_pixel`](tools/click_browser_pixel.md) — `CortexStepClickBrowserPixel` (8 fields)
- [`clipboard`](tools/clipboard.md) — `CortexStepClipboard` (1 fields)
- [`cloud_s_q_l_execute_s_q_l`](tools/cloud_s_q_l_execute_s_q_l.md) — `CortexStepCloudSQLExecuteSQL` (5 fields)
- [`cloud_s_q_l_schema_update`](tools/cloud_s_q_l_schema_update.md) — `CortexStepCloudSQLSchemaUpdate` (4 fields)
- [`code_acknowledgement`](tools/code_acknowledgement.md) — `CortexStepCodeAcknowledgement` (4 fields)
- [`code_action`](tools/code_action.md) — `CortexStepCodeAction` (22 fields)
- [`code_search`](tools/code_search.md) — `CortexStepCodeSearch` (4 fields)
- [`command_status`](tools/command_status.md) — `CortexStepCommandStatus` (12 fields)
- [`compile`](tools/compile.md) — `CortexStepCompile` (8 fields)
- [`compile_applet`](tools/compile_applet.md) — `CortexStepCompileApplet` (2 fields)
- [`compile_diagnostic`](tools/compile_diagnostic.md) — `CortexStepCompileDiagnostic` (5 fields)
- [`conversation_history`](tools/conversation_history.md) — `CortexStepConversationHistory` (1 fields)
- [`delete_directory`](tools/delete_directory.md) — `CortexStepDeleteDirectory` (2 fields)
- [`deploy_firebase`](tools/deploy_firebase.md) — `CortexStepDeployFirebase` (1 fields)
- [`deploy_web_app`](tools/deploy_web_app.md) — `CortexStepDeployWebApp` (17 fields)
- [`dummy`](tools/dummy.md) — `CortexStepDummy` (2 fields)
- [`edit_notebook`](tools/edit_notebook.md) — `CortexStepEditNotebook` (3 fields)
- [`ephemeral_message`](tools/ephemeral_message.md) — `CortexStepEphemeralMessage` (5 fields)
- [`error_message`](tools/error_message.md) — `CortexStepErrorMessage` (3 fields)
- [`execute_browser_java_script`](tools/execute_browser_java_script.md) — `CortexStepExecuteBrowserJavaScript` (13 fields)
- [`execute_notebook`](tools/execute_notebook.md) — `CortexStepExecuteNotebook` (3 fields)
- [`file_breakdown`](tools/file_breakdown.md) — `CortexStepFileBreakdown` (2 fields)
- [`file_change`](tools/file_change.md) — `CortexStepFileChange` (8 fields)
- [`find`](tools/find.md) — `CortexStepFind` (14 fields)
- [`find_all_references`](tools/find_all_references.md) — `CortexStepFindAllReferences` (5 fields)
- [`finish`](tools/finish.md) — `CortexStepFinish` (2 fields)
- [`generate_image`](tools/generate_image.md) — `CortexStepGenerateImage` (6 fields)
- [`generator_metadata`](tools/generator_metadata.md) — `CortexStepGeneratorMetadata` (7 fields)
- [`generic`](tools/generic.md) — `CortexStepGeneric` (2 fields)
- [`git_commit`](tools/git_commit.md) — `CortexStepGitCommit` (3 fields)
- [`grep_search`](tools/grep_search.md) — `CortexStepGrepSearch` (15 fields)
- [`install_applet_dependencies`](tools/install_applet_dependencies.md) — `CortexStepInstallAppletDependencies` (2 fields)
- [`install_applet_package`](tools/install_applet_package.md) — `CortexStepInstallAppletPackage` (5 fields)
- [`internal_metadata`](tools/internal_metadata.md) — `CortexStepInternalMetadata` (1 fields)
- [`internal_search`](tools/internal_search.md) — `CortexStepInternalSearch` (2 fields)
- [`invoke_subagent`](tools/invoke_subagent.md) — `CortexStepInvokeSubagent` (5 fields)
- [`k_i_insertion`](tools/k_i_insertion.md) — `CortexStepKIInsertion` (1 fields)
- [`knowledge_artifacts`](tools/knowledge_artifacts.md) — `CortexStepKnowledgeArtifacts` (1 fields)
- [`knowledge_generation`](tools/knowledge_generation.md) — `CortexStepKnowledgeGeneration` (0 fields)
- [`lint_applet`](tools/lint_applet.md) — `CortexStepLintApplet` (3 fields)
- [`lint_diff`](tools/lint_diff.md) — `CortexStepLintDiff` (2 fields)
- [`list_browser_pages`](tools/list_browser_pages.md) — `CortexStepListBrowserPages` (1 fields)
- [`list_directory`](tools/list_directory.md) — `CortexStepListDirectory` (5 fields)
- [`list_resources`](tools/list_resources.md) — `CortexStepListResources` (4 fields)
- [`lookup_knowledge_base`](tools/lookup_knowledge_base.md) — `CortexStepLookupKnowledgeBase` (3 fields)
- [`manager_feedback`](tools/manager_feedback.md) — `CortexStepManagerFeedback` (2 fields)
- [`mcp_tool`](tools/mcp_tool.md) — `CortexStepMcpTool` (13 fields)
- [`memory`](tools/memory.md) — `CortexStepMemory` (4 fields)
- [`metadata`](tools/metadata.md) — `CortexStepMetadata` (32 fields)
- [`move`](tools/move.md) — `CortexStepMove` (2 fields)
- [`mquery`](tools/mquery.md) — `CortexStepMquery` (5 fields)
- [`notify_user`](tools/notify_user.md) — `CortexStepNotifyUser` (8 fields)
- [`open_browser_url`](tools/open_browser_url.md) — `CortexStepOpenBrowserUrl` (10 fields)
- [`outline`](tools/outline.md) — `CortexStepOutline` (4 fields)
- [`plan_input`](tools/plan_input.md) — `CortexStepPlanInput` (2 fields)
- [`planner_response`](tools/planner_response.md) — `CortexStepPlannerResponse` (14 fields)
- [`post_pr_review`](tools/post_pr_review.md) — `CortexStepPostPrReview` (7 fields)
- [`proposal_feedback`](tools/proposal_feedback.md) — `CortexStepProposalFeedback` (3 fields)
- [`propose_code`](tools/propose_code.md) — `CortexStepProposeCode` (4 fields)
- [`r_p_c_action`](tools/r_p_c_action.md) — `CortexStepRPCAction` (5 fields)
- [`read_browser_page`](tools/read_browser_page.md) — `CortexStepReadBrowserPage` (3 fields)
- [`read_deployment_config`](tools/read_deployment_config.md) — `CortexStepReadDeploymentConfig` (9 fields)
- [`read_knowledge_base_item`](tools/read_knowledge_base_item.md) — `CortexStepReadKnowledgeBaseItem` (3 fields)
- [`read_notebook`](tools/read_notebook.md) — `CortexStepReadNotebook` (3 fields)
- [`read_resource`](tools/read_resource.md) — `CortexStepReadResource` (4 fields)
- [`read_terminal`](tools/read_terminal.md) — `CortexStepReadTerminal` (3 fields)
- [`read_url_content`](tools/read_url_content.md) — `CortexStepReadUrlContent` (6 fields)
- [`resolve_task`](tools/resolve_task.md) — `CortexStepResolveTask` (5 fields)
- [`restart_dev_server`](tools/restart_dev_server.md) — `CortexStepRestartDevServer` (1 fields)
- [`retrieve_memory`](tools/retrieve_memory.md) — `CortexStepRetrieveMemory` (8 fields)
- [`run_command`](tools/run_command.md) — `CortexStepRunCommand` (28 fields)
- [`run_extension_code`](tools/run_extension_code.md) — `CortexStepRunExtensionCode` (7 fields)
- [`search_knowledge_base`](tools/search_knowledge_base.md) — `CortexStepSearchKnowledgeBase` (5 fields)
- [`search_web`](tools/search_web.md) — `CortexStepSearchWeb` (7 fields)
- [`send_command_input`](tools/send_command_input.md) — `CortexStepSendCommandInput` (10 fields)
- [`set_up_cloud_sql`](tools/set_up_cloud_sql.md) — `CortexStepSetUpCloudSql` (4 fields)
- [`set_up_firebase`](tools/set_up_firebase.md) — `CortexStepSetUpFirebase` (8 fields)
- [`shell_exec`](tools/shell_exec.md) — `CortexStepShellExec` (4 fields)
- [`state`](tools/state.md) — `CortexStepState` (1 fields)
- [`suggested_responses`](tools/suggested_responses.md) — `CortexStepSuggestedResponses` (1 fields)
- [`system_message`](tools/system_message.md) — `CortexStepSystemMessage` (4 fields)
- [`task_boundary`](tools/task_boundary.md) — `CortexStepTaskBoundary` (7 fields)
- [`tool_call_choice`](tools/tool_call_choice.md) — `CortexStepToolCallChoice` (3 fields)
- [`tool_call_proposal`](tools/tool_call_proposal.md) — `CortexStepToolCallProposal` (1 fields)
- [`trajectory_choice`](tools/trajectory_choice.md) — `CortexStepTrajectoryChoice` (3 fields)
- [`trajectory_search`](tools/trajectory_search.md) — `CortexStepTrajectorySearch` (6 fields)
- [`user_input`](tools/user_input.md) — `CortexStepUserInput` (13 fields)
- [`view_code_item`](tools/view_code_item.md) — `CortexStepViewCodeItem` (4 fields)
- [`view_content_chunk`](tools/view_content_chunk.md) — `CortexStepViewContentChunk` (3 fields)
- [`view_file`](tools/view_file.md) — `CortexStepViewFile` (14 fields)
- [`view_file_outline`](tools/view_file_outline.md) — `CortexStepViewFileOutline` (13 fields)
- [`wait`](tools/wait.md) — `CortexStepWait` (1 fields)
- [`workspace_a_p_i`](tools/workspace_a_p_i.md) — `CortexStepWorkspaceAPI` (6 fields)
- [`write_blob`](tools/write_blob.md) — `CortexStepWriteBlob` (4 fields)
- [`write_to_file`](tools/write_to_file.md) — `CortexStepWriteToFile` (5 fields)
