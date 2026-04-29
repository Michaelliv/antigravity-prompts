# `browser_subagent`

**Cortex step type:** `CortexStepBrowserSubagent`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (12)

```proto
message CortexStepBrowserSubagent {
  string task = 1;
  string reused_subagent_id = 9;
  string recording_name = 7;
  repeated exa.codeium_common_pb.Media media = 11;
  string result = 2;
  string task_name = 3;
  string task_summary = 13;
  string recording_path = 4;
  exa.cortex_pb.RecordingGenerationStatus recording_generation_status = 6;
  string subagent_id = 8;
  bool skipped = 10;
  string scratchpad_path = 12;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `task`
```
The input to send to the task. Required when Action is 'send_input'.
```
```
The task ID to manage. Required when Action is 'kill', 'status', or 'send_input'.
```
```
An at most 20 character title describing the task in the imperative form. Will be displayed as the title of the tool in the step UI.
```

### `media`
```
Optional absolute paths to media files (images, videos, etc.) to provide as context to the subagent. Maximum 3 files.
```
```
The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'.
```
