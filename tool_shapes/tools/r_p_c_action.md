# `r_p_c_action`

**Cortex step type:** `CortexStepRPCAction`
**Source:** `third_party/jetski/cortex_pb/cortex.proto`

## Fields (5)

```proto
message CortexStepRPCAction {
  string service_name = 1;
  string method_name = 2;
  google.protobuf.Struct arguments = 3;
  string error_message = 4;
  google.protobuf.Struct result = 5;
}
```

## Field descriptions

From `jsonschema_description:` tags in the binary, matched by field name.
