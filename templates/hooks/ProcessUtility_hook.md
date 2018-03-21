Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>PlannedStmt *</i> <b>pstmt</b> — ...
* <i>const char *</i> <b>queryString</b> — ...
* <i>ProcessUtilityContext</i> <b>context</b> — ...
* <i>ParamListInfo</i> <b>params</b> — ...
* <i>QueryEnvironment *</i> <b>queryEnv</b> — ...
* <i>DestReceiver *</i> <b>dest</b> — ...
* <i>char *</i> <b>completionTag</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.