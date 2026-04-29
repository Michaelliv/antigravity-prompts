# All parameter descriptions extracted from the Antigravity language-server binary

185 unique parameter descriptions (the text the model sees for each tool argument).

### 1. (binary offset 0x54b4bfa)

```
A 2-5 word description of the subagent's role. Should read similar to a job title, e.g. 'Codebase Researcher', 'Database Debugger', etc. Should also be detailed enough to distinguish between different subagents who might share similar purposes.
```

### 2. (binary offset 0x5589997)

```
A clear, actionable task description for the browser subagent. The subagent is an agent similar to you, with a different set of tools, limited to tools to understand the state of and control the browser. The task you define is the prompt sent to this subagent. Since each agent invocation is a one-shot, autonomous execution, the prompt must be highly detailed, containing a comprehensive task description and all necessary context. Avoid vague instructions; be specific about what to do, when to stop, and clearly state exactly what information the agent should return in its final and only report. This should be the second argument.
```

### 3. (binary offset 0x53561a7)

```
A clear, actionable task description for the subagent. Be specific about what the subagent should do and what information it should return.
```

### 4. (binary offset 0x4ffa34b)

```
A description of the changes that you are making to the file.
```

### 5. (binary offset 0x537c282)

```
A list of chunks to replace. It is best to provide multiple chunks for non-contiguous edits if possible. This must be a JSON array, not a string.
```

### 6. (binary offset 0x511c807)

```
A list of sed expressions to apply sequentially.
```

### 7. (binary offset 0x548e27d)

```
A measure of how important and relevant the edit is to the user's task. Use 'high' for edits directly addressing the main request or fixing critical issues, 'medium' for supporting changes, 'low' for minor improvements. enum=high,medium,low
```

### 8. (binary offset 0x54b567e)

```
A series of pixel coordinates defining the drag path. When this tool call is executed, the first waypoint will be clicked, then the mouse will be dragged to each subsequent waypoint in the provided order, and finally the mouse will be released at the last waypoint.
```

### 9. (binary offset 0x547a7f5)

```
A short, user-friendly summary of the task (1-2 sentences max). This will be displayed to the user in the UI instead of the full task description. Should be concise and describe the goal at a high level.
```

### 10. (binary offset 0x52d9b40)

```
A single contiguous chunk to replace. For non-contiguous edits, use the multi_replace_file_content tool instead.
```

### 11. (binary offset 0x501c9d5)

```
Absolute path to the .ipynb notebook file.
```

### 12. (binary offset 0x5368cf7)

```
Absolute path to the file or directory to delete. Must be either within an artifacts/ subdirectory of a Knowledge Item, or a top-level Knowledge Item directory.
```

### 13. (binary offset 0x5022a7f)

```
Absolute path to the node to edit, e.g /path/to/file
```

### 14. (binary offset 0x4f626b5)

```
Always set to true.
```

### 15. (binary offset 0x540577b)

```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```

### 16. (binary offset 0x52f2082)

```
An at most 20 character title describing the task in the imperative form. Will be displayed as the title of the tool in the step UI.
```

### 17. (binary offset 0x5522cbb)

```
An existing page ID which will be replaced with this new URL. You should provide a page_id in almost all cases. To open a new page, set this field to 'new_page'. IMPORTANT: Opening a new page should be extremely rare and only done if you are explicitly instructed to keep multiple pages open simultaneously. By default, always replace the most recently used page or any page not critical to your current task.
```

### 18. (binary offset 0x543e383)

```
Brief, user-facing explanation of what this change did. Focus on non-obvious rationale, design decisions, or important context. Don't just restate what the code does.
```

### 19. (binary offset 0x535491e)

```
Classification of the edit. Examples include "Continuing the user's work", "Bug fix", and "Documentation".
```

### 20. (binary offset 0x5001fe9)

```
Content of the prompt section.
```

### 21. (binary offset 0x517c50e)

