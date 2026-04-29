# `ListBrowserPages` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x5023314–0x502337e
- Likely cortex step: `CortexStepListBrowserPages`

| field | flag | tag |
|---|---|---|
| `Excludes` | 0x3 | `jsonschema_description:"Optional, exclude files/directories that match the given glob patterns"` |

### Parsed tags

**`Excludes`**
- `jsonschema_description` = `Optional, exclude files/directories that match the given glob patterns`

## Cluster @ 0x5023664–0x50236ce
- Likely cortex step: `CortexStepListBrowserPages`

| field | flag | tag |
|---|---|---|
| `PageId` | 0x3 | `jsonschema:"required" jsonschema_description:"page_id of the Browser page to get the DOM tree of"` |

### Parsed tags

**`PageId`**
- `jsonschema` = `required`
- `jsonschema_description` = `page_id of the Browser page to get the DOM tree of`
