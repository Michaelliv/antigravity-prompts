# `unknown_0x557612f` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x557612f–0x557637e

| field | flag | tag |
|---|---|---|
| `SafeToAutoRun` | 0x3 | `jsonschema:"required" json:"SafeToAutoRun" jsonschema_description:"Set to true if you believe that this command is safe to run WITHOUT user approval. A command is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the command could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe command."` |

### Parsed tags

**`SafeToAutoRun`**
- `jsonschema` = `required`
- `json` = `SafeToAutoRun`
- `jsonschema_description` = `Set to true if you believe that this command is safe to run WITHOUT user approval. A command is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the command could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe command.`