```
Custom prompt sections to include in the subagent's system prompt.
```

### 22. (binary offset 0x5442ef9)

```
Detailed multi-line summary of the artifact file, after edits have been made. Summary does not need to mention the artifact name and should focus on the contents and purpose of the artifact.
```

### 23. (binary offset 0x54466b9)

```
Element name only (2-4 words, noun phrase). NOT an action sentence. Examples: 'Username Field', 'Submit Button', 'Login Link'. Never include verbs like 'clicking' or phrases like 'to focus'.
```

### 24. (binary offset 0x51efd73)

```
Full API URL (e.g., https://docs.googleapis.com/v1/documents/{documentId}:batchUpdate)
```

### 25. (binary offset 0x550090a)

```
Glob patterns to filter files found within the 'SearchPath', if 'SearchPath' is a directory. For example, '*.go' to only include Go files, or '!**/vendor/*' to exclude vendor directories. This is NOT for specifying the primary search directory; use 'SearchPath' for that. Leave empty if no glob filtering is needed or if 'SearchPath' is a single file.
```

### 26. (binary offset 0x504d045)

```
HTTP method (GET, POST, PUT, DELETE)
```

### 27. (binary offset 0x5231784)

```
Horizontal scroll delta in pixels. Positive values scroll to the right, negative values scroll to the left.
```

### 28. (binary offset 0x50d809f)

```
Human-readable description of the JavaScript to execute
```

### 29. (binary offset 0x523909c)

```
Human-readable description of what this subagent does and when it should be used.
```

### 30. (binary offset 0x4fbdaeb)

```
Human-readable title for the Knowledge Item
```

### 31. (binary offset 0x54e4048)

```
ID of a previous subagent to resume from. If provided, the agent will continue from the previous context. If empty, the subagent will start with an empty context. Use this to resume work from a cancelled subagent, or when the current task would benefit from the previous subagent's context.
```

### 32. (binary offset 0x4fd49f7)

```
ID of the command to get status for
```

### 33. (binary offset 0x5503e13)

```
If applicable, IDs of lint errors this edit aims to fix (they'll have been given in recent IDE feedback). If you believe the edit could fix lints, do specify lint IDs; if the edit is wholly unrelated, do not. A rule of thumb is, if your edit was influenced by lint feedback, include lint IDs. Exercise honest judgement here.
```

### 34. (binary offset 0x5177543)

```
If true, captures a screenshot of a specific element by index instead of the full viewport.
```

### 35. (binary offset 0x548e171)

```
If true, captures an extended screenshot starting from the current scroll position downward, up to 4000px or the end of page content, whichever is less. To capture content above or below this range, scroll first and then capture.
```

### 36. (binary offset 0x543b66f)

```
If true, multiple occurrences of 'targetContent' will be replaced by 'replacementContent' if they are found. Otherwise if multiple occurences are found, an error will be returned.
```

### 37. (binary offset 0x4fb373d)

```
If true, performs a case-insensitive search.
```

### 38. (binary offset 0x548031f)

```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```

### 39. (binary offset 0x4fb39f4)

```
If true, saves the screenshot as an artifact.
```

### 40. (binary offset 0x51e37d9)

```
If true, the user can select multiple options.
```

### 41. (binary offset 0x54dfae3)

```
If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality.
```

### 42. (binary offset 0x5001d74)

```
Index of the annotated DOM element to click on.
```

### 43. (binary offset 0x502f889)

```
Index of the annotated DOM element to input text into.
```

### 44. (binary offset 0x50c283f)

```
Index of the annotated DOM select element to select an option from.
```

### 45. (binary offset 0x551e852)

```
JavaScript code to execute on the page. The code must be a valid expression or series of statements that can be evaluated directly (e.g., 'document.querySelector(".button").click()' or '(() => { window.scrollTo(0, 1000); return true; })()'). Avoid bare return statements outside of functions. The code should not depend on external variables, modify page content, or perform non-navigation actions.
```

