# Antigravity tool catalog (function-level + parameter-level)

Extracted from the language-server binary. Each entry is the actual text the model
sees as the tool/function description or parameter description.

## `browser_click_dom`

```
Click on an annotated DOM element in a browser page. The index can be found by calling browser_get_dom. Prefer the BrowserInput tool if you need to input text in an element. If the element is not clickable through this tool, you may need to click based on the pixel coordinates instead.
```

## `browser_get_dom`

```
Get the DOM tree of an open page in the browser. Returns only interactive elements and text within the current viewport, each with an index for interaction. If an element is not included, it may be outside the viewport or getting filtered for other reasons - refer to the screenshot to confirm. Then try read_browser_page and browser_scroll tools.
```

## `browser_drag`

```
Drag from one pixel coordinate to another in the browser. This simulates a click, drag, and drag operation from the starting coordinates, through zero or more intermediate coordinates, and then to the ending coordinates.
```

## `reload_browser_page`

```
Reload/refresh a browser page. Use this when you need to refresh the page to see updated content, retry a failed page load, or reset the page state.
```

## `read_console_logs`

```
Retrieve the console logs of a browser page that is already open in the browser.
```

## `execute_browser_javascript`

```
Execute JavaScript on a page in the browser for navigation and interaction. The JavaScript runs in the page context and should be a valid expression or statement sequence. Does not modify page content.
```

## `browser_select_option`

```
Select an option from a dropdown (select) element in a browser page. The index can be found by calling browser_get_dom.. It's possible one or more expressions may have backslashes that are not properly escaped. Please fix it and try again1.
```

## `list_browser_pages`

```
List all open pages in Jetski Browser and their metadata (page_id, url, title, viewport size, etc.).ed25519: expected opts.Hash zero (unhashed message, for standard Ed25519) or SHA-512 (for Ed25519ph)
```

## `list_dir`

```
List the contents of a directory, i.e. all files and subdirectories that are children of the directory. Directory path must be an absolute path to a directory that exists. For each child in the directory, output will have: relative path to the directory, whether it is a directory or file, size in bytes if file, and number of children (recursive) if directory.
```

## `grep_search`

```
Use ripgrep to find exact pattern matches within files or directories.insertion of row [insertID: %q; insertIndex: %v] failed with error: %s^(import|using|namespace|interface|op|model|scalar|alias|union|enum)\s
```

## `get_network_request`

```
Get detailed information about a specific network request by its request ID. Use this after calling list_network_requests to get more details about a particular request.
```

## `send_message`

```
Send a message to another agent. This tool can be used to communicate with subagents, peer agents, etc. Do not use this tool to communicate with the user.If you are making multiple edits across a single file, %s. DO NOT try to replace the entire existing content with the new content, this is very expensive.I just made the changes:
```

## `manage_inbox`

```
Manage your message inbox. Use this tool to list all messages or read the full content of a specific message. Do not use this tool to poll for messages.^\s*namespace\s|^\s*
```

## `inherit_subagent`

```
Subagent that inherits the parent agent's full configuration including tools, system prompt, and model. Use this when you need to run a task in a separate conversation context but with the same capabilities as the current agent.When using pixel clicking, your tool call coordinates will be scaled to the browser's actual dimensions when your tool call is processed. Follow your tool call's guidance on which coordinate ranges are acceptable in your output.Use this tool ONLY when you are making MULTIPLE, NON-CONTIGUOUS edits to the same file (i.e., you are changing more than one separate block of text). If you are making a single contiguous block of edits, use the %s tool instead.
```

## `delete_knowledge`

```
Delete files or directories within the knowledge base. This tool can ONLY delete:
```

## `workspace_api`

```
Make authenticated HTTP requests to Google Workspace APIs (Docs, Sheets, Slides, Drive). Requires the full API URL, HTTP method, and request body. Use this tool for almost all operations on Google Workspace files. Use manual browser automation only as a fallback if the API lacks the specific capability required for the task.
```

## `multi_replace_file`

```
Use this tool ONLY when you are making MULTIPLE, NON-CONTIGUOUS edits to the same file (i.e., you are changing more than one separate block of text). If you are making a single contiguous block of edits, use the %s tool instead.
```

## `replace_file`

```
Use this tool ONLY when you are making a SINGLE CONTIGUOUS block of edits to the same file (i.e. replacing a single contiguous block of text). If you are making edits to multiple non-adjacent lines, use the %s tool instead.grpc: Server.handleStream received malformed method name %q. Allowing it because the environment variable GRPC_GO_EXPERIMENTAL_DISABLE_STRICT_PATH_CHECKING is set to true, but this option will be removed in a future release.
```

