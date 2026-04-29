# `search_web`

**Cortex step type:** `CortexStepSearchWeb`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (7)

```proto
message CortexStepSearchWeb {
  string query = 1;
  string domain = 3;
  repeated exa.codeium_common_pb.KnowledgeBaseItem web_documents = 2;
  string web_search_url = 4;
  string summary = 5;
  exa.codeium_common_pb.ThirdPartyWebSearchConfig third_party_config = 6;
  exa.cortex_pb.SearchWebType search_type = 7;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `query`
```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```
```
If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality.
```

### `domain`
```
Optional domain to recommend the search prioritize
```

### `summary`
```
One paragraph summary of the Knowledge Item
```
```
Detailed multi-line summary of the artifact file, after edits have been made. Summary does not need to mention the artifact name and should focus on the contents and purpose of the artifact.
```
```
A short, user-friendly summary of the task (1-2 sentences max). This will be displayed to the user in the UI instead of the full task description. Should be concise and describe the goal at a high level.
```
