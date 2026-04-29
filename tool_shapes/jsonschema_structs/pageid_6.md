# `ParseToolArgs` struct @ 0x3034e32

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `PageId` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `The page_id of the browser page containing the dropdown element.`

- `Index` _int32_
  - `jsonschema` = `required`
  - `jsonschema_description` = `Index of the annotated DOM select element to select an option from.`

- `Value` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `The value or text of the option to select from the dropdown.`

## Raw body

```
 PageId string "jsonschema:\"required\" jsonschema_description:\"The page_id of the browser page containing the dropdown element.\""; Index int32 "jsonschema:\"required\" jsonschema_description:\"Index of the annotated DOM select element to select an option from.\""; Value string "jsonschema:\"required\" jsonschema_description:\"The value or text of the option to select from the dropdown.\"" 
```
