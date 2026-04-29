## Critique (Google's Piper Code Review)

**Navigation:**
- **Dashboard:** Shows CLs needing your attention.
- **CL Page:** Main page for a changelist.
  - **Files Tab:** Lists changed files. Click to see diffs and add inline comments.
  - **Analysis Tab:** Shows presubmit checks, linter warnings, TAP/Guitar test results, coverage. Click test results for links to Sponge or Test Fusion logs.
  - **Comments:** Displayed inline and in summary at bottom.

**Comments:**
- Find comments inline, in sidebar (Shift+U), or in History section.
- Click "Reply" to draft a response. Use "Done" for implemented suggestions, "Ack" for acknowledged FYIs.
- Uncheck "Resolve" if discussion needs to continue.
- Draft replies are saved but not visible until you click "Reply" -> "Send".

**Submission:**
1. Get LGTM from reviewers and Approval from code owners.
2. Resolve all comments.
3. Pass all presubmit checks in Analysis tab.
4. Click "Submit" button.

---

## Gerrit (Git-on-Borg Code Review)

**Navigation:**
- **Dashboard:** Shows changes needing attention.
- **Change Screen:** Main page for a Gerrit change.
  - **Files Tab:** Lists changed files with diffs.
  - **Patch Sets:** Dropdown to compare different versions.
  - **Labels/Scores:** Shows Code-Review (+2 approved, +1 good, -1 needs work, -2 veto) and Verified status.
  - **CI Results:** Look for bot comments with links to build/test logs.

**Comments:**
- Comments appear inline in file diffs and in change log.
- Click "Reply" on a comment to respond.
- Check "Resolved" box to close the thread.
- Click "Reply" button at top, then "Send" to publish all draft comments.

**Submission:**
1. Get required label scores from reviewers.
2. Ensure CI checks pass (Verified +1).
3. Meet all submit requirements.
4. Click "Submit" when enabled.

## Finding Louhi Logs for Gerrit Changes

When Continuous Integration (CI) is run by Louhi on Gerrit changes, results and logs can typically be accessed as follows:

1. **Navigate to the Gerrit Change:** Open the specific Change List (CL) in the Gerrit UI.

2. **Go to the "Checks" Tab:** If the host has the Treetop plugin enabled for Louhi integration, there will be a "Checks" tab on the Gerrit change page. This tab displays the status of various presubmit checks, including Louhi flows.

3. **Locate the Louhi Job:** Within the "Checks" tab, find the row corresponding to the Louhi presubmit flow you are interested in. Failing jobs will be highlighted (e.g., with a red icon).

4. **Access Execution Details:** Click on the link or button associated with the Louhi job to view more details. This link, often labeled something like "Details", "View Logs", or containing the flow name, will navigate you directly to the specific execution page within the Louhi UI.

5. **Analyze in Louhi:**
   - On the Louhi execution page, identify the failed stage(s) in the pipeline.
   - Click on the failed stage to expand it.
   - Look for tabs to the detailed logs, "Logs", which will often show an Open in Sponge button. This will take you to the markdown file of the logs.

**Miscellaneous Notes:**

- **Comments:** Louhi may also post comments directly on the Gerrit CL, summarizing results and providing direct links to the Louhi execution.
- **Labels:** Failing Louhi flows often result in a negative vote on a Gerrit label (e.g., Verified -1). The most reliable link to the logs will be in the Checks tab or comments.
- **Optional Tests:** CL's on Gerrit may fail tests labelled as optional. These tests do not block submission.
**Primary Path:** Gerrit Change -> "Checks" Tab -> Click on the specific Louhi presubmit job run -> Link to Louhi UI -> Find failed stage -> Logs tab -> Sponge link