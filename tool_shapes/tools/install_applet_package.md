# `install_applet_package`

**Cortex step type:** `CortexStepInstallAppletPackage`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepInstallAppletPackage {
  string package_name = 1;
  string error_message = 2;
  string logs = 3;
  bool is_dev_dependency = 4;
  repeated string package_names = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
