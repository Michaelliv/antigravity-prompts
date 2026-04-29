# `ToJsonSchemaString` struct @ 0x2f9e648

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `Action` _string_
  - `jsonschema` = `required,enum=list,enum=read`
  - `jsonschema_description` = `The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message).`

- `MessageID` _string_
  - `json` = `MessageID,omitempty`
  - `jsonschema_description` = `The ID of the message to read. Required when Action is 'read'.`

## Raw body

```
 Action string "jsonschema:\"required,enum=list,enum=read\" jsonschema_description:\"The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message).\""; MessageID string "json:\"MessageID,omitempty\" jsonschema_description:\"The ID of the message to read. Required when Action is 'read'.\"" 
```
