# `ToJsonSchemaString` struct @ 0x2f9d7fa

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `ServerName` _string_
  - `jsonschema_description` = `Name of the server to read the resource from.`

- `Uri` _string_
  - `jsonschema_description` = `Unique identifier for the resource.`

## Raw body

```
 ServerName string "jsonschema_description:\"Name of the server to read the resource from.\""; Uri string "jsonschema_description:\"Unique identifier for the resource.\"" 
```
