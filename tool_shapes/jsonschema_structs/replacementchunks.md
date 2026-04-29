# `ToJsonSchemaString` struct @ 0x2f9e1ae

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- **embedded** `google3/third_party/jetski/cortex/tools/tools.TabCodeEditArgs`

- `ReplacementChunks` _[]*google3/third_party/jetski/cortex/tools/tools.ReplacementChunkForTab_
  - `jsonschema` = `required`
  - `jsonschema_description` = `A list of chunks to replace. It is best to provide multiple chunks for non-contiguous edits if possible. This must be a JSON array, not a string.`

## Raw body

```
 google3/third_party/jetski/cortex/tools/tools.TabCodeEditArgs; ReplacementChunks []*google3/third_party/jetski/cortex/tools/tools.ReplacementChunkForTab "jsonschema:\"required\" jsonschema_description:\"A list of chunks to replace. It is best to provide multiple chunks for non-contiguous edits if possible. This must be a JSON array, not a string.\"" 
```
