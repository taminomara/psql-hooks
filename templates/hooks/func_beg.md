Hook for intercepting post-init phase. 

This hook is called when we start PLpgSQL function, after we've initialized 
the local variables.
The hook can be used for pre-validation of a function arguments. 

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_function *</i> <b>func</b> — PLpgSQL compiled function.