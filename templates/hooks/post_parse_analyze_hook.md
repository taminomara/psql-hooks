Called when parse analyze goes, right after performing transformTopLevelStmt().

Used in several internal methods: 
[pg_analyze_and_rewrite_params()](https://github.com/postgres/postgres/blob/src/backend/tcop/postgres.c#L686), 
[parse_analyze()](https://github.com/postgres/postgres/blob/src/backend/parser/analyze.c#L100).

*Inputs:*

* <i>ParseState *</i> <b>pstate</b> — parse state filled by query_string and queryEnv.  
* <i>Query *</i> <b>query</b> — output result of the transformTopLevelStmt().