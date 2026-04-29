# `ParseToolArgs` struct @ 0x3034a6e

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `PageId` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `page_id of the Browser page to release the mouse button on`

- `Button` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `Mouse button to release. Options are 'left', 'right', or 'middle'.`

## Raw body

```
 PageId string "jsonschema:\"required\" jsonschema_description:\"page_id of the Browser page to release the mouse button on\""; Button string "jsonschema:\"required\" jsonschema_description:\"Mouse button to release. Options are 'left', 'right', or 'middle'.\"" 
```
