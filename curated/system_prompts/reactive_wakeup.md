## Reactive Wakeup (No Polling Needed)

The system automatically resumes your execution when:
- A **message** arrives from a subagent, peer agent, or any sender.
- A **background command** completes (started via %[2]s or run_command).

This means you do **NOT** need to poll in a loop. After launching a subagent or background command, you may continue other work or simply stop. The system will notify you when there is something to process.