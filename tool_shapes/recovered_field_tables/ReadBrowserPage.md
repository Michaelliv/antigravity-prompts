# `ReadBrowserPage` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x50207ce–0x5020909
- Likely cortex step: `CortexStepReadBrowserPage`

| field | flag | tag |
|---|---|---|
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"The page_id of the browser page to input text on."` |
| `X` | 0x3 | `jsonschema:"required" jsonschema_description:"x-coordinate of the pixel to move the mouse cursor to."` |
| `Y` | 0x3 | `jsonschema:"required" jsonschema_description:"y-coordinate of the pixel to move the mouse cursor to."` |

### Parsed tags

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `The page_id of the browser page to input text on.`

**`X`**
- `jsonschema` = `required`
- `jsonschema_description` = `x-coordinate of the pixel to move the mouse cursor to.`

**`Y`**
- `jsonschema` = `required`
- `jsonschema_description` = `y-coordinate of the pixel to move the mouse cursor to.`

## Cluster @ 0x50323a0–0x503247c
- Likely cortex step: `CortexStepReadBrowserPage`

| field | flag | tag |
|---|---|---|
| `Pattern` | 0x3 | `jsonschema:"required" jsonschema_description:"Optional, Pattern to search for, supports glob format"` |
| `Questions` | 0x3 | `json:"questions" jsonschema_description:"The list of questions to ask." jsonschema_required:"true"` |

### Parsed tags

**`Pattern`**
- `jsonschema` = `required`
- `jsonschema_description` = `Optional, Pattern to search for, supports glob format`

**`Questions`**
- `json` = `questions`
- `jsonschema_description` = `The list of questions to ask.`
- `jsonschema_required` = `true`

## Cluster @ 0x5032710–0x503277e
- Likely cortex step: `CortexStepReadBrowserPage`

| field | flag | tag |
|---|---|---|
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to simulate a key press on"` |

### Parsed tags

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to simulate a key press on`

## Cluster @ 0x50368d9–0x50369b7
- Likely cortex step: `CortexStepReadBrowserPage`

| field | flag | tag |
|---|---|---|
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to capture console logs of."` |
| `PageID` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to capture a screenshot of."` |

### Parsed tags

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to capture console logs of.`

**`PageID`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to capture a screenshot of.`

## Cluster @ 0x5044f40–0x5045090
- Likely cortex step: `CortexStepReadBrowserPage`

| field | flag | tag |
|---|---|---|
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to press the mouse button on"` |
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to move the mouse cursor to."` |
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to execute the JavaScript on"` |

### Parsed tags

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to press the mouse button on`

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to move the mouse cursor to.`

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to execute the JavaScript on`
