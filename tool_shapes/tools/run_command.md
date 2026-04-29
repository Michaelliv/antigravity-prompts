# `run_command`

**Cortex step type:** `CortexStepRunCommand`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (28)

Field names recovered from `(*CortexStepRunCommand).Get*` symbols (includes both inputs and outputs).

- `Args`
- `AutoRunDecision`
- `Blocking`
- `CombinedOutput`
- `CombinedOutputSnapshot`
- `Command`
- `CommandId`
- `CommandLine`
- `Cwd`
- `ExitCode`
- `ProposedCommandLine`
- `RawDebugOutput`
- `RequestedTerminalId`
- `RunPersistent`
- `SandboxOverride`
- `ShouldAutoRun`
- `Stderr`
- `StderrBuffer`
- `StderrLinesAbove`
- `StderrOutput`
- `Stdout`
- `StdoutBuffer`
- `StdoutLinesAbove`
- `StdoutOutput`
- `TerminalId`
- `UsedIdeTerminal`
- `UserRejected`
- `WaitMsBeforeAsync`


## Parameter descriptions (5)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Whether to terminate the command. Exactly one of input and terminate must be specified.
```

### 2.
```
Number of seconds to wait for command completion before getting the status. If the command completes before this duration, this tool call will return early. Set to 0 to get the status of the command immediately. If you are only interested in waiting for command completion, set to the max value, 300.
```

### 3.
```
Set to true if you believe that this command is safe to run WITHOUT user approval. An input is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the input could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe input.
```

### 4.
```
Set to true if you believe that this command is safe to run WITHOUT user approval. A command is unsafe if it may have some destructive side-effects. Example unsafe side-effects include: deleting files, mutating state, installing system dependencies, making external requests, etc. Set to true only if you are extremely confident it is safe. If you feel the command could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run a potentially unsafe command.
```

### 5.
```
This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms). Keep the value as small as possible, with a maximum of 10000ms.
```
