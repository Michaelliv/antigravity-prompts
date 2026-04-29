# `replace_file_content`


## Parameter descriptions (7)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The content to replace the target content with.
```

### 2.
```
A single contiguous chunk to replace. For non-contiguous edits, use the multi_replace_file_content tool instead.
```

### 3.
```
A list of chunks to replace. It is best to provide multiple chunks for non-contiguous edits if possible. This must be a JSON array, not a string.
```

### 4.
```
If true, multiple occurrences of 'targetContent' will be replaced by 'replacementContent' if they are found. Otherwise if multiple occurences are found, an error will be returned.
```

### 5.
```
The starting line number of the chunk (1-indexed). Should be at or before the first line containing the target content. Must satisfy 1 <= StartLine <= EndLine. The target content is searched for within the [StartLine, EndLine] range.
```

### 6.
```
The ending line number of the chunk (1-indexed). Should be at or after the last line containing the target content. Must satisfy StartLine <= EndLine <= number of lines in the file. The target content is searched for within the [StartLine, EndLine] range.
```

### 7.
```
The exact string to be replaced. This must be the exact character-sequence to be replaced, including whitespace. Be very careful to include any leading whitespace otherwise this will not work at all. This must be a unique substring within the file, or else it will error.
```
