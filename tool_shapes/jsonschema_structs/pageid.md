# `ParseToolArgs` struct @ 0x303397d

Recovered byte-exact from a Go generic instantiation symbol in the
language-server binary. This is the JSON-schema-source struct passed
to `utils.ToJsonSchemaString` / `utils.ParseToolArgs`.

## Fields

- `PageID` _string_
  - `jsonschema_description` = `page_id of the Browser page to perform the drag operation on`

- `Waypoints` _[]google3/third_party/jetski/cortex/tools/browser/browser.waypoint_
  - `jsonschema_description` = `A series of pixel coordinates defining the drag path. When this tool call is executed, the first waypoint will be clicked, then the mouse will be dragged to each subsequent waypoint in the provided order, and finally the mouse will be released at the last waypoint.`

## Raw body

```
 PageID string "jsonschema_description:\"page_id of the Browser page to perform the drag operation on\""; Waypoints []google3/third_party/jetski/cortex/tools/browser/browser.waypoint "jsonschema_description:\"A series of pixel coordinates defining the drag path. When this tool call is executed, the first waypoint will be clicked, then the mouse will be dragged to each subsequent waypoint in the provided order, and finally the mouse will be released at the last waypoint.\"" 
```
