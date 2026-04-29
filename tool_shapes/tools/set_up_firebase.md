# `set_up_firebase`

**Cortex step type:** `CortexStepSetUpFirebase`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

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

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