### 46. (binary offset 0x5052f28)

```
List of references related to this Knowledge Item
```

### 47. (binary offset 0x51d7495)

```
List of tool names available to the subagent. If empty, inherits default tools.
```

### 48. (binary offset 0x5163b45)

```
Markdown language for the code block, e.g 'python' or 'javascript'
```

### 49. (binary offset 0x501c95b)

```
Metadata for the artifact, required when IsArtifact is true.
```

### 50. (binary offset 0x52f7071)

```
Metadata updates if updating an artifact file, leave blank if not updating an artifact. Should be updated if the content is changing meaningfully.
```

### 51. (binary offset 0x550c22a)

```
Model to use for the subagent. 'inherit' (default) uses the calling agent's model. 'fast' uses a smaller, faster model suited for simple tasks like research lookups, file reading, or quick searches. 'heavy' uses a larger, more capable model suited for complex tasks requiring deep reasoning, large refactors, or multi-step planning.
```

### 52. (binary offset 0x50b8ecf)

```
Mouse button to press. Options are 'left', 'right', or 'middle'.
```

### 53. (binary offset 0x50c27c6)

```
Mouse button to release. Options are 'left', 'right', or 'middle'.
```

### 54. (binary offset 0x547e7b9)

```
Name of the browser recording that is created with the actions of the subagent. Should be all lowercase with underscores, describing what the recording contains. Maximum 3 words. Example: 'login_flow_demo'
```

### 55. (binary offset 0x53ea4dc)

```
Name of the generated image to save. Should be all lowercase with underscores, describing what the image contains. Maximum 3 words. Example: 'login_page_mockup'
```

### 56. (binary offset 0x558eeff)

```
Name of the key/key combination to simulate. Examples of keys are: "F1" - "F12", "Digit0"- "Digit9", "KeyA"- "KeyZ", "Backquote", "Minus", "Equal", "Backslash", "Backspace", "Tab", "Delete", "Escape", "ArrowDown", "End", "Enter", "Home", "Insert", "PageDown", "PageUp", "ArrowRight", "ArrowUp", etc. This tool also supports combinations with modifiers (e.g., Control+Enter). Examples of modifiers are: "Shift", "Control", "Alt", "Meta", "ShiftLeft", "ControlOrMeta". "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. Only specify one of Key or Text - use Key for keyboard shortcuts and special keys.
```

### 57. (binary offset 0x53f63f8)

```
Name of the screenshot to save. Should be all lowercase with underscores, describing what the screenshot contains. Maximum 3 words. Example: 'login_page_error'
```

### 58. (binary offset 0x4fc210b)

```
Name of the server to list available resources from.
```

### 59. (binary offset 0x4fa6abd)

```
Name of the server to read the resource from.
```

### 60. (binary offset 0x5581e5a)

```
Name of the task that the browser subagent is performing. This is the identifier that groups the subagent steps together, but should still be a human readable name. This should read like a title, should be properly capitalized and human readable, example: 'Navigating to Example Page'. Replace URLs or non-human-readable expressions like CSS selectors or long text with human-readable terms like 'URL' or 'Page' or 'Submit Button'. Be very sure this task name represents a reasonable chunk of work. It should almost never be the entire user request. This should be the very first argument.
```

### 61. (binary offset 0x517b8d5)

```
Number of characters to view. Make this as small as possible to avoid excessive memory usage.
```

### 62. (binary offset 0x54f2a5f)

```
Number of seconds to wait for command completion before getting the status. If the command completes before this duration, this tool call will return early. Set to 0 to get the status of the command immediately. If you are only interested in waiting for command completion, set to the max value, 300.
```

### 63. (binary offset 0x4fcf2b0)

```
One paragraph summary of the Knowledge Item
```

### 64. (binary offset 0x52d7908)

```
Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.
```

### 65. (binary offset 0x5491ee1)

