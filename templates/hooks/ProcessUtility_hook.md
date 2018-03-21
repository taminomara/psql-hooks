Hook for the ProcessUtility.

Replaces [standard_ProcessUtility()](https://github.com/postgres/postgres/blob/src/backend/tcop/utility.c#L375)

This hook should not provide any output.

*Inputs:*

* <i>PlannedStmt *</i> <b>pstmt</b> — PlannedStmt wrapper for the utility statement
* <i>const char *</i> <b>queryString</b> — original source text of command, 
may be passed multiple times when processing a query string
containing multiple semicolon-separated statements. pstmt->stmt_location and pstmt->stmt_len 
indicates the substring containing the current statement.
* <i>ProcessUtilityContext</i> <b>context</b> — identifies source of statement 
(toplevel client command, non-toplevel client command, subcommand of a larger utility command)
* <i>ParamListInfo</i> <b>params</b> — parameters of an execution.
* <i>QueryEnvironment *</i> <b>queryEnv</b> — execution environment, optional, can be NULL.
* <i>DestReceiver *</i> <b>dest</b> — results receiver.
* <i>char *</i> <b>completionTag</b> — points to a buffer of size COMPLETION_TAG_BUFSIZE 
in which to store a command completion status string