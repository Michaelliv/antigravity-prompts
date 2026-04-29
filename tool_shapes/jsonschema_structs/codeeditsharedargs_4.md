# `ToJsonSchemaString` struct @ 0x2f03a5e

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- **embedded** `google3/third_party/jetski/cortex/tools/code/code.CodeEditSharedArgs`

- **embedded** `*google3/third_party/jetski/cortex/tools/code/code.ReplacementChunk`
  - `jsonschema` = `required`
  - `jsonschema_description` = `A single contiguous chunk to replace. For non-contiguous edits, use the multi_replace_file_content tool instead.`

## Raw body

```
 google3/third_party/jetski/cortex/tools/code/code.CodeEditSharedArgs; *google3/third_party/jetski/cortex/tools/code/code.ReplacementChunk "jsonschema:\"required\" jsonschema_description:\"A single contiguous chunk to replace. For non-contiguous edits, use the multi_replace_file_content tool instead.\"" 
```
