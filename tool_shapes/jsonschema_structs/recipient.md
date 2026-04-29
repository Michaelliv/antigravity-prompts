# `ToJsonSchemaString` struct @ 0x2f9e364

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `Recipient` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `The recipient ID to send the message to, e.g. a subagent conversation ID.`

- `Message` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `The message content.`

## Raw body

```
 Recipient string "jsonschema:\"required\" jsonschema_description:\"The recipient ID to send the message to, e.g. a subagent conversation ID.\""; Message string "jsonschema:\"required\" jsonschema_description:\"The message content.\"" 
```
