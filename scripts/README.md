# Live RPC client for the Antigravity language server

While Antigravity is running, you can talk directly to its native language
server (the Go binary at `language_server_macos_arm`) over its local gRPC
port — same channel the Electron extension uses.

## Quick start

```sh
# With Antigravity running:
./agy-rpc.py Heartbeat
./agy-rpc.py FetchUserInfo
./agy-rpc.py GetUserStatus
./agy-rpc.py WellSupportedLanguages
./agy-rpc.py GetAllCascadeTrajectories
./agy-rpc.py GetCascadeTrajectory '{"cascadeId":"<id-from-GetAllCascadeTrajectories>"}'
```

## How it works

- The language server speaks **Connect protocol** (JSON over HTTPS) on a
  random localhost port. It also accepts gRPC and gRPC-Web.
- Self-signed TLS — the script uses `verify=False`.
- Auth is a CSRF token passed in the `x-codeium-csrf-token` header. The
  token is supplied to the LS as a `--csrf_token` command-line arg by
  the Electron extension at launch — readable via `ps`.
- Service: `exa.language_server_pb.LanguageServerService`.
- Method: any of the **202 RPCs** in
  [`../protos/third_party/jetski/language_server_pb/language_server.proto`](../protos/third_party/jetski/language_server_pb/language_server.proto).

## Discovery (what the script automates)

```sh
LSPID=$(pgrep -f language_server_macos_arm | head -1)
CSRF=$(ps -p $LSPID -o command= | sed -E 's/.*--csrf_token *([0-9a-f-]+).*/\1/')
PORT=$(lsof -nP -p $LSPID | awk '/LISTEN/{print $9}' | head -1 | sed 's/.*://')

curl -sk -X POST "https://127.0.0.1:$PORT/exa.language_server_pb.LanguageServerService/Heartbeat" \
  -H "Content-Type: application/json" \
  -H "Connect-Protocol-Version: 1" \
  -H "x-codeium-csrf-token: $CSRF" \
  -d '{}'
# {"lastExtensionHeartbeat":"2026-04-29T07:36:20.060056Z"}
```

## Notable RPCs

| RPC | What it returns |
|---|---|
| `Heartbeat` | `lastExtensionHeartbeat` timestamp |
| `FetchUserInfo` | minimal user settings |
| `GetUserStatus` | full account info: name, email, plan tier, model entitlements with quotas, allowed tiers per model |
| `WellSupportedLanguages` | language enum list |
| `GetWorkspaceInfos` | home/workspace paths |
| `GetAllCascadeTrajectories` | summaries of every conversation with id, status, step count |
| `GetCascadeTrajectory` | full step-by-step trajectory of one conversation (USER_INPUT → CONVERSATION_HISTORY → EPHEMERAL_MESSAGE → PLANNER_RESPONSE → tool calls → …) |
| `GetCascadeTrajectorySteps` | same, alternate shape |
| `GetCascadeTrajectoryGeneratorMetadata` | per-step model usage (tokens, model id, cache info, response IDs) |
| `GetUserTrajectoryDebug` | mainline trajectory metadata |
| `DumpPprof` | runtime profile dumps |
| `GetDebugDiagnostics` | recent log lines + outgoing API URLs hit |
| `StartCascade`, `SendUserCascadeMessage` | start / continue a conversation |
| `RevertToCascadeStep`, `CancelCascadeInvocation` | trajectory control |

A handful return `unimplemented`/501 (`GetUserSettings`, `GetCommandModelConfigs`); some are `deprecated` (`GetCascadeMemories`, `GetUserMemories`, `GetTermsOfService`).

## Limitations

- The **system prompt itself is not stored** in any trajectory step we found
  — it's assembled per-request and shipped to `cloudcode-pa.googleapis.com`.
  The trajectory has only the user's input (with `<USER_REQUEST>…</ADDITIONAL_METADATA>` envelope) and the model's responses.
- `cortex.proto` (which would give us byte-exact tool input message types) failed to extract via protodump
  due to `EDITION_2024` features — see top-level README. We have field
  names recovered from Go symbols (`tool_shapes/tools/`) but not message
  numbers / types / comments for that one file.
- The TLS cert is self-signed (verify=False). On Antigravity restart, the
  port and CSRF token both change — the script re-discovers them every run.

## Next step for actual model-prompt capture

The only authoritative source is the **outgoing request** the LS makes to
`cloudcode-pa.googleapis.com` — that body contains the system prompt + every
tool's full JSON schema, exactly as the model sees it. Capture via mitmproxy
with the system trust store set up.
