# `send_command_input`

**Cortex step type:** `CortexStepSendCommandInput`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (10)

```proto
message CortexStepSendCommandInput {
  string command_id = 1;
  string input = 2;
  bool should_auto_run = 3;
  bool terminate = 6;
  int64 wait_ms = 7;
  bool user_rejected = 4;
  exa.cortex_pb.AutoRunDecision auto_run_decision = 5;
  exa.cortex_pb.RunCommandOutput output = 8;
  bool running = 9;
  int32 exit_code = 10;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `input`
```
The text to input into the element.
```
```
The page_id of the browser page to input text on.
```
```
Index of the annotated DOM element to input text into.
```

### `terminate`
```
Whether to terminate the command. Exactly one of input and terminate must be specified.
```
```
The input to send to the command's stdin. Include newline characters (the literal character, not the escape sequence) if needed to submit commands. Exactly one of input and terminate must be specified.
```

### `output`
```
The command ID from a previous run_command call. This is returned in the run_command output.
```
```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```

### `running`
```
The action to perform: 'list' (list all running tasks), 'kill' (cancel the task), 'status' (check the task status and log URI), 'send_input' (send input to a running task).
```
```
This specifies the number of milliseconds to wait after starting the command before sending it to the background. If you want the command to complete execution synchronously, set this to a large enough value that you expect the command to complete in that time under ordinary circumstances. If you're starting an interactive or long-running command, set it to a large enough value that it would cause possible failure cases to execute synchronously (e.g. 500ms). Keep the value as small as possible, with a maximum of 10000ms.
```
