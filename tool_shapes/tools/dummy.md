# `dummy`

**Cortex step type:** `CortexStepDummy`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (2)

```proto
message CortexStepDummy {
  uint32 input = 1;
  uint32 output = 2;
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

### `output`
```
The command ID from a previous run_command call. This is returned in the run_command output.
```
```
Amount of time to wait for output after sending input. Keep the value as small as possible, but large enough to capture the output you expect. Must be between 500ms and 10000ms.
```
