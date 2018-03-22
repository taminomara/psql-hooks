Hook for overriding explain procedure for a single query.

This hook, if present, should generate explanation for the given query
using other `Explain*` functions and modifying the explain state.

The default behaviour is to plan query using `pg_plan_query()` and than
delegate printing to the `ExplainOnePlan()` function.

*Inputs:*

* <i>Query *</i> <b>query</b> — query that needs explanation.
* <i>int</i> <b>cursorOptions</b> — cursor options in form of a per-bit enum.
  See `CURSOR_OPT_*` macros for detailed documentations.
* <i>IntoClause *</i> <b>into</b> — target information for `SELECT INTO`,
  `CREATE TABLE AS`, and `CREATE MATERIALIZED VIEW`. `NULL` unless
  explaining the contents of a `CreateTableAsStmt`.
* <i>ExplainState *</i> <b>es</b> — current explain state. The hook is free to
  modify it in order to produce output.
* <i>const char *</i> <b>queryString</b> — an actual query string.
* <i>ParamListInfo</i> <b>params</b> — plan parameters.
* <i>QueryEnvironment *</i> <b>queryEnv</b> — context-specific values.

*Output:*

This hook does not produce any output.

