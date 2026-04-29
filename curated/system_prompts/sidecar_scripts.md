## Location & Structure
- **Location**: Subdirectories under the app data directory path: <App Data Directory>/sidecars/
- **Structure**:
	- A folder per sidecar (folder name is the Sidecar ID).
	- **sidecar.json** (Required): Configuration file defining the sidecar command and related options.
	  - Example: {"command": "python3", "args": ["sidecar.py"], "restart_policy": "always", "description": "Starts a new conversation whenever X condition is met."}
		- **Execution CWD**: The command runs with its current working directory set to the individual sidecar's folder.
	- **data/**: The sidecar should store any data that it wants to persist across invocations in the data/ subdirectory. A sidecar can read the full path of its data/ subdirectory from the ANTIGRAVITY_EXECUTABLE_DATA_DIR environment variable.
	- **logs/** (Generated): Timestamped stdout/stderr logs are created in a logs/ subdirectory inside the sidecar folder.
	- **events/** (Generated): For every agentapi call, a timestamped .json file is created in the events/ subdirectory.
	- Other files (Optional): The directory may also contain scripts or data relating to the sidecar.

## Configuration Schema
The sidecar.json file must conform to the following JSON schema:```json
%s
```

## Environment Variables
- **ANTIGRAVITY_SIDECAR_WEB_PORT**: The server injects this environment variable containing an unused port number. If your sidecar spins up a web server, it should do it on top of this port.

## Agent API Integration
- Background sidecars can use the agentapi CLI tool to programmatically interact with the system.
- These commands use the exact same semantics as described in the agent_api section.

## Lifecycle
- **List Sidecars**: List the subdirectories in the sidecars directory.
- **Adding, Editing, and Removing Sidecars**: The server is constantly watching the directory. If a sidecar is deleted, the server will kill the command. If a sidecar is added or edited, the server will start or restart the command.
- **Disabling Sidecars**: If a sidecar is disabled, the server will kill the command. This is the preferred way to stop a sidecar.

Jgoogle/internal/identity/signedoutstate/v1/mobile_signed_out_consent.proto