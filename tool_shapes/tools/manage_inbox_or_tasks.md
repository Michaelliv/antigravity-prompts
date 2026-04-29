# `manage_inbox_or_tasks`


## Parameter descriptions (5)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
The input to send to the task. Required when Action is 'send_input'.
```

### 2.
```
The ID of the message to read. Required when Action is 'read'.
```

### 3.
```
The task ID to manage. Required when Action is 'kill', 'status', or 'send_input'.
```

### 4.
```
The action to perform: 'list' (list all messages with metadata) or 'read' (read full content of a specific message).
```

### 5.
```
The action to perform: 'list' (list all running tasks), 'kill' (cancel the task), 'status' (check the task status and log URI), 'send_input' (send input to a running task).
```
