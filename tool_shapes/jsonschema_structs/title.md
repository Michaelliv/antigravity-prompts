# `ToJsonSchemaString` struct @ 0x2fe6efc

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `Title` _string_
  - `jsonschema_description` = `Human-readable title for the Knowledge Item`
  - `json` = `title`

- `Summary` _string_
  - `jsonschema_description` = `One paragraph summary of the Knowledge Item`
  - `json` = `summary`

- `References` _[]google3/third_party/jetski/cortex/artifacts/knowledge/knowledge.Reference_
  - `jsonschema_description` = `List of references related to this Knowledge Item`
  - `json` = `references,omitempty`

## Raw body

```
 Title string "jsonschema_description:\"Human-readable title for the Knowledge Item\" json:\"title\""; Summary string "jsonschema_description:\"One paragraph summary of the Knowledge Item\" json:\"summary\""; References []google3/third_party/jetski/cortex/artifacts/knowledge/knowledge.Reference "jsonschema_description:\"List of references related to this Knowledge Item\" json:\"references,omitempty\"" 
```