```
Optional absolute paths to the images to use in generation. You can pass in images here if you would like to edit or combine images. You can pass in artifact images and any images in the file system. Note: you cannot pass in more than 3 images.
```

### 66. (binary offset 0x4ff3351)

```
Optional domain to recommend the search prioritize
```

### 67. (binary offset 0x53f615d)

```
Optional map of filename to content for r commands. Reference as '10r myname' in expressions. Use this for appending code blocks to avoid escaping issues.
```

### 68. (binary offset 0x50323c0)

```
Optional, Pattern to search for, supports glob format
```

### 69. (binary offset 0x502331f)

```
Optional, exclude files/directories that match the given glob patterns
```

### 70. (binary offset 0x5238286)

```
Optional, file extensions to include (without leading .), matching paths must match at least one of the included extensions
```

### 71. (binary offset 0x4f5959c)

```
Optional, maximum depth to search
```

### 72. (binary offset 0x54cda3c)

```
Optional, whether the full absolute path must match the glob pattern, default: only filename needs to match. Take care when specifying glob patterns with this flag on, e.g when FullPath is on, pattern '*.py' will not match to the file '/foo/bar.py', but pattern '**/*.py' will match.
```

### 73. (binary offset 0x51e3846)

```
Optional. Endline to view, 1-indexed as usual, inclusive. This value must be greater than or equal to StartLine.
```

### 74. (binary offset 0x53546d2)

```
Optional. Set to true only when reading a file to execute its instructions for a task. Set to false if the purpose is to edit, preview, or manage the file.
```

### 75. (binary offset 0x51dde3a)

```
Optional. Startline to view, 1-indexed as usual, inclusive. This value must be less than or equal to EndLine.
```

### 76. (binary offset 0x4ff9b14)

```
Path of the node within the file, e.g package.class.FunctionName
```

### 77. (binary offset 0x502f749)

```
Path to file to view. Must be an absolute path.
```

### 78. (binary offset 0x50dea29)

```
Path to list contents of, should be absolute path to a directory
```

### 79. (binary offset 0x4f294bc)

```
Request body JSON
```

### 80. (binary offset 0x547d1a5)

```
Set this to true to overwrite an existing file. WARNING: This will replace the entire file contents. Only use when you explicitly intend to overwrite. Otherwise, use a code edit tool to modify existing files.
```

### 81. (binary offset 0x502bf3c)

```
Set this to true when creating an artifact file.
```

### 82. (binary offset 0x550cf32)

```
Set to true if you believe that this code is safe to run WITHOUT user approval. JavaScript is unsafe if it may have some destructive side-effects. Set to true only if you are exremely confident it is safe. If you feel the JavaScript could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run potentially unsafe JavaScript.
```

### 83. (binary offset 0x557616b)

```
Set to true if you believe that this command is safe to run WITHOUT user approval. A command is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the command could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe command.
```

### 84. (binary offset 0x556142f)

```
Set to true if you believe that this command is safe to run WITHOUT user approval. An input is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the input could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe input.
```

### 85. (binary offset 0x4ff1462)

```
Set to true to request user feedback on this artifact.
```

### 86. (binary offset 0x54f07d8)

```
Text to type sequentially, character by character. Use this for typing regular text content like letters, numbers, and basic symbols. Each character will be typed individually in sequence. Only specify one of Key or Text - use Text for typing regular content, not for keyboard shortcuts or special keys like F1, Control+C, etc.
```

### 87. (binary offset 0x53ea699)

```
The 0-based index of the cell to operate on. Required for 'get', 'update', and 'delete' actions. Optional for 'add' (inserts at index, appends if omitted).
```

### 88. (binary offset 0x50d7b2e)

```
The ID of the message to read. Required when Action is 'read'.
```

### 89. (binary offset 0x4fc4d67)

```
The URL to open in the user's browser.
```

### 90. (binary offset 0x505ce1b)

```
The absolute path to the file to edit.
```

### 91. (binary offset 0x54b8190)

