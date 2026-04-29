# Failed Replacements
The following replacement blocks failed to apply to the file. Remember that a start_line or end_line of 0 means the line number is unspecified and should be ignored:
<failed_replacements>
{{.ReplacementInfos}}
</failed_replacements>

# Full File Content
This is the full content of the file that should be edited. Note that the file may already contain some of the changes from the edit goal (valid `replacement_chunk`s may have already been applied successfully).
The file content has been modified to include a line number before every line, in the format: <line_number>: <original_line>. The line numbers are for reference only and should not be included in in the corrected replacement chunks.
<file>
{{.FileContent}}
</file>

# Your Task
Based on the information above, please identify the reasons for the failed replacements, and provide a corrected json list of `replacement_chunk`s, explaining your changes. The `search_target` blocks must be an exact match of a substring in the file.

Note: You must return exactly one corrected replacement chunk for each failed replacement chunk. They must be in the same order, and keep their original chunk_index.

Please output only the improved replacement chunks in the following XML format, and nothing else:

<corrected_replacement_chunk>
<chunk_index>
int
</chunk_index>
<explanation_of_changes>
...
</explanation_of_changes>
<new_search_target>
...
</new_search_target>
<new_replacement_block>
...
</new_replacement_block>
<start_line>
int
</start_line>
<end_line>
int
</end_line>
</corrected_replacement_chunk>
...