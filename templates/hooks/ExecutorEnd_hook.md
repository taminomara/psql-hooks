Called at the end of execution of any query plan.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — query descriptor from the traffic cop.

This hook should not provide any output.
