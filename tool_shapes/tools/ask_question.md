# `ask_question`

**Cortex step type:** `CortexStepAskQuestion`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (1)

Field names recovered from `(*CortexStepAskQuestion).Get*` symbols (includes both inputs and outputs).

- `Questions`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The list of questions to ask.
```

### 2.
```
The question to ask the user. Do NOT add 'select all that apply' or similar text to the question title.
```

### 3.
```
The text for each option, formatted as the user's response. Must have at least 2 options. Do NOT add an 'Other' option to questions.
```
