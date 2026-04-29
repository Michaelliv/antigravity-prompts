# `Type` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x4f294a9–0x4f294e6
- Likely cortex step: `CortexStepType`

| field | flag | tag |
|---|---|---|
| `Body` | 0x3 | `json:"Body" jsonschema_description:"Request body JSON"` |

### Parsed tags

**`Body`**
- `json` = `Body`
- `jsonschema_description` = `Request body JSON`

## Cluster @ 0x52d78e4–0x52d7996
- Likely cortex step: `CortexStepType`

| field | flag | tag |
|---|---|---|
| `MediaPaths` | 0x3 | `jsonschema:"optional" jsonschema_description:"Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files."` |

### Parsed tags

**`MediaPaths`**
- `jsonschema` = `optional`
- `jsonschema_description` = `Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.`

## Cluster @ 0x52f2063–0x52f211f
- Likely cortex step: `CortexStepType`

| field | flag | tag |
|---|---|---|
| `Title` | 0x3 | `jsonschema:"required" jsonschema_description:"An at most 20 character title describing the task in the imperative form. Will be displayed as the title of the tool in the step UI."` |

### Parsed tags

**`Title`**
- `jsonschema` = `required`
- `jsonschema_description` = `An at most 20 character title describing the task in the imperative form. Will be displayed as the title of the tool in the step UI.`

## Cluster @ 0x53524a8–0x5352569
- Likely cortex step: `CortexStepType`

| field | flag | tag |
|---|---|---|
| `Action` | 0x3 | `jsonschema:"required,enum=list,enum=read" jsonschema_description:"The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message)."` |

### Parsed tags

**`Action`**
- `jsonschema` = `required,enum=list,enum=read`
- `jsonschema_description` = `The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message).`

## Cluster @ 0x535490c–0x53549cf
- Likely cortex step: `CortexStepType`

| field | flag | tag |
|---|---|---|
| `Classification` | 0x3 | `jsonschema_description:"Classification of the edit. Examples include \"Continuing the user's work\", \"Bug fix\", and \"Documentation\"." jsonschema_extras:"\"type\":\"string\""` |

### Parsed tags

**`Classification`**
- `jsonschema_description` = `Classification of the edit. Examples include "Continuing the user's work", "Bug fix", and "Documentation".`
- `jsonschema_extras` = `"type":"string"`

## Cluster @ 0x53560c3–0x535624b
- Likely cortex step: `CortexStepType`

| field | flag | tag |
|---|---|---|
| `ScrollToEnd` | 0x3 | `jsonschema_description:"if true, scroll in the direction to the end of the selected element/page. For example, if direction is down, would scroll to the bottom of the element/page."` |
| `Prompt` | 0x3 | `jsonschema:"required" jsonschema_description:"A clear, actionable task description for the subagent. Be specific about what the subagent should do and what information it should return."` |

### Parsed tags

**`ScrollToEnd`**
- `jsonschema_description` = `if true, scroll in the direction to the end of the selected element/page. For example, if direction is down, would scroll to the bottom of the element/page.`

**`Prompt`**
- `jsonschema` = `required`
- `jsonschema_description` = `A clear, actionable task description for the subagent. Be specific about what the subagent should do and what information it should return.`