```
The action to perform: 'list' (list all cells), 'get' (get cell content), 'add' (add new cell), 'update' (update cell content), 'delete' (delete cell), 'create' (create new notebook).
```

### 92. (binary offset 0x53524dc)

```
The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message).
```

### 93. (binary offset 0x548d158)

```
The action to perform: 'list' (list all running tasks), 'kill' (cancel the task), 'status' (check the task status and log URI), 'send_input' (send input to a running task).
```

### 94. (binary offset 0x50609ca)

```
The cell content. Required for 'add' and 'update' actions.
```

### 95. (binary offset 0x50684e9)

```
The code contents to write to the file.
```

### 96. (binary offset 0x520492b)

```
The command ID from a previous run_command call. This is returned in the run_command output.
```

### 97. (binary offset 0x5152ce5)

```
The content to replace the target content with.
```

### 98. (binary offset 0x502f6de)

```
The current working directory for the command
```

### 99. (binary offset 0x4fd69c5)

```
The directory to search within
```

### 100. (binary offset 0x54ccb61)

```
The ending line number of the chunk (1-indexed). Should be at or after the last line containing the target content. Must satisfy StartLine <= EndLine <= number of lines in the file. The target content is searched for within the [StartLine, EndLine] range.
```

### 101. (binary offset 0x50bed78)

```
The exact command line string to execute.
```

### 102. (binary offset 0x54d0eb9)

```
The exact string to be replaced. This must be the exact character-sequence to be replaced, including whitespace. Be very careful to include any leading whitespace otherwise this will not work at all. This must be a unique substring within the file, or else it will error.
```

### 103. (binary offset 0x521c97f)

```
The index of the element to capture (required if CaptureByElementIndex is true). Get the index using browser_get_dom.
```

### 104. (binary offset 0x540617b)

```
The input to send to the command's stdin. Include newline characters (the literal character, not the escape sequence) if needed to submit commands. Exactly one of input and terminate must be specified.
```

### 105. (binary offset 0x50d0187)

```
The input to send to the task. Required when Action is 'send_input'.
```

### 106. (binary offset 0x503242b)

```
The list of questions to ask.
```

### 107. (binary offset 0x4f8dea8)

```
The message content.
```

### 108. (binary offset 0x50b8f47)

```
The page_id of the browser page containing the dropdown element.
```

### 109. (binary offset 0x4ffa5b4)

```
The page_id of the browser page to click on.
```

### 110. (binary offset 0x5058597)

```
The page_id of the browser page to get network request from.
```

### 111. (binary offset 0x50207ed)

```
The page_id of the browser page to input text on.
```

### 112. (binary offset 0x505d1ac)

```
The page_id of the browser page to list network requests for.
```

### 113. (binary offset 0x51d6dc4)

```
The path to search. This can be a directory or a file. This is a required parameter.
```

### 114. (binary offset 0x52e28b8)

```
The question to ask the user. Do NOT add 'select all that apply' or similar text to the question title.
```

### 115. (binary offset 0x514aa4d)

```
The recipient ID to send the message to, e.g. a subagent conversation ID.
```

### 116. (binary offset 0x52316eb)

```
The request ID to retrieve details for. This ID can be obtained from the list_network_requests tool.
```

### 117. (binary offset 0x54f2bb5)

```
The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'.
```

### 118. (binary offset 0x50270e4)

```
The search term or pattern to look for within files.
```

### 119. (binary offset 0x54b16d4)

```
The starting line number of the chunk (1-indexed). Should be at or before the first line containing the target content. Must satisfy 1 <= StartLine <= EndLine. The target content is searched for within the [StartLine, EndLine] range.
```

### 120. (binary offset 0x501c903)

```
The target file to create and write code to.
```

### 121. (binary offset 0x51da192)

```
The target file to modify. Always specify the target file as the very first argument.
```

### 122. (binary offset 0x5177061)

```
The task ID to manage. Required when Action is 'kill', 'status', or 'send_input'.
```

