# `ask_question`

**Cortex step type:** `CortexStepAskQuestion`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (1)

```proto
message CortexStepAskQuestion {
  repeated exa.cortex_pb.AskQuestionEntry questions = 1;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `questions`
```
The list of questions to ask.
```
```
The text for each option, formatted as the user's response. Must have at least 2 options. Do NOT add an 'Other' option to questions.
```
