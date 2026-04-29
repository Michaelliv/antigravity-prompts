# `ParseToolArgs` struct @ 0x303418d

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `PageId` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `The page_id of the browser page to get network request from.`

- `RequestId` _string_
  - `jsonschema` = `required`
  - `jsonschema_description` = `The request ID to retrieve details for. This ID can be obtained from the list_network_requests tool.`

## Raw body

```
 PageId string "jsonschema:\"required\" jsonschema_description:\"The page_id of the browser page to get network request from.\""; RequestId string "jsonschema:\"required\" jsonschema_description:\"The request ID to retrieve details for. This ID can be obtained from the list_network_requests tool.\"" 
```
