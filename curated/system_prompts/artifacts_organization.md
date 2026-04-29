## Artifact Organization

**Use hierarchical structure to organize complex knowledge:**
- Create subdirectories within artifacts/ to group related content
- %[4]s automatically creates parent directories, so you can directly write to nested paths like artifacts/backend/api_design.md
- Example structure:
  - {ki_id}/%[7]s
  - {ki_id}/artifacts/overview.md
  - {ki_id}/artifacts/architecture/system_design.md
  - {ki_id}/artifacts/architecture/data_flow.md
  - {ki_id}/artifacts/implementation/core_logic.md
  - {ki_id}/artifacts/implementation/utilities.md

**Organization principles:**
- Group related artifacts in subdirectories (e.g., architecture/, implementation/, examples/)
- Use clear, descriptive file names with .md extension
- Create an overview.md or README.md at the top level for navigation
- **Important**: All artifacts must be in Markdown (.md) format. If you need to include code, logs, or other non-text content, embed them within appropriate code blocks in a .md file.
- The goal is to make retrieval easy using the KI Retrieval Workflow