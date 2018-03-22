Hook for intercepting PLpgSQL function pre-init phase. 

This hook is called when we start a function before we've initialized 
the local variables defined by the function.
Can be useful for time measuring of а function initialization in tandem 
with [func_beg()](Detailed.md#func_beg) and for measuring total execution time 
with the help of [func_end()](Detailed.md#func_end).

Before any call to func_setup, PLpgSQL fills in the error_callback 
and assign_expr fields with pointers to its own plpgsql_exec_error_callback 
and exec_assign_expr functions.
 
The hook should not provide any output. 

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_function *</i> <b>func</b> — PLpgSQL compiled function.