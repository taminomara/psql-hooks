Hook for intercepting end of a function. 

This hook is called at the end of PLpgSQL function.
Can be used as a function callback.

The hook should not provide any output. 

*Inputs:*

* <i>PLpgSQL_execstate *</i> <b>estate</b> — runtime execution data.
* <i>PLpgSQL_function *</i> <b>func</b> — PLpgSQL compiled function.