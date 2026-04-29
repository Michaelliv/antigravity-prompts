# `manager_feedback`

**Cortex step type:** `CortexStepManagerFeedback`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (2)

```proto
message CortexStepManagerFeedback {
  exa.cortex_pb.CortexStepManagerFeedbackStatus status = 1;
  string feedback = 2;
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

### `feedback`
```
Set to true to request user feedback on this artifact.
```
```
If applicable, IDs of lint errors this edit aims to fix (they'll have been given in recent IDE feedback). If you believe the edit could fix lints, do specify lint IDs; if the edit is wholly unrelated, do not. A rule of thumb is, if your edit was influenced by lint feedback, include lint IDs. Exercise honest judgement here.
```
