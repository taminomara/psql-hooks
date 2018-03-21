Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>QueryDesc *</i> <b>queryDesc</b> — ...
* <i>ScanDirection</i> <b>direction</b> — ...
* <i>uint64</i> <b>count</b> — ...
* <i>bool</i> <b>execute_once</b> — ...

*Output:*

This hook does not produce any output. Describe, what exactly it should do.
Maybe, it should throw an error via a standard `ereport(ERROR, ...)`?
Maybe, there are some mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.