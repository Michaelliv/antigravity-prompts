# `unknown_0x54f2a32` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x54f2a32–0x54f2d18

| field | flag | tag |
|---|---|---|
| `WaitDurationSeconds` | 0x3 | `jsonschema:"required" jsonschema_description:"Number of seconds to wait for command completion before getting the status. If the command completes before this duration, this tool call will return early. Set to 0 to get the status of the command immediately. If you are only interested in waiting for command completion, set to the max value, 300."` |
| `ResourceTypes` | 0x3 | `jsonschema_description:"The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'."` |

### Parsed tags

**`WaitDurationSeconds`**
- `jsonschema` = `required`
- `jsonschema_description` = `Number of seconds to wait for command completion before getting the status. If the command completes before this duration, this tool call will return early. Set to 0 to get the status of the command immediately. If you are only interested in waiting for command completion, set to the max value, 300.`

**`ResourceTypes`**
- `jsonschema_description` = `The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'.`
