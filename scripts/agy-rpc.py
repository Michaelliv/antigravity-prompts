#!/usr/bin/env python3
"""
agy-rpc.py — call any LanguageServerService RPC on a running Antigravity
language server using the Connect protocol (JSON over HTTPS).

Discovers the running LS, extracts its CSRF token from process args, and
routes calls to https://127.0.0.1:<port>/exa.language_server_pb.LanguageServerService/<RPC>

Usage:
  ./agy-rpc.py <RpcName> [json-body]

Examples:
  ./agy-rpc.py Heartbeat
  ./agy-rpc.py FetchUserInfo
  ./agy-rpc.py GetUserStatus
  ./agy-rpc.py GetCascadeTrajectory '{"cascadeId":"<id>"}'
  ./agy-rpc.py GetAllCascadeTrajectories
  ./agy-rpc.py WellSupportedLanguages

Discover RPC names: see protos/third_party/jetski/language_server_pb/language_server.proto
(202 RPCs).
"""
import json, os, re, ssl, subprocess, sys, urllib.request

SERVICE = "exa.language_server_pb.LanguageServerService"

def discover():
    out = subprocess.run(["pgrep", "-f", "language_server_macos_arm"],
                         capture_output=True, text=True).stdout.split()
    if not out:
        sys.exit("error: language_server_macos_arm not running. Open Antigravity first.")
    pid = out[0]
    cmd = subprocess.run(["ps","-p",pid,"-o","command="], capture_output=True, text=True).stdout
    csrf = re.search(r"--csrf_token\s+(\S+)", cmd)
    if not csrf:
        sys.exit(f"error: no --csrf_token in process args (pid {pid})")
    csrf = csrf.group(1)
    lsof = subprocess.run(["lsof","-nP","-p",pid], capture_output=True, text=True).stdout
    ports = re.findall(r"127\.0\.0\.1:(\d+) \(LISTEN\)", lsof)
    if not ports:
        sys.exit(f"error: language server has no listening ports (pid {pid})")
    return pid, int(ports[0]), csrf  # first port is HTTPS gRPC

def call(rpc, body):
    pid, port, csrf = discover()
    url = f"https://127.0.0.1:{port}/{SERVICE}/{rpc}"
    req = urllib.request.Request(url,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Connect-Protocol-Version": "1",
            "x-codeium-csrf-token": csrf,
        }, method="POST")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    rpc = sys.argv[1]
    body = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    code, resp = call(rpc, body)
    try:
        print(json.dumps(json.loads(resp), indent=2))
    except json.JSONDecodeError:
        print(resp)
    sys.exit(0 if code < 400 else 1)

if __name__ == "__main__":
    main()