## `browser_mouse_release`

```
Release a mouse button. Use this after browser_mouse_down to complete a click or drag operation.b3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aefaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab73617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f
```

## `set_window_state`

```
WindowState must be one of 'normal', 'minimized', 'maximized', or 'fullscreen', got '%s'
```

## `pixel_click`

```
Clicking at pixel coordinates (%d, %d) on browser page with page_id: %sScrolled page using mouse wheel: (x=%d, y=%d) with delta (dx=%d, dy=%d)
```

## `pixel_scroll`

```
Scrolled page using mouse wheel: (x=%d, y=%d) with delta (dx=%d, dy=%d)
```

## `browser_click_pixel`

```
When using pixel clicking, your tool call coordinates will be scaled to the browser's actual dimensions when your tool call is processed. Follow your tool call's guidance on which coordinate ranges are acceptable in your output.Use this tool ONLY when you are making MULTIPLE, NON-CONTIGUOUS edits to the same file (i.e., you are changing more than one separate block of text). If you are making a single contiguous block of edits, use the %s tool instead.
```

## `finish`

```
Task is complete. Summarize what you did and do not call any more tools.Your web applications should be built using the following technologies:,src[%d] has type %T, which is not a ValueSaver, struct or struct pointerbigquery: can only infer schema from struct or pointer to struct, not %s
```

## `browser_screenshot`

```
Captured region: x=%.0f, y=%.0f, width=%.0f, height=%.0f (CSS pixels)
```

## `request_input`

```
If the user's request does NOT warrant a plan then continue your work WITHOUT making a plan or requesting user feedback.
```

## `image_describe`

```
Describe this video in A LOT OF detail. This text will be used in place of the video to answer questions about the video.
```

## `wait`

```
If you are waiting for a condition to happen on a browser page, you should repeatedly call the wait tool with maximum wait time until either the condition is met or the page is in a state where the condition
```

## `subagent_create`

```
A clear, actionable task description for the subagent. Be specific about what the subagent should do and what information it should return."
```

## `browser_subagent_create`

```
A clear, actionable task description for the browser subagent. The subagent is an agent similar to you, with a different set of tools, limited to tools to understand the state of and control the browser. The task you define is the prompt sent to this subagent. Since each agent invocation is a one-shot, autonomous execution, the prompt must be highly detailed, containing a comprehensive task description and all necessary context.
```

## `list_directory`

```
List the contents of a directory, i.e. all files and subdirectories that are children of the directory. Directory path must be an absolute path to a directory that exists. For each child in the directory, output will have: relative path to the directory, whether it is a directory or file, size in bytes if file, and number of children (recursive) if directory.
```

## `replace_failed_correct`

```
Your task is to analyze a failed edit attempt and provide a corrected `replacement_chunk`s that will apply the edit successfully. The correction should be as minimal as possible, staying very close to the original `replacement_chunk`s.
```

## `browser_input_key`

```
Name of the key/key combination to simulate. Examples of keys are: \"F1\" - \"F12\", \"Digit0\"- \"Digit9\", \"KeyA\"- \"KeyZ\", \"Backquote\", \"Minus\", \"Equal\", \"Backslash\", \"Backspace\", \"Tab\", \"Delete\", \"Escape\", \"ArrowDown\", \"End\", \"Enter\", \"Home\", \"Insert\", \"PageDown\", \"PageUp\", \"ArrowRight\", \"ArrowUp\", etc. This tool also supports combinations with modifiers (e.g., Control+Enter). Examples of modifiers are: \"Shift\", \"Control\", \"Alt\", \"Meta\", \"ShiftLeft\", \"ControlOrMeta\".
```

## `window_state`

```
The window state to set. Options: 'normal' (resizable window with specified width/height), 'minimized' (window minimized to taskbar), 'maximized' (window is full screen but shows taskbar), 'fullscreen' (window fills entire screen and hides taskbar). Width and Height are only used when WindowState is 'normal'. Generally you should prefer 'maximized'.
```

## `safe_to_auto_run_cmd`

```
Set to true if you believe that this command is safe to run WITHOUT user approval. An input is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe.
```

## `safe_to_auto_run_js`

```
Set to true if you believe that this code is safe to run WITHOUT user approval. JavaScript is unsafe if it may have some destructive side-effects. Set to true only if you are exremely confident it is safe. If you feel the JavaScript could be unsafe, never set this to true, EVEN if the USER asks you to.
```

## `wait_ms_before_async`

```
This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms).
```

