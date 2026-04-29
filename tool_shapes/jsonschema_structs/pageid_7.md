# `ParseToolArgs` struct @ 0x30351ed

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `PageId` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `page_id of the Browser page to move the mouse cursor to.`

- `X` _int32_
  - `jsonschema` = `required`
  - `jsonschema_description` = `x-coordinate of the pixel to move the mouse cursor to.`

- `Y` _int32_
  - `jsonschema` = `required`
  - `jsonschema_description` = `y-coordinate of the pixel to move the mouse cursor to.`

## Raw body

```
 PageId string "jsonschema:\"required\" jsonschema_description:\"page_id of the Browser page to move the mouse cursor to.\""; X int32 "jsonschema:\"required\" jsonschema_description:\"x-coordinate of the pixel to move the mouse cursor to.\""; Y int32 "jsonschema:\"required\" jsonschema_description:\"y-coordinate of the pixel to move the mouse cursor to.\"" 
```
