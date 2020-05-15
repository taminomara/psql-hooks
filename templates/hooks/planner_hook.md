Called in query optimizer entry point.

If set, replaces standard planner. Consider inclusion of the standard planner to hook 
if this hook assuming just pre-process or post-process for builtin planner.

*Inputs:*

* <i>Query *</i> <b>parse</b> — query text.
* <i>int</i> <b>cursorOptions</b>
* <i>ParamListInfo</i> <b>boundParams</b>
