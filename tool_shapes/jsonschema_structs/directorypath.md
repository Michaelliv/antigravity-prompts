# `ParseToolArgs` struct @ 0x2f9dff1

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `DirectoryPath` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `Path to list contents of, should be absolute path to a directory`

## Raw body

```
 DirectoryPath string "jsonschema:\"required\" jsonschema_description:\"Path to list contents of, should be absolute path to a directory\"" 
```
