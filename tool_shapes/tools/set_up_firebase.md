# `set_up_firebase`

**Cortex step type:** `CortexStepSetUpFirebase`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (8)

```proto
message CortexStepSetUpFirebase {
  string error_message = 1;
  exa.cortex_pb.SetUpFirebaseErrorCode rpc_error_code = 6;
  string firebase_project_id = 7;
  exa.cortex_pb.SetUpFirebaseRequest request = 2;
  exa.cortex_pb.SetUpFirebaseResult result = 3;
  exa.cortex_pb.SetUpFirebaseAppConfig app_config = 4;
  string firestore_region = 8;
  string database_id = 9;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.

### `request`
```
Request body JSON
```
```
Set to true to request user feedback on this artifact.
```
```
The page_id of the browser page to get network request from.
```
