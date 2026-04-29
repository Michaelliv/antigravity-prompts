# `grep`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
If true, performs a case-insensitive search.
```

### 2.
```
If true, returns each line that matches the query, including line numbers and snippets of matching lines (equivalent to 'git grep -nI'). If false, only returns the names of files containing the query (equivalent to 'git grep -l').
```

### 3.
```
If true, treats Query as a regular expression pattern with special characters like *, +, (, etc. having regex meaning. If false, treats Query as a literal string where all characters are matched exactly. Use false for normal text searches and true only when you specifically need regex functionality.
```
