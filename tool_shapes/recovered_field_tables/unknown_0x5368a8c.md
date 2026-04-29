# `unknown_0x5368a8c` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x5368a8c–0x5368db0

| field | flag | tag |
|---|---|---|
| `X` | 0x3 | `jsonschema_description:"X coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call."` |
| `Y` | 0x3 | `jsonschema_description:"Y coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call."` |
| `ArtifactType` | 0x3 | `jsonschema:"required,enum=implementation_plan,enum=walkthrough,enum=task,enum=other" jsonschema_description:"Type of artifact: 'implementation_plan', 'walkthrough', 'task', or 'other'."` |
| `PathToDelete` | 0x3 | `jsonschema_description:"Absolute path to the file or directory to delete. Must be either within an artifacts/ subdirectory of a Knowledge Item, or a top-level Knowledge Item directory."` |

### Parsed tags

**`X`**
- `jsonschema_description` = `X coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.`

**`Y`**
- `jsonschema_description` = `Y coordinate for starting, continuing, or ending dragging (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions when executing the tool call.`

**`ArtifactType`**
- `jsonschema` = `required,enum=implementation_plan,enum=walkthrough,enum=task,enum=other`
- `jsonschema_description` = `Type of artifact: 'implementation_plan', 'walkthrough', 'task', or 'other'.`

**`PathToDelete`**
- `jsonschema_description` = `Absolute path to the file or directory to delete. Must be either within an artifacts/ subdirectory of a Knowledge Item, or a top-level Knowledge Item directory.`
