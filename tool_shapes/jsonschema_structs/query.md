# `ParseToolArgs` struct @ 0x2f9d9b4

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `Query` _string_
  - `jsonschema` = `required`
  - `json` = `query`

- `Domain` _string_
  - `json` = `domain`
  - `jsonschema_description` = `Optional domain to recommend the search prioritize`

## Raw body

```
 Query string "jsonschema:\"required\" json:\"query\""; Domain string "json:\"domain\" jsonschema_description:\"Optional domain to recommend the search prioritize\"" 
```
