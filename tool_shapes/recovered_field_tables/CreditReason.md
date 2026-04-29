# `CreditReason` recovered field table

Recovered from Go reflect-name records in language-server binary.

## Cluster @ 0x540575b–0x5405845
- Likely cortex step: `CortexStepCreditReason`

| field | flag | tag |
|---|---|---|
| `WaitMs` | 0x3 | `jsonschema:"required" jsonschema_description:"Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms."` |

### Parsed tags

**`WaitMs`**
- `jsonschema` = `required`
- `jsonschema_description` = `Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.`

## Cluster @ 0x5406172–0x540625d
- Likely cortex step: `CortexStepCreditReason`

| field | flag | tag |
|---|---|---|
| `Input` | 0x3 | `jsonschema_description:"The input to send to the command's stdin. Include newline characters (the literal character, not the escape sequence) if needed to submit commands. Exactly one of input and terminate must be specified."` |

### Parsed tags

**`Input`**
- `jsonschema_description` = `The input to send to the command's stdin. Include newline characters (the literal character, not the escape sequence) if needed to submit commands. Exactly one of input and terminate must be specified.`
