# `find`

**Cortex step type:** `CortexStepFind`
**Package:** `google3/third_party/jetski/cortex_pb/cortex_go_proto`

## Cortex step fields (14)

Field names recovered from `(*CortexStepFind).Get*` symbols (includes both inputs and outputs).

- `CommandRun`
- `Excludes`
- `Extensions`
- `FindError`
- `FullPath`
- `Includes`
- `MaxDepth`
- `Pattern`
- `RawOutput`
- `SearchDirectory`
- `TotalResults`
- `TruncatedOutput`
- `TruncatedTotalResults`
- `Type`


## Parameter descriptions (3)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Optional, type filter, enum=file,directory,any
```

### 2.
```
Optional, Pattern to search for, supports glob format
```

### 3.
```
Optional, file extensions to include (without leading .), matching paths must match at least one of the included extensions
```
