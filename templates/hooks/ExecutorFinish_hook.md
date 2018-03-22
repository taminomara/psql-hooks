Called after the last ExecutorRun call

Replaces [standard_ExecutorFinish()](https://github.com/postgres/postgres/blob/src/backend/executor/execMain.c#L408)

*Inputs:*

* <i>QueryDesc *</i> <b>queryDesc</b> — query descriptor from the traffic cop.