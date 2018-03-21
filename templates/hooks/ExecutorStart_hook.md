Called at the beginning of any execution of any query plan.

Note: when it set, replaces the [standard_ExecutorStart()](https://github.com/postgres/postgres/blob/src/backend/executor/execMain.c#L149), 
which contains a lot of predefined logic. 
Consider inclusion of the standard executor to the hook handler 
if you assume adding your logic atop.

This hook should not provide any output.

*Inputs:*

* <i>QueryDesc *</i> <b>queryDesc</b> — created by CreateQueryDesc, 
tupDesc field of the QueryDesc is filled in to describe the tuples that will be 
returned, and the internal fields (estate and planstate) are set up.
* <i>int</i> <b>eflags</b> — contains flag bits as described in executor.h.
