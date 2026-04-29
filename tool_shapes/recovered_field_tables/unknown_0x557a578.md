# `unknown_0x557a578` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x557a578–0x557a7e3

| field | flag | tag |
|---|---|---|
| `WaitMsBeforeAsync` | 0x3 | `jsonschema:"required" json:"WaitMsBeforeAsync" jsonschema_description:"This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms). Keep the value as small as possible, with a maximum of 10000ms."` |

### Parsed tags

**`WaitMsBeforeAsync`**
- `jsonschema` = `required`
- `json` = `WaitMsBeforeAsync`
- `jsonschema_description` = `This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms). Keep the value as small as possible, with a maximum of 10000ms.`
