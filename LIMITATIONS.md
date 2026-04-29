# Limitations & what's still missing

## Summary

We have **121 tool input proto messages** (from `cortex.proto`) and **178 parameter
description strings** (from `jsonschema_description:` Go struct tags), with **40
high-fidelity (field-name, field-type, tag) triples** recovered from `go.shape.struct`
generic-instantiation strings. The remaining ~138 descriptions belong to non-generic
Go types whose `__go_type` reflect layout we couldn't walk for this build.

## Why we can't (easily) get the remaining bits

### 1. BoringCrypto blocks mitmproxy on the model API endpoint

The binary is built with Google's `boringcrypto` Go variant
(visible in the strings: `crypto/internal/fips140`, `boring.PublicKeyECDH`,
`fips140: verification mismatch`). Its TLS stack uses its own hardcoded root
certificate pool and **does not consult `/Library/Keychains/System.keychain`**.

Empirically, with `HTTPS_PROXY=http://127.0.0.1:8080` set in the language server's
environment and the mitmproxy CA installed in macOS system trust:

- `antigravity-unleash.goog` → ✅ intercepted cleanly
- `daily-cloudcode-pa.googleapis.com` → ✅ intercepted cleanly
- **`cloudcode-pa.googleapis.com`** → ❌ TLS handshake aborted by client.
  mitmproxy log: *"Client TLS handshake failed. … this may indicate that the
  client does not trust the proxy's certificate."*

The `cloudcode-pa.googleapis.com` endpoint is precisely where the assembled
prompt + tool schemas are sent. Its TLS stack uses BoringCrypto's pinned roots.

To bypass:
- DYLD library interposition to hook `boring.X509_verify_cert`
- Static binary patch of the cert-verify function (NOP)
- lldb attach + breakpoint in `(*Transport).RoundTrip` to dump the request body
  before TLS

### 2. GoReSym / redress can't parse moduledata

Both tools fail on this binary because Google's internal Go 1.27 toolchain
relocates the pclntab from `__gopclntab` to `__lrodata_gopcln`. We worked
around that for **function symbols** by hex-renaming the section name in a
copy of the binary (16-byte `__lrodata_gopcln` → `__gopclntab\0\0\0\0\0`),
which gave us 95,300 user-function names. But the **moduledata struct layout
itself** also differs from stock Go in ways gore@v0.13.27 doesn't handle:

```
GetTypes: failed to get types data section: the length of module data
section is to big: address 0x1049e8a10, base 0x1049e8a10,
length 0xfffffffefb9b9cd0
```

That blocks `gore.GoFile.GetTypes()` from walking the type table.

### 3. Hand-rolled reflect-name parsing got 0 hits

The Go runtime stores struct field names + tags as packed byte sequences:
`[flags][varint nlen][name][varint tlen][tag]`. We scanned the binary for
each `jsonschema_description:` marker and tried to walk backwards to find
this layout — none matched. Possibly Google's build uses a slightly
different encoding (extra fields, different varint scheme, or names stored
in a separate section indexed by nameOff).

### 4. cortex.proto uses Edition 2024

`protodump` failed on it because protobuf-go in protodump's deps doesn't
support Edition 2024. We worked around with a custom locate-trim-parse:
search for the `\x0a\x29third_party/jetski/cortex_pb/cortex.proto` tag
prefix, walk forward consuming valid proto wire-format until invalid, then
parse with Python `google.protobuf` — which raises on the EDITION_2024
enum value but populates the FileDescriptorProto object with everything
preceding it. We get 421 messages + 70 enums.

## What would close the gap

The cleanest path to **byte-exact tool definitions as the model sees
them** is one of:

1. **Patch the binary** to disable BoringCrypto's cert pinning, then
   mitmproxy a single chat. ~30 min reverse engineering.
2. **lldb scripted dump** of the outgoing request from a running LS.
3. **Update `protobuf-go` and `gore`** to a version supporting Edition
   2024 + Go 1.27 google3 moduledata layout.

Until one of those: this repo is the best static reconstruction
achievable.
