# `send_command_input`

**Cortex step type:** `CortexStepSendCommandInput`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (10)

Field names recovered from `(*CortexStepSendCommandInput).Get*` symbols (includes both inputs and outputs).

- `AutoRunDecision`
- `CommandId`
- `ExitCode`
- `Input`
- `Output`
- `Running`
- `ShouldAutoRun`
- `Terminate`
- `UserRejected`
- `WaitMs`


## Parameter descriptions (1)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```
