# `task_boundary`

**Cortex step type:** `CortexStepTaskBoundary`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepTaskBoundary {
  string task_name = 1;
  string task_status = 2;
  string task_summary = 3;
  string task_summary_with_citations = 4;
  string delta_summary = 6;
  string delta_summary_with_citations = 7;
  exa.cortex_pb.AgentMode mode = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `mode`
```
Workspace mode for the subagent. 'inherit' (default) shares the parent's workspace. 'branch' creates a new workspace branched from the parent (CitC clone or git worktree). If omitted, defaults to 'inherit'.
```
