# `execute_notebook_or_edit`


## Parameter descriptions (4)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
Absolute path to the .ipynb notebook file.
```

### 2.
```
The cell content. Required for 'add' and 'update' actions.
```

### 3.
```
The 0-based index of the cell to operate on. Required for 'get', 'update', and 'delete' actions. Optional for 'add' (inserts at index, appends if omitted).
```

### 4.
```
The action to perform: 'list' (list all cells), 'get' (get cell content), 'add' (add new cell), 'update' (update cell content), 'delete' (delete cell), 'create' (create new notebook).
```
