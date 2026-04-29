# `ExecuteBrowserJavaScript` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x504d010–0x504d082
- Likely cortex step: `CortexStepExecuteBrowserJavaScript`

| field | flag | tag |
|---|---|---|
| `HttpMethod` | 0x3 | `jsonschema:"required" json:"HttpMethod" jsonschema_description:"HTTP method (GET, POST, PUT, DELETE)"` |

### Parsed tags

**`HttpMethod`**
- `jsonschema` = `required`
- `json` = `HttpMethod`
- `jsonschema_description` = `HTTP method (GET, POST, PUT, DELETE)`

## Cluster @ 0x504d568–0x504d5da
- Likely cortex step: `CortexStepExecuteBrowserJavaScript`

| field | flag | tag |
|---|---|---|
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to release the mouse button on"` |

### Parsed tags

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to release the mouse button on`

## Cluster @ 0x50b8eb0–0x50b8fa0
- Likely cortex step: `CortexStepExecuteBrowserJavaScript`

| field | flag | tag |
|---|---|---|
| `Button` | 0x3 | `jsonschema:"required" jsonschema_description:"Mouse button to press. Options are 'left', 'right', or 'middle'."` |
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"The page_id of the browser page containing the dropdown element."` |

### Parsed tags

**`Button`**
- `jsonschema` = `required`
- `jsonschema_description` = `Mouse button to press. Options are 'left', 'right', or 'middle'.`

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `The page_id of the browser page containing the dropdown element.`

## Cluster @ 0x50bed41–0x50bedba
- Likely cortex step: `CortexStepExecuteBrowserJavaScript`

| field | flag | tag |
|---|---|---|
| `CommandLine` | 0x3 | `json:"CommandLine" jsonschema:"required" jsonschema_description:"The exact command line string to execute."` |

### Parsed tags

**`CommandLine`**
- `json` = `CommandLine`
- `jsonschema` = `required`
- `jsonschema_description` = `The exact command line string to execute.`
