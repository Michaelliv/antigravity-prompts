# `command_status`

**Cortex step type:** `CortexStepCommandStatus`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (12)

```proto
message CortexStepCommandStatus {
  string command_id = 1;
  uint32 output_character_count = 8;
  uint32 wait_duration_seconds = 10;
  exa.cortex_pb.CortexStepStatus status = 2;
  string combined = 9;
  string delta = 12;
  int32 exit_code = 5;
  exa.cortex_pb.CortexErrorDetails error = 6;
  uint32 waited_duration_seconds = 11;
  string stdout = 3;
  string stderr = 4;
  exa.cortex_pb.CommandOutputPriority output_priority = 7;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `status`
```
ID of the command to get status for
```
```
The task ID to manage. Required when Action is 'kill', 'status', or 'send_input'.
```
```
The action to perform: 'list' (list all running tasks), 'kill' (cancel the task), 'status' (check the task status and log URI), 'send_input' (send input to a running task).
```

### `delta`
```
Vertical scroll delta in pixels. Positive values scroll down, negative values scroll up.
```
```
Horizontal scroll delta in pixels. Positive values scroll to the right, negative values scroll to the left.
```

### `error`
```
If true, multiple occurrences of 'targetContent' will be replaced by 'replacementContent' if they are found. Otherwise if multiple occurences are found, an error will be returned.
```
```
The exact string to be replaced. This must be the exact character-sequence to be replaced, including whitespace. Be very careful to include any leading whitespace otherwise this will not work at all. This must be a unique substring within the file, or else it will error.
```