### 123. (binary offset 0x5379424)

```
The text for each option, formatted as the user's response. Must have at least 2 options. Do NOT add an 'Other' option to questions.
```

### 124. (binary offset 0x4ff0d9d)

```
The text prompt to generate an image for.
```

### 125. (binary offset 0x4fbddc8)

```
The text to input into the element.
```

### 126. (binary offset 0x5164aa5)

```
The type of cell: 'code', 'markdown', or 'raw'. Required for 'add' action.
```

### 127. (binary offset 0x505349d)

```
The value or text of the option to select from the dropdown.
```

### 128. (binary offset 0x5144f8f)

```
The window contents height in display independent pixels. Only used when WindowState is 'normal'.
```

### 129. (binary offset 0x513bac4)

```
The window contents width in display independent pixels. Only used when WindowState is 'normal'.
```

### 130. (binary offset 0x559244c)

```
The window state to set. Options: 'normal' (resizable window with specified width/height), 'minimized' (window minimized to taskbar), 'maximized' (window is full screen but shows taskbar), 'fullscreen' (window fills entire screen and hides taskbar). Width and Height are only used when WindowState is 'normal'. Generally you should prefer 'maximized'. If the user asks to make the window smaller or a particular size, use 'normal'. When resetting the window size, prefer 'maximized' instead of 'normal' with specific width/height values. 'minimized' and 'fullscreen' are somewhat jarring, so you should only use these when the user explicitly asks for it.
```

### 131. (binary offset 0x557a5bc)

```
This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms). Keep the value as small as possible, with a maximum of 10000ms.
```

### 132. (binary offset 0x4fede0b)

```
Title of the prompt section.
```

### 133. (binary offset 0x4fd5034)

```
Type name of the subagent to invoke.
```

### 134. (binary offset 0x5368c83)

```
Type of artifact: 'implementation_plan', 'walkthrough', 'task', or 'other'.
```

### 135. (binary offset 0x536b084)

```
Type of click to perform: 'left', 'right', or 'double'. If not specified or left empty, a left click will be performed.
```

### 136. (binary offset 0x4fe9dc7)

```
Type of reference (e.g., file, conversation_id, url)
```

### 137. (binary offset 0x4fbb1cf)

```
URL to read content from
```

### 138. (binary offset 0x4f4c426)

```
Unique identifier for the resource.
```

### 139. (binary offset 0x51534bd)

```
Unique name for the subagent. Used to invoke it via invoke_subagent.
```

### 140. (binary offset 0x50d7ac0)

```
User-facing explanation of what this call does
```

### 141. (binary offset 0x4f51f59)

```
Value of the reference
```

### 142. (binary offset 0x517c090)

```
Vertical scroll delta in pixels. Positive values scroll down, negative values scroll up.
```

### 143. (binary offset 0x5004a5d)

```
Whether to clear existing text before inputting. Default is false.
```

### 144. (binary offset 0x501b1c5)

```
Whether to press Enter after inputting the text. Default is false.
```

### 145. (binary offset 0x50d00f8)

```
Whether to terminate the command. Exactly one of input and terminate must be specified.
```

### 146. (binary offset 0x543c2b8)

```
Workspace mode for the subagent. 'inherit' (default) shares the parent's workspace. 'branch' creates a new workspace branched from the parent (CitC clone or git worktree). If omitted, defaults to 'inherit'.
```

### 147. (binary offset 0x5368a91)

```
X coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 148. (binary offset 0x536595b)

```
X coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 149. (binary offset 0x52b3717)

```
X coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions.
```

### 150. (binary offset 0x5368b5a)

