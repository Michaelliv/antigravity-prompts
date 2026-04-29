# Byte-exact field index

**179** verbatim `(field_name, struct-tag)` records recovered from Go reflect-name tables in the Antigravity language-server binary. Each row is a real field in some tool's argument struct, with its raw Go reflect tag string exactly as the compiler emitted it. These tags are what the language server feeds to jsonschema generation when it builds tool descriptors for the model.

## Why this is unattributed

Cortex-step proto messages (`CortexStep<X>` in `cortex.proto`) describe the *outcome state* of a tool call — what gets stored in the trajectory — not the JSON-schema *input args* the model fills in. The actual arg structs (e.g. `tools.runCommandArgs`, `notebook.editNotebookArgs`) live in a separate Go object hierarchy. They share neither field names nor object identity with the proto messages, so static signals (proto field-name match, rodata proximity to a `CortexStep<X>` token) routinely yield false positives. Earlier attempts to auto-attribute produced confidently wrong rows like *"Mouse button to release."* assigned to `CortexStepCaptureBrowserConsoleLogs`. The honest move is to present the recovered records flat. Attribution requires reading the descriptive text and is best done by a human or LLM with the tool's purpose in mind.

## Records

| field | tag | binary offset |
|---|---|---:|
| `AbsolutePath` | `jsonschema:"required" jsonschema_description:"Path to file to view. Must be an absolute path."` | 0x502f724 |
| `Action` | `jsonschema:"required,enum=list,enum=get,enum=add,enum=update,enum=delete,enum=create" jsonschema_description:"The action to perform: 'list' (list all cells), 'get' (get cell content), 'add' (add new cell), 'update' (update cell content), 'delete' (delete cell), 'create' (create new notebook)."` | 0x54b8130 |
| `Action` | `jsonschema:"required,enum=list,enum=kill,enum=status,enum=send_input" jsonschema_description:"The action to perform: 'list' (list all running tasks), 'kill' (cancel the task), 'status' (check the task status and log URI), 'send_input' (send input to a running task)."` | 0x548d108 |
| `Action` | `jsonschema:"required,enum=list,enum=read" jsonschema_description:"The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message)."` | 0x53524a8 |
| `AllowMultiple` | `jsonschema:"required" jsonschema_description:"If true, multiple occurrences of 'targetContent' will be replaced by 'replacementContent' if they are found. Otherwise if multiple occurences are found, an error will be returned."` | 0x543b648 |
| `ArtifactMetadata` | `jsonschema_description:"Metadata for the artifact, required when IsArtifact is true."` | 0x501c948 |
| `ArtifactMetadata` | `jsonschema_description:"Metadata updates if updating an artifact file, leave blank if not updating an artifact. Should be updated if the content is changing meaningfully."` | 0x52f705d |
| `ArtifactType` | `jsonschema:"required,enum=implementation_plan,enum=walkthrough,enum=task,enum=other" jsonschema_description:"Type of artifact: 'implementation_plan', 'walkthrough', 'task', or 'other'."` | 0x5368c1e |
| `Body` | `json:"Body" jsonschema_description:"Request body JSON"` | 0x4f294a9 |
| `Button` | `jsonschema:"required" jsonschema_description:"Mouse button to press. Options are 'left', 'right', or 'middle'."` | 0x50b8eb0 |
| `Button` | `jsonschema:"required" jsonschema_description:"Mouse button to release. Options are 'left', 'right', or 'middle'."` | 0x50c27a7 |
| `CaptureBeyondViewport` | `jsonschema_description:"If true, captures an extended screenshot starting from the current scroll position downward, up to 4000px or the end of page content, whichever is less. To capture content above or below this range, scroll first and then capture."` | 0x548e158 |
| `CaptureByElementIndex` | `jsonschema_description:"If true, captures a screenshot of a specific element by index instead of the full viewport."` | 0x517752b |
| `CaseInsensitive` | `jsonschema_description:"If true, performs a case-insensitive search."` | 0x4fb372b |
| `CellIndex` | `json:"CellIndex,omitempty" jsonschema_description:"The 0-based index of the cell to operate on. Required for 'get', 'update', and 'delete' actions. Optional for 'add' (inserts at index, appends if omitted)."` | 0x53ea671 |
| `CellType` | `json:"CellType,omitempty" jsonschema_description:"The type of cell: 'code', 'markdown', or 'raw'. Required for 'add' action."` | 0x5164a80 |
| `Classification` | `jsonschema_description:"Classification of the edit. Examples include \"Continuing the user's work\", \"Bug fix\", and \"Documentation\"." jsonschema_extras:"\"type\":\"string\""` | 0x535490c |
| `ClearText` | `jsonschema_description:"Whether to clear existing text before inputting. Default is false."` | 0x5004a51 |
| `ClickType` | `jsonschema_description:"Type of click to perform: 'left', 'right', or 'double'. If not specified or left empty, a left click will be performed." jsonschema:"enum=left,enum=right,enum=double"` | 0x536b077 |
| `CodeContent` | `jsonschema:"required" jsonschema_description:"The code contents to write to the file." attribution:"true"` | 0x50684c5 |
| `CodeMarkdownLanguage` | `jsonschema:"required" jsonschema_description:"Markdown language for the code block, e.g 'python' or 'javascript'"` | 0x5163b18 |
| `Command` | `json:"command" jsonschema:"description=The command to execute (e.g. python3)"` | 0x4fb36d4 |
| `CommandId` | `jsonschema:"required" jsonschema_description:"ID of the command to get status for"` | 0x4fd49d5 |
| `CommandId` | `jsonschema:"required" jsonschema_description:"The command ID from a previous run_command call. This is returned in the run_command output."` | 0x5204908 |
| `CommandLine` | `json:"CommandLine" jsonschema:"required" jsonschema_description:"The exact command line string to execute."` | 0x50bed41 |
| `Content` | `json:"Content,omitempty" jsonschema_description:"The cell content. Required for 'add' and 'update' actions."` | 0x50609a7 |
| `Content` | `json:"content" jsonschema:"required" jsonschema_description:"Content of the prompt section."` | 0x5001fba |
| `CookieDeprecationMetadataIssueDetails` | `json:"cookieDeprecationMetadataIssueDetails,omitempty"` | 0x4fd4f57 |
| `Cwd` | `jsonschema:"required" json:"Cwd" jsonschema_description:"The current working directory for the command"` | 0x502f6b7 |
| `Description` | `json:"description" jsonschema:"required" jsonschema_description:"Human-readable description of what this subagent does and when it should be used."` | 0x5239064 |
| `Description` | `jsonschema:"required" json:"Description" jsonschema_description:"Brief, user-facing explanation of what this change did. Focus on non-obvious rationale, design decisions, or important context. Don't just restate what the code does."` | 0x543e34b |
| `Description` | `jsonschema:"required" json:"Description" jsonschema_description:"User-facing explanation of what this call does"` | 0x50d7a89 |
| `Description` | `jsonschema:"required" jsonschema_description:"Element name only (2-4 words, noun phrase). NOT an action sentence. Examples: 'Username Field', 'Submit Button', 'Login Link'. Never include verbs like 'clicking' or phrases like 'to focus'."` | 0x5446694 |
| `Direction` | `jsonschema:"required" jsonschema_description:"direction of the scroll. Options are left, right, up, down"` | 0x505d202 |
| `DirectoryPath` | `jsonschema:"required" jsonschema_description:"Path to list contents of, should be absolute path to a directory"` | 0x50dea03 |
| `DisabledByHoldbackPrefetchSpeculationRules` | `json:"disabledByHoldbackPrefetchSpeculationRules"` | 0x4fd4fb5 |
| `Domain` | `json:"domain" jsonschema_description:"Optional domain to recommend the search prioritize"` | 0x4ff333a |
| `Dx` | `jsonschema:"required" jsonschema_description:"Horizontal scroll delta in pixels. Positive values scroll to the right, negative values scroll to the left."` | 0x5231768 |
| `Dy` | `jsonschema:"required" jsonschema_description:"Vertical scroll delta in pixels. Positive values scroll down, negative values scroll up."` | 0x517c074 |
| `ElementIndex` | `jsonschema:"required" jsonschema_description:"index of the element to scroll on"` | 0x4fd6aba |
| `ElementIndex` | `jsonschema_description:"The index of the element to capture (required if CaptureByElementIndex is true). Get the index using browser_get_dom."` | 0x521c96f |
| `EndLine` | `jsonschema:"required" jsonschema_description:"The ending line number of the chunk (1-indexed). Should be at or after the last line containing the target content. Must satisfy StartLine <= EndLine <= number of lines in the file. The target content is searched for within the [StartLine, EndLine] range."` | 0x54ccb40 |
| `EndLine` | `jsonschema_description:"Optional. Endline to view, 1-indexed as usual, inclusive. This value must be greater than or equal to StartLine."` | 0x51e383b |
| `Excludes` | `jsonschema_description:"Optional, exclude files/directories that match the given glob patterns"` | 0x5023314 |
| `Expressions` | `json:"expressions" jsonschema:"required" jsonschema_description:"A list of sed expressions to apply sequentially."` | 0x511c7d0 |
| `Extensions` | `jsonschema_description:"Optional, file extensions to include (without leading .), matching paths must match at least one of the included extensions"` | 0x5238278 |
| `File` | `json:"File,omitempty" jsonschema_description:"Absolute path to the node to edit, e.g /path/to/file"` | 0x5022a62 |
| `FileContent` | `json:"file_content,omitempty" jsonschema_description:"Optional map of filename to content for r commands. Reference as '10r myname' in expressions. Use this for appending code blocks to avoid escaping issues."` | 0x53f6130 |
| `FullPath` | `jsonschema_description:"Optional, whether the full absolute path must match the glob pattern, default: only filename needs to match. Take care when specifying glob patterns with this flag on, e.g when FullPath is on, pattern '*.py' will not match to the file '/foo/bar.py', but pattern '**/*.py' will match."` | 0x54cda30 |
| `Height` | `jsonschema_description:"The window contents height in display independent pixels. Only used when WindowState is 'normal'."` | 0x5144f86 |
| `HttpMethod` | `jsonschema:"required" json:"HttpMethod" jsonschema_description:"HTTP method (GET, POST, PUT, DELETE)"` | 0x504d010 |
| `ImageName` | `jsonschema:"required" jsonschema_description:"Name of the generated image to save. Should be all lowercase with underscores, describing what the image contains. Maximum 3 words. Example: 'login_page_mockup'"` | 0x53ea4b9 |
| `ImagePaths` | `jsonschema_description:"Optional absolute paths to the images to use in generation. You can pass in images here if you would like to edit or combine images. You can pass in artifact images and any images in the file system. Note: you cannot pass in more than 3 images."` | 0x5491ed3 |
| `Importance` | `jsonschema_description:"A measure of how important and relevant the edit is to the user's task. Use 'high' for edits directly addressing the main request or fixing critical issues, 'medium' for supporting changes, 'low' for minor improvements. enum=high,medium,low"` | 0x548e26f |
| `IncludePreservedRequests` | `jsonschema_description:"Always set to true."` | 0x4f6269a |
| `Includes` | `jsonschema_description:"Glob patterns to filter files found within the 'SearchPath', if 'SearchPath' is a directory. For example, '*.go' to only include Go files, or '!**/vendor/*' to exclude vendor directories. This is NOT for specifying the primary search directory; use 'SearchPath' for that. Leave empty if no glob filtering is needed or if 'SearchPath' is a single file."` | 0x55008fe |
| `Index` | `jsonschema:"required" jsonschema_description:"Index of the annotated DOM element to click on."` | 0x5001d56 |
| `Index` | `jsonschema:"required" jsonschema_description:"Index of the annotated DOM element to input text into."` | 0x502f86b |
| `Index` | `jsonschema:"required" jsonschema_description:"Index of the annotated DOM select element to select an option from."` | 0x50c2821 |
| `Input` | `json:"Input,omitempty" jsonschema_description:"The input to send to the task. Required when Action is 'send_input'."` | 0x50d0168 |
| `Input` | `jsonschema_description:"The input to send to the command's stdin. Include newline characters (the literal character, not the escape sequence) if needed to submit commands. Exactly one of input and terminate must be specified."` | 0x5406172 |
| `Instruction` | `jsonschema:"required" jsonschema_description:"A description of the changes that you are making to the file."` | 0x50c2d5f |
| `Instruction` | `jsonschema_description:"A description of the changes that you are making to the file."` | 0x4ffa33d |
| `IsArtifact` | `jsonschema:"required" jsonschema_description:"Set this to true when creating an artifact file."` | 0x502bf19 |
| `IsMultiSelect` | `json:"is_multi_select,omitempty" jsonschema_description:"If true, the user can select multiple options." jsonschema_default:"false"` | 0x51e37a7 |
| `IsRegex` | `jsonschema_description:"If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality."` | 0x54dfad8 |
| `IsSkillFile` | `jsonschema_description:"Optional. Set to true only when reading a file to execute its instructions for a task. Set to false if the purpose is to edit, preview, or manage the file."` | 0x53546c3 |
| `JavaScriptDescription` | `jsonschema:"required" jsonschema_description:"Human-readable description of the JavaScript to execute"` | 0x50d8071 |
| `JavaScriptSource` | `jsonschema:"required" jsonschema_description:"JavaScript code to execute on the page. The code must be a valid expression or series of statements that can be evaluated directly (e.g., 'document.querySelector(\".button\").click()' or '(() => { window.scrollTo(0, 1000); return true; })()'). Avoid bare return statements outside of functions. The code should not depend on external variables, modify page content, or perform non-navigation actions."` | 0x551e828 |
| `Key` | `jsonschema_description:"Name of the key/key combination to simulate. Examples of keys are: \"F1\" - \"F12\", \"Digit0\"- \"Digit9\", \"KeyA\"- \"KeyZ\", \"Backquote\", \"Minus\", \"Equal\", \"Backslash\", \"Backspace\", \"Tab\", \"Delete\", \"Escape\", \"ArrowDown\", \"End\", \"Enter\", \"Home\", \"Insert\", \"PageDown\", \"PageUp\", \"ArrowRight\", \"ArrowUp\", etc. This tool also supports combinations with modifiers (e.g., Control+Enter). Examples of modifiers are: \"Shift\", \"Control\", \"Alt\", \"Meta\", \"ShiftLeft\", \"ControlOrMeta\". \"ControlOrMeta\" resolves to \"Control\" on Windows and Linux and to \"Meta\" on macOS. Only specify one of Key or Text - use Key for keyboard shortcuts and special keys."` | 0x558eef8 |
| `MatchPerLine` | `jsonschema_description:"If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l')."` | 0x548030f |
| `MaxDepth` | `jsonschema_description:"Optional, maximum depth to search"` | 0x4f59591 |
| `MediaPaths` | `jsonschema:"optional" jsonschema_description:"Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files."` | 0x52d78e4 |
| `Message` | `jsonschema:"required" jsonschema_description:"The message content."` | 0x4f8de88 |
| `MessageID` | `json:"MessageID,omitempty" jsonschema_description:"The ID of the message to read. Required when Action is 'read'."` | 0x50d7b07 |
| `Model` | `jsonschema_description:"Model to use for the subagent. 'inherit' (default) uses the calling agent's model. 'fast' uses a smaller, faster model suited for simple tasks like research lookups, file reading, or quick searches. 'heavy' uses a larger, more capable model suited for complex tasks requiring deep reasoning, large refactors, or multi-step planning." jsonschema:"enum=inherit,enum=fast,enum=heavy"` | 0x550c221 |
| `ModelTrainingExpectedTotalIteration` | `json:"modelTrainingExpectedTotalIteration,omitempty,string"` | 0x4ff14b1 |
| `Name` | `json:"name" jsonschema:"required" jsonschema_description:"Unique name for the subagent. Used to invoke it via invoke_subagent."` | 0x5153494 |
| `NodePath` | `jsonschema_description:"Path of the node within the file, e.g package.class.FunctionName"` | 0x4ff9b09 |
| `NotebookPath` | `jsonschema:"required" jsonschema_description:"Absolute path to the .ipynb notebook file."` | 0x501c9b0 |
| `Options` | `json:"options" jsonschema_description:"The text for each option, formatted as the user's response. Must have at least 2 options. Do NOT add an 'Other' option to questions." jsonschema_required:"true"` | 0x537940a |
| `OutputCharacterCount` | `jsonschema_description:"Number of characters to view. Make this as small as possible to avoid excessive memory usage."` | 0x517b8be |
| `Overwrite` | `jsonschema:"required" jsonschema_description:"Set this to true to overwrite an existing file. WARNING: This will replace the entire file contents. Only use when you explicitly intend to overwrite. Otherwise, use a code edit tool to modify existing files."` | 0x547d182 |
| `PageID` | `jsonschema:"required" jsonschema_description:"The page_id of the browser page to click on."` | 0x4ffa5f9 |
| `PageID` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to capture a screenshot of."` | 0x5036948 |
| `PageID` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to resize."` | 0x4fd4c09 |
| `PageID` | `jsonschema_description:"page_id of the Browser page to perform the drag operation on"` | 0x4fd4b4d |
| `PageId` | `jsonschema:"required" jsonschema_description:"The page_id of the browser page containing the dropdown element."` | 0x50b8f28 |
| `PageId` | `jsonschema:"required" jsonschema_description:"The page_id of the browser page to click on."` | 0x4ffa595 |
| `PageId` | `jsonschema:"required" jsonschema_description:"The page_id of the browser page to get network request from."` | 0x5058578 |
| `PageId` | `jsonschema:"required" jsonschema_description:"The page_id of the browser page to input text on."` | 0x50207ce |
| `PageId` | `jsonschema:"required" jsonschema_description:"The page_id of the browser page to list network requests for."` | 0x505d18d |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to capture console logs of."` | 0x50368d9 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to execute the JavaScript on"` | 0x5045020 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to get the DOM tree of"` | 0x5023664 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to move the mouse cursor to."` | 0x5044fb0 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to press the mouse button on"` | 0x5044f40 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to read"` | 0x4fc4da6 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to refresh/reload"` | 0x4ffdc9a |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to release the mouse button on"` | 0x504d568 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to scroll on"` | 0x4fed960 |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to scroll."` | 0x4fd4bab |
| `PageId` | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to simulate a key press on"` | 0x5032710 |
| `PageIdToReplace` | `jsonschema:"required" jsonschema_description:"An existing page ID which will be replaced with this new URL. You should provide a page_id in almost all cases. To open a new page, set this field to 'new_page'. IMPORTANT: Opening a new page should be extremely rare and only done if you are explicitly instructed to keep multiple pages open simultaneously. By default, always replace the most recently used page or any page not critical to your current task."` | 0x5522c92 |
| `PathToDelete` | `jsonschema_description:"Absolute path to the file or directory to delete. Must be either within an artifacts/ subdirectory of a Knowledge Item, or a top-level Knowledge Item directory."` | 0x5368ce7 |
| `Pattern` | `jsonschema:"required" jsonschema_description:"Optional, Pattern to search for, supports glob format"` | 0x50323a0 |
| `PressEnter` | `jsonschema_description:"Whether to press Enter after inputting the text. Default is false."` | 0x501b1b8 |
| `Prompt` | `jsonschema:"required" jsonschema_description:"A clear, actionable task description for the subagent. Be specific about what the subagent should do and what information it should return."` | 0x5356187 |
| `Prompt` | `jsonschema:"required" jsonschema_description:"The text prompt to generate an image for."` | 0x4ff0d7e |
| `PromptSections` | `json:"prompt_sections,omitempty" jsonschema_description:"Custom prompt sections to include in the subagent's system prompt."` | 0x517c4dc |
| `Query` | `jsonschema:"required" jsonschema_description:"The search term or pattern to look for within files."` | 0x50270c6 |
| `Question` | `json:"question" jsonschema_description:"The question to ask the user. Do NOT add 'select all that apply' or similar text to the question title." jsonschema_required:"true"` | 0x52e289c |
| `Questions` | `json:"questions" jsonschema_description:"The list of questions to ask." jsonschema_required:"true"` | 0x503240e |
| `Recipient` | `jsonschema:"required" jsonschema_description:"The recipient ID to send the message to, e.g. a subagent conversation ID."` | 0x514aa2b |
| `RecordingName` | `jsonschema:"required" jsonschema_description:"Name of the browser recording that is created with the actions of the subagent. Should be all lowercase with underscores, describing what the recording contains. Maximum 3 words. Example: 'login_flow_demo'"` | 0x547e792 |
| `References` | `jsonschema_description:"List of references related to this Knowledge Item" json:"references,omitempty"` | 0x5052f1b |
| `ReplacementChunks` | `jsonschema:"required" jsonschema_description:"A list of chunks to replace. It is best to provide multiple chunks for non-contiguous edits if possible. This must be a JSON array, not a string."` | 0x537c257 |
| `ReplacementContent` | `jsonschema:"required" jsonschema_description:"The content to replace the target content with." attribution:"true"` | 0x5152cba |
| `RequestFeedback` | `jsonschema_description:"Set to true to request user feedback on this artifact."` | 0x4ff1450 |
| `RequestId` | `jsonschema:"required" jsonschema_description:"The request ID to retrieve details for. This ID can be obtained from the list_network_requests tool."` | 0x52316c8 |
| `ResourceTypes` | `jsonschema_description:"The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'."` | 0x54f2ba4 |
| `ReusedSubagentId` | `jsonschema:"optional" jsonschema_description:"ID of a previous subagent to resume from. If provided, the agent will continue from the previous context. If empty, the subagent will start with an empty context. Use this to resume work from a cancelled subagent, or when the current task would benefit from the previous subagent's context."` | 0x54e401e |
| `Role` | `jsonschema:"required" jsonschema_description:"A 2-5 word description of the subagent's role. Should read similar to a job title, e.g. 'Codebase Researcher', 'Database Debugger', etc. Should also be detailed enough to distinguish between different subagents who might share similar purposes."` | 0x54b4bdc |
| `SafeToAutoRun` | `jsonschema:"required" json:"SafeToAutoRun" jsonschema_description:"Set to true if you believe that this command is safe to run WITHOUT user approval. A command is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the command could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe command."` | 0x557612f |
| `SafeToAutoRun` | `jsonschema:"required" jsonschema_description:"Set to true if you believe that this command is safe to run WITHOUT user approval. An input is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the input could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe input."` | 0x5561408 |
| `SafeToAutoRun` | `jsonschema_description:"Set to true if you believe that this code is safe to run WITHOUT user approval. JavaScript is unsafe if it may have some destructive side-effects. Set to true only if you are exremely confident it is safe. If you feel the JavaScript could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run potentially unsafe JavaScript."` | 0x550cf21 |
| `SaveScreenshot` | `jsonschema_description:"If true, saves the screenshot as an artifact."` | 0x4fb39e3 |
| `ScreenshotName` | `jsonschema:"required" jsonschema_description:"Name of the screenshot to save. Should be all lowercase with underscores, describing what the screenshot contains. Maximum 3 words. Example: 'login_page_error'"` | 0x53f63d0 |
| `ScrollByElementIndex` | `jsonschema_description:"if true, scroll by the element with the given index; the scroll is performed via executing a mouseWheel event on the pixel at the middle of the element.. Otherwise scroll the entire page; in this case, if 0 pixels are scrolled, the page is likely not scrollable and the tool call should be retried by scrolling a DOM element."` | 0x54f32ee |
| `ScrollToEnd` | `jsonschema_description:"if true, scroll in the direction to the end of the selected element/page. For example, if direction is down, would scroll to the bottom of the element/page."` | 0x53560c3 |
| `SearchDirectory` | `jsonschema:"required" jsonschema_description:"The directory to search within"` | 0x4fd699d |
| `SearchPath` | `jsonschema:"required" jsonschema_description:"The path to search. This can be a directory or a file. This is a required parameter."` | 0x51d6da0 |
| `ServerName` | `jsonschema_description:"Name of the server to list available resources from."` | 0x4fc20fe |
| `ServerName` | `jsonschema_description:"Name of the server to read the resource from."` | 0x4fa6ab0 |
| `ServerUrl` | `json:"serverUrl,omitempty" yaml:"serverUrl,omitempty" mapstructure:"serverUrl,omitempty"` | 0x4ff9aa5 |
| `StartLine` | `jsonschema:"required" jsonschema_description:"The starting line number of the chunk (1-indexed). Should be at or before the first line containing the target content. Must satisfy 1 <= StartLine <= EndLine. The target content is searched for within the [StartLine, EndLine] range."` | 0x54b16b1 |
| `StartLine` | `jsonschema_description:"Optional. Startline to view, 1-indexed as usual, inclusive. This value must be less than or equal to EndLine."` | 0x51dde2d |
| `Summary` | `jsonschema:"required" jsonschema_description:"Detailed multi-line summary of the artifact file, after edits have been made. Summary does not need to mention the artifact name and should focus on the contents and purpose of the artifact."` | 0x5442ed8 |
| `Summary` | `jsonschema_description:"One paragraph summary of the Knowledge Item" json:"summary"` | 0x4fcf2a6 |
| `TargetContent` | `jsonschema:"required" jsonschema_description:"The exact string to be replaced. This must be the exact character-sequence to be replaced, including whitespace. Be very careful to include any leading whitespace otherwise this will not work at all. This must be a unique substring within the file, or else it will error."` | 0x54d0e92 |
| `TargetFile` | `json:"target_file" jsonschema:"required" jsonschema_description:"The absolute path to the file to edit."` | 0x505cde5 |
| `TargetFile` | `jsonschema:"required" jsonschema_description:"The target file to create and write code to."` | 0x501c8e0 |
| `TargetFile` | `jsonschema:"required" jsonschema_description:"The target file to modify. Always specify the target file as the very first argument."` | 0x51da16e |
| `TargetLintErrorIds` | `json:"TargetLintErrorIds,omitempty" jsonschema_description:"If applicable, IDs of lint errors this edit aims to fix (they'll have been given in recent IDE feedback). If you believe the edit could fix lints, do specify lint IDs; if the edit is wholly unrelated, do not. A rule of thumb is, if your edit was influenced by lint feedback, include lint IDs. Exercise honest judgement here."` | 0x5503dd9 |
| `Task` | `jsonschema:"required" jsonschema_description:"A clear, actionable task description for the browser subagent. The subagent is an agent similar to you, with a different set of tools, limited to tools to understand the state of and control the browser. The task you define is the prompt sent to this subagent. Since each agent invocation is a one-shot, autonomous execution, the prompt must be highly detailed, containing a comprehensive task description and all necessary context. Avoid vague instructions; be specific about what to do, when to stop, and clearly state exactly what information the agent should return in its final and only report. This should be the second argument."` | 0x5589979 |
| `TaskId` | `json:"TaskId,omitempty" jsonschema_description:"The task ID to manage. Required when Action is 'kill', 'status', or 'send_input'."` | 0x517703f |
| `TaskName` | `jsonschema:"required" jsonschema_description:"Name of the task that the browser subagent is performing. This is the identifier that groups the subagent steps together, but should still be a human readable name. This should read like a title, should be properly capitalized and human readable, example: 'Navigating to Example Page'. Replace URLs or non-human-readable expressions like CSS selectors or long text with human-readable terms like 'URL' or 'Page' or 'Submit Button'. Be very sure this task name represents a reasonable chunk of work. It should almost never be the entire user request. This should be the very first argument."` | 0x5581e38 |
| `TaskSummary` | `jsonschema:"required" jsonschema_description:"A short, user-friendly summary of the task (1-2 sentences max). This will be displayed to the user in the UI instead of the full task description. Should be concise and describe the goal at a high level."` | 0x547a7d0 |
| `Terminate` | `jsonschema_description:"Whether to terminate the command. Exactly one of input and terminate must be specified."` | 0x50d00ec |
| `Text` | `jsonschema:"required" jsonschema_description:"The text to input into the element."` | 0x4fbddab |
| `Text` | `jsonschema_description:"Text to type sequentially, character by character. Use this for typing regular text content like letters, numbers, and basic symbols. Each character will be typed individually in sequence. Only specify one of Key or Text - use Text for typing regular content, not for keyboard shortcuts or special keys like F1, Control+C, etc."` | 0x54f07d0 |
| `Title` | `json:"title" jsonschema:"required" jsonschema_description:"Title of the prompt section."` | 0x4fedde0 |
| `Title` | `jsonschema:"required" jsonschema_description:"An at most 20 character title describing the task in the imperative form. Will be displayed as the title of the tool in the step UI."` | 0x52f2063 |
| `Title` | `jsonschema_description:"Human-readable title for the Knowledge Item" json:"title"` | 0x4fbdae3 |
| `ToolNames` | `json:"tool_names,omitempty" jsonschema_description:"List of tool names available to the subagent. If empty, inherits default tools."` | 0x51d746c |
| `Type` | `jsonschema_description:"Optional, type filter, enum=file,directory,any"` | 0x4f911b9 |
| `Type` | `jsonschema_description:"Type of reference (e.g., file, conversation_id, url)" json:"type"` | 0x4fe9dc0 |
| `TypeName` | `jsonschema:"required" jsonschema_description:"Type name of the subagent to invoke."` | 0x4fd5013 |
| `URL` | `json:"Url" jsonschema:"required" jsonschema_description:"URL to read content from"` | 0x4fbb1a8 |
| `Uri` | `jsonschema_description:"Unique identifier for the resource."` | 0x4f4c420 |
| `Url` | `jsonschema:"required" json:"Url" jsonschema_description:"Full API URL (e.g., https://docs.googleapis.com/v1/documents/{documentId}:batchUpdate)"` | 0x51efd4b |
| `Url` | `jsonschema:"required" jsonschema_description:"The URL to open in the user's browser."` | 0x4fc4d4b |
| `Value` | `jsonschema:"required" jsonschema_description:"The value or text of the option to select from the dropdown."` | 0x505347f |
| `Value` | `jsonschema_description:"Value of the reference" json:"value"` | 0x4f51f51 |
| `WaitDurationSeconds` | `jsonschema:"required" jsonschema_description:"Number of seconds to wait for command completion before getting the status. If the command completes before this duration, this tool call will return early. Set to 0 to get the status of the command immediately. If you are only interested in waiting for command completion, set to the max value, 300."` | 0x54f2a32 |
| `WaitMs` | `jsonschema:"required" jsonschema_description:"Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms."` | 0x540575b |
| `WaitMsBeforeAsync` | `jsonschema:"required" json:"WaitMsBeforeAsync" jsonschema_description:"This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms). Keep the value as small as possible, with a maximum of 10000ms."` | 0x557a578 |
| `Waypoints` | `jsonschema_description:"A series of pixel coordinates defining the drag path. When this tool call is executed, the first waypoint will be clicked, then the mouse will be dragged to each subsequent waypoint in the provided order, and finally the mouse will be released at the last waypoint."` | 0x54b5671 |
| `Width` | `jsonschema_description:"The window contents width in display independent pixels. Only used when WindowState is 'normal'."` | 0x513babc |
| `WindowState` | `jsonschema:"required" jsonschema_description:"The window state to set. Options: 'normal' (resizable window with specified width/height), 'minimized' (window minimized to taskbar), 'maximized' (window is full screen but shows taskbar), 'fullscreen' (window fills entire screen and hides taskbar). Width and Height are only used when WindowState is 'normal'. Generally you should prefer 'maximized'. If the user asks to make the window smaller or a particular size, use 'normal'. When resetting the window size, prefer 'maximized' instead of 'normal' with specific width/height values. 'minimized' and 'fullscreen' are somewhat jarring, so you should only use these when the user explicitly asks for it." jsonschema:"enum=normal,enum=minimized,enum=maximized,enum=fullscreen"` | 0x5592427 |
| `Workspace` | `jsonschema_description:"Workspace mode for the subagent. 'inherit' (default) shares the parent's workspace. 'branch' creates a new workspace branched from the parent (CitC clone or git worktree). If omitted, defaults to 'inherit'."` | 0x543c2ab |
| `X` | `jsonschema:"required" jsonschema_description:"X coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call."` | 0x5365940 |
| `X` | `jsonschema:"required" jsonschema_description:"X coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions."` | 0x52b36fc |
| `X` | `jsonschema:"required" jsonschema_description:"x-coordinate of the pixel to move the mouse cursor to."` | 0x5020837 |
| `X` | `jsonschema_description:"X coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call."` | 0x5368a8c |
| `Y` | `jsonschema:"required" jsonschema_description:"Y coordinate of the pixel to click (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call."` | 0x5365878 |
| `Y` | `jsonschema:"required" jsonschema_description:"Y coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions."` | 0x52b37a8 |
| `Y` | `jsonschema:"required" jsonschema_description:"y-coordinate of the pixel to move the mouse cursor to."` | 0x50208a0 |
| `Y` | `jsonschema_description:"Y coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call."` | 0x5368b55 |
