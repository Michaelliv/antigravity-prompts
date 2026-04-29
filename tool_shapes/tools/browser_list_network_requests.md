# `browser_list_network_requests`

**Cortex step type:** `CortexStepBrowserListNetworkRequests`

**Source:** `third_party/jetski/cortex_pb/cortex.proto` (byte-exact, recovered from the embedded `FileDescriptorProto`)

## Proto schema

```proto
message CortexStepBrowserListNetworkRequests {
  string page_id = 1;
  bool include_preserved_requests = 2;
  repeated string resource_types = 3;
  exa.codeium_common_pb.BrowserPageMetadata page_metadata = 4;
  string network_requests = 5;
}
```

## Field descriptions

See [`../byte_exact_field_index.md`](../byte_exact_field_index.md) for byte-exact `(field_name, jsonschema tag)` records recovered from Go reflect-name tables in the binary. Cortex-step proto messages and JSON-schema tool-arg structs are different namespaces, so a clean static attribution from one to the other is not possible. Match by reading the description text against this tool's purpose.
