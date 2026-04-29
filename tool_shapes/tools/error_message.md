# `error_message`

**Cortex step type:** `CortexStepErrorMessage`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (3)

```proto
message CortexStepErrorMessage {
  exa.cortex_pb.CortexErrorDetails error = 3;
  bool should_show_user = 5;
  bool should_show_model = 4;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `error`
```
If true, multiple occurrences of 'targetContent' will be replaced by 'replacementContent' if they are found. Otherwise if multiple occurences are found, an error will be returned.
```
```
The exact string to be replaced. This must be the exact character-sequence to be replaced, including whitespace. Be very careful to include any leading whitespace otherwise this will not work at all. This must be a unique substring within the file, or else it will error.
```