```
Y coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 151. (binary offset 0x5365893)

```
Y coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.
```

### 152. (binary offset 0x52b37c3)

```
Y coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions.
```

### 153. (binary offset 0x540929f)

```
description=A standard cron expression (5 fields: minute hour day-of-month month day-of-week). Use for recurring schedules. Mutually exclusive with DurationSeconds. Example: '*/5 * * * *' for every 5 minutes.
```

### 154. (binary offset 0x4faf027)

```
description=Arguments to pass to the command
```

### 155. (binary offset 0x51e7149)

```
description=Description of what the sidecar does. Make sure this is accurate and up-to-date.
```

### 156. (binary offset 0x52efec3)

```
description=Optional. Maximum number of times the cron schedule will fire before stopping. Only applicable when CronExpression is set. Defaults to unlimited.
```

### 157. (binary offset 0x5234237)

```
description=Restart policy for the sidecar. Options: always, on-failure, never. Defaults to always.
```

### 158. (binary offset 0x4fb36ed)

```
description=The command to execute (e.g. python3)
```

### 159. (binary offset 0x52d72ac)

```
description=The message content to include in the notification when the timer fires or cron triggers. This is sent to the agent as a high-priority message.
```

### 160. (binary offset 0x51e71c5)

```
description=The number of seconds to wait (max 900). Use for one-shot timers. Mutually exclusive with CronExpression.
```

### 161. (binary offset 0x5049bd6)

```
description=Whether the sidecar is disabled. Defaults to false.
```

### 162. (binary offset 0x505d224)

```
direction of the scroll. Options are left, right, up, down
```

### 163. (binary offset 0x54f3306)

```
if true, scroll by the element with the given index; the scroll is performed via executing a mouseWheel event on the pixel at the middle of the element.. Otherwise scroll the entire page; in this case, if 0 pixels are scrolled, the page is likely not scrollable and the tool call should be retried by scrolling a DOM element.
```

### 164. (binary offset 0x53560d2)

```
if true, scroll in the direction to the end of the selected element/page. For example, if direction is down, would scroll to the bottom of the element/page.
```

### 165. (binary offset 0x4fd6adf)

```
index of the element to scroll on
```

### 166. (binary offset 0x52d78f2)

```
optional
```

### 167. (binary offset 0x5036967)

```
page_id of the Browser page to capture a screenshot of.
```

### 168. (binary offset 0x50368f8)

```
page_id of the Browser page to capture console logs of.
```

### 169. (binary offset 0x504503f)

```
page_id of the Browser page to execute the JavaScript on
```

### 170. (binary offset 0x5023683)

```
page_id of the Browser page to get the DOM tree of
```

### 171. (binary offset 0x5044fcf)

```
page_id of the Browser page to move the mouse cursor to.
```

### 172. (binary offset 0x4fd4b56)

```
page_id of the Browser page to perform the drag operation on
```

### 173. (binary offset 0x5044f5f)

```
page_id of the Browser page to press the mouse button on
```

### 174. (binary offset 0x4fc4dc5)

```
page_id of the Browser page to read
```

### 175. (binary offset 0x4ffdcb9)

```
page_id of the Browser page to refresh/reload
```

### 176. (binary offset 0x504d587)

```
page_id of the Browser page to release the mouse button on
```

### 177. (binary offset 0x4fd4c28)

```
page_id of the Browser page to resize.
```

### 178. (binary offset 0x4fed97f)

```
page_id of the Browser page to scroll on
```

### 179. (binary offset 0x4fd4bca)

```
page_id of the Browser page to scroll.
```

### 180. (binary offset 0x503272f)

```
page_id of the Browser page to simulate a key press on
```

### 181. (binary offset 0x4e8efbd)

```
required
```

### 182. (binary offset 0x5368c2e)

```
required,enum=implementation_plan,enum=walkthrough,enum=task,enum=other
```

### 183. (binary offset 0x54b813a)

```
required,enum=list,enum=get,enum=add,enum=update,enum=delete,enum=create
```

### 184. (binary offset 0x5020851)

```
x-coordinate of the pixel to move the mouse cursor to.
```

### 185. (binary offset 0x50208ba)

```
y-coordinate of the pixel to move the mouse cursor to.
```

