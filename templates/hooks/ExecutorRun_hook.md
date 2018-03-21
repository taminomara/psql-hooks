Called at any plan execution, after ExecutorStart.

Replaces [standard_ExecutorRun()](https://github.com/postgres/postgres/blob/src/backend/executor/execMain.c#L308)

*Inputs:*

* <i>QueryDesc *</i> <b>queryDesc</b> — query descriptor from the traffic cop.
* <i>ScanDirection</i> <b>direction</b> - if value is NoMovementScanDirection then nothing is done 
except to start up/shut down the destination.
* <i>uint64</i> <b>count</b> — count = 0 is interpreted as no portal limit, i.e., 
run to completion.  Also note that the count limit is only applied to 
retrieved tuples, not for instance to those inserted/updated/deleted by a ModifyTable plan node.
* <i>bool</i> <b>execute_once</b> — becomes equal to true after first execution.

*Output:*

This hook should not provide any output. However output tuples (if any) are sent to 
the destination receiver specified in the QueryDesc. 
The number of tuples processed at the top level can be found in estate->es_processed.