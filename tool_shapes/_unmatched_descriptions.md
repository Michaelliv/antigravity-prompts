# Unmatched parameter descriptions (33)

Generic descriptions (e.g., "Always set to true.", short field labels) that could not be confidently attributed to one tool.

### 1.

```
Value of the reference
```

### 2.

```
index of the element to scroll on
```

### 3.

```
Unique identifier for the resource.
```

### 4.

```
The text to input into the element.
```

### 5.

```
ID of the command to get status for
```

### 6.

```
The absolute path to the file to edit.
```

### 7.

```
The exact command line string to execute.
```

### 8.

```
Name of the server to read the resource from.
```

### 9.

```
The current working directory for the command
```

### 10.

```
User-facing explanation of what this call does
```

### 11.

```
The page_id of the browser page to input text on.
```

### 12.

```
Name of the server to list available resources from.
```

### 13.

```
Absolute path to the node to edit, e.g /path/to/file
```

### 14.

```
The search term or pattern to look for within files.
```

### 15.

```
direction of the scroll. Options are left, right, up, down
```

### 16.

```
page_id of the Browser page to perform the drag operation on
```

### 17.

```
The page_id of the browser page to list network requests for.
```

### 18.

```
The page_id of the browser page containing the dropdown element.
```

### 19.

```
Path to list contents of, should be absolute path to a directory
```

### 20.

```
Optional, exclude files/directories that match the given glob patterns
```

### 21.

```
The type of cell: 'code', 'markdown', or 'raw'. Required for 'add' action.
```

### 22.

```
The path to search. This can be a directory or a file. This is a required parameter.
```

### 23.

```
Vertical scroll delta in pixels. Positive values scroll down, negative values scroll up.
```

### 24.

```
Horizontal scroll delta in pixels. Positive values scroll to the right, negative values scroll to the left.
```

### 25.

```
X coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions.
```

### 26.

```
Y coordinate of the pixel to scroll (0-999). Coordinates are scaled to a 1000x1000 grid and mapped to screen dimensions.
```

### 27.

```
An at most 20 character title describing the task in the imperative form. Will be displayed as the title of the tool in the step UI.
```

### 28.

```
Metadata updates if updating an artifact file, leave blank if not updating an artifact. Should be updated if the content is changing meaningfully.
```

### 29.

```
Optional map of filename to content for r commands. Reference as '10r myname' in expressions. Use this for appending code blocks to avoid escaping issues.
```

### 30.

```
The input to send to the command's stdin. Include newline characters (the literal character, not the escape sequence) if needed to submit commands. Exactly one of input and terminate must be specified.
```

### 31.

```
Optional, whether the full absolute path must match the glob pattern, default: only filename needs to match. Take care when specifying glob patterns with this flag on, e.g when FullPath is on, pattern '*.py' will not match to the file '/foo/bar.py', but pattern '**/*.py' will match.
```

### 32.

```
The resource types to list network requests for. When empty, all resource types are listed. Supported types: 'Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch', 'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'FedCM', 'Other'.
```

### 33.

```
Glob patterns to filter files found within the 'SearchPath', if 'SearchPath' is a directory. For example, '*.go' to only include Go files, or '!**/vendor/*' to exclude vendor directories. This is NOT for specifying the primary search directory; use 'SearchPath' for that. Leave empty if no glob filtering is needed or if 'SearchPath' is a single file.
```

