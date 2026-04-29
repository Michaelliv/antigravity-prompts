# `subagent_create`


## Parameter descriptions (12)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Title of the prompt section.
```

### 2.
```
Content of the prompt section.
```

### 3.
```
Unique name for the subagent. Used to invoke it via invoke_subagent.
```

### 4.
```
Custom prompt sections to include in the subagent's system prompt.
```

### 5.
```
List of tool names available to the subagent. If empty, inherits default tools.
```

### 6.
```
Human-readable description of what this subagent does and when it should be used.
```

### 7.
```
Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.
```

### 8.
```
A clear, actionable task description for the subagent. Be specific about what the subagent should do and what information it should return.
```

### 9.
```
Workspace mode for the subagent. 'inherit' (default) shares the parent's workspace. 'branch' creates a new workspace branched from the parent (CitC clone or git worktree). If omitted, defaults to 'inherit'.
```

### 10.
```
A 2-5 word description of the subagent's role. Should read similar to a job title, e.g. 'Codebase Researcher', 'Database Debugger', etc. Should also be detailed enough to distinguish between different subagents who might share similar purposes.
```

### 11.
```
ID of a previous subagent to resume from. If provided, the agent will continue from the previous context. If empty, the subagent will start with an empty context. Use this to resume work from a cancelled subagent, or when the current task would benefit from the previous subagent's context.
```

### 12.
```
Model to use for the subagent. 'inherit' (default) uses the calling agent's model. 'fast' uses a smaller, faster model suited for simple tasks like research lookups, file reading, or quick searches. 'heavy' uses a larger, more capable model suited for complex tasks requiring deep reasoning, large refactors, or multi-step planning.
```
