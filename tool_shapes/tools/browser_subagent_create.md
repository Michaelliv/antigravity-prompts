# `browser_subagent_create`


## Parameter descriptions (4)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
A short, user-friendly summary of the task (1-2 sentences max). This will be displayed to the user in the UI instead of the full task description. Should be concise and describe the goal at a high level.
```

### 2.
```
Name of the browser recording that is created with the actions of the subagent. Should be all lowercase with underscores, describing what the recording contains. Maximum 3 words. Example: 'login_flow_demo'
```

### 3.
```
Name of the task that the browser subagent is performing. This is the identifier that groups the subagent steps together, but should still be a human readable name. This should read like a title, should be properly capitalized and human readable, example: 'Navigating to Example Page'. Replace URLs or non-human-readable expressions like CSS selectors or long text with human-readable terms like 'URL' or 'Page' or 'Submit Button'. Be very sure this task name represents a reasonable chunk of work. It should almost never be the entire user request. This should be the very first argument.
```

### 4.
```
A clear, actionable task description for the browser subagent. The subagent is an agent similar to you, with a different set of tools, limited to tools to understand the state of and control the browser. The task you define is the prompt sent to this subagent. Since each agent invocation is a one-shot, autonomous execution, the prompt must be highly detailed, containing a comprehensive task description and all necessary context. Avoid vague instructions; be specific about what to do, when to stop, and clearly state exactly what information the agent should return in its final and only report. This should be the second argument.
```
