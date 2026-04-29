# `ParseToolArgs` struct @ 0x3035860

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `PageId` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `page_id of the Browser page to get the DOM tree of`

## Raw body

```
 PageId string "jsonschema:\"required\" jsonschema_description:\"page_id of the Browser page to get the DOM tree of\"" 
```
