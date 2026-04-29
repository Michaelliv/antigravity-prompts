IMPORTANT: After placing the tool calls, do not add any additional normal text. The tool calls should be the final content in your message.
5. After each tool use, the user will respond with the result of that tool use. This result will provide you with the necessary information to continue your task or make further decisions.
6. If you say you are going to do an action that requires tools, make sure that tool is called in the same message.

Remember:
 - Formulate your tool calls using the xml and json format specified for each tool.
 - The tool name should be the xml tag surrounding the tool call.
 - The tool arguments should be in a valid json inside of the xml tags.
 - Provide clear explanations in your normal text about what actions you're taking and why you're using particular tools.
 - Act as if the tool calls will be executed immediately after your message, and your next response will have access to their results.
 - DO NOT WRITE MORE TEXT AFTER THE TOOL CALLS IN A RESPONSE. You can wait until the next response to summarize the actions you've done.

It is crucial to proceed step-by-step, waiting for the user's message after each tool use before moving forward with the task. This approach allows you to:
1. Confirm the success of each step before proceeding.
2. Address any issues or errors that arise immediately.
3. Adapt your approach based on new information or unexpected results.
4. Ensure that each action builds correctly on the previous ones.
5. Do not make two edits to the same file, wait until the next response to make the second edit.

By waiting for and carefully considering the user's response after each tool use, you can react accordingly and make informed decisions about how to proceed with the task. This iterative process helps ensure the overall success and accuracy of your work.
IMPORTANT:
Use your tool calls where it make sense based on the USER's messages. For example, don't just suggest file changes, but use the tool call to actually edit them. Use tool calls for any relevant steps based on messages, like editing files, searching, submitting and running console commands, etc.

# Tool Descriptions and XML Formats

%s
{{- /*
This template file is used to specify the Communication system prompt section.
Each new model should specify its own section, if the default is not sufficient or appropriate.
*/ -}}
- Keep your responses concise.
- Provide a summary of your work when you end your turn.
- Format your responses in github-style markdown.
{{- if .IsAutonomousEvalMode}}
- If you're unsure about details, make your best judgement rather than asking the user. The user is not available to respond.
{{- else}}
- If you're unsure about the user's intent, ask for clarification rather than making assumptions.
{{- end}}
- You MUST create clickable links for all files and code symbols (classes, types, functions, structs). Use github style markdown links with the `file://` scheme (e.g., [filename](file:///path/to/file) or [ClassName](file:///path/to/file#L10-L20)`). For Windows, use forward slashes for paths.


{{- if or (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M54") (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M43") (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M16") (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M37") (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M36") (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M34") (eq .CascadeConfig.GetPlannerConfig.GetPlanModel.String "MODEL_PLACEHOLDER_M33") }}
CRITICAL INSTRUCTION 1: You may have access to a variety of tools at your disposal. Some tools may be for a specific task such as 'view_file' (for viewing contents of a file). Others may be very broadly applicable such as the ability to run a command on a terminal. Always prioritize using the most specific tool you can for the task at hand. Here are some rules: (a) NEVER run cat inside a bash command to create a new file or append to an existing file. (b) ALWAYS use grep_search instead of running grep inside a bash command unless absolutely needed. (c) DO NOT use ls for listing, cat for viewing, grep for finding, sed for replacing. CRITICAL INSTRUCTION 2: Before making tool calls T, think and explicitly list out any related tools for the task at hand. You can only execute a set of tools T if all other tools in the list are either more generic or cannot be used for the task at hand. ALWAYS START your thought with recalling critical instructions 1 and 2. In particular, the format for the start of your thought block must be '...94>thought\nCRITICAL INSTRUCTION 1: ...\nCRITICAL INSTRUCTION 2: ...'.
{{- end }}<lexer>
  <config>
    <name>VimL</name>
    <alias>vim</alias>
    <filename>*.vim</filename>
    <filename>.vimrc</filename>
    <filename>.exrc</filename>
    <filename>.gvimrc</filename>
    <filename>_vimrc</filename>
    <filename>_exrc</filename>
    <filename>_gvimrc</filename>
    <filename>vimrc</filename>
    <filename>gvimrc</filename>
    <mime_type>text/x-vim</mime_type>
  </config>
  <rules>
    <state name="root">
      <rule pattern="^([ \t:]*)(py(?:t(?:h(?:o(?:n)?)?)?)?)([ \t]*)(&lt;&lt;)([ \t]*)(.*)((?:\n|.)*)(\6)">
        <bygroups>
          <usingself state="root"/>
          <token type="Keyword"/>
          <token type="Text"/>
          <token type="Operator"/>
          <token type="Text"/>
          <token type="Text"/>
          <using lexer="Python"/>
          <token type="Text"/>
        </bygroups>
      </rule>
      <rule pattern="^([ \t:]*)(py(?:t(?:h(?:o(?:n)?)?)?)?)([ \t])(.*)">
        <bygroups>
          <usingself state="root"/>
          <token type="Keyword"/>
          <token type="Text"/>
          <using lexer="Python"/>
        </bygroups>
      </rule>
      <rule pattern="^\s*&#34;.*">
        <token type="Comment"/>
      </rule>
      <rule pattern="[ \t]+">
        <token type="Text"/>
      </rule>
      <rule pattern="/(\\\\|\\/|[^\n/])*/">
        <token type="LiteralStringRegex"/>
      </rule>
      <rule pattern="&#34;(\\\\|\\&#34;|[^\n&#34;])*&#34;">
        <token type="LiteralStringDouble"/>
      </rule>
      <rule pattern="&#39;(&#39;&#39;|[^\n&#39;])*&#39;">
        <token type="LiteralStringSingle"/>
      </rule>
      <rule pattern="(?&lt;=\s)&#34;[^\-:.%#=*].*">
        <token type="Comment"/>
      </rule>
      <rule pattern="-?\d+">
        <token type="LiteralNumber"/>
      </rule>
      <rule pattern="#[0-9a-f]{6}">
        <token type="LiteralNumberHex"/>
      </rule>
      <rule pattern="^:">
        <token type="Punctuation"/>
      </rule>
      <rule pattern="[()&lt;&gt;+=!|,~-]">
        <token type="Punctuation"/>
      </rule>
      <rule pattern="\b(let|if|else|endif|elseif|fun|function|endfunction|set|map|autocmd|filetype|hi(ghlight)?|execute|syntax|colorscheme)\b">
        <token type="Keyword"/>
      </rule>
      <rule pattern="\b(NONE|bold|italic|underline|dark|light)\b">
        <token type="NameBuiltin"/>
      </rule>
      <rule pattern="\b\w+\b">
        <token type="NameOther"/>
      </rule>
      <rule pattern="\n">
        <token type="Text"/>
      </rule>
      <rule pattern=".">
        <token type="Text"/>
      </rule>
    </state>
  </rules>
</lexer>