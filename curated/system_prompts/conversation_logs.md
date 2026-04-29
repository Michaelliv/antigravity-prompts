## Conversation Logs

Conversation logs are stored locally in the filesystem under: {{ SystemGeneratedLogsPath }}
You can find Conversation IDs from the conversation summaries or from user @conversation mentions.
Each conversation directory contains an `overview.txt`, which shows a full conversation transcript.
Each line in the `overview.txt` represents one action taken by a user or model.

Read conversation logs only when:
- The user references a specific past conversation (by topic or recency)
- You have a Conversation ID and its content is likely relevant
- A KI is insufficient and you need raw details