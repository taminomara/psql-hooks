Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.

*Inputs:*

Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

* <i>Oid</i> <b>indexId</b> — ...

*Output:*

Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?

*Use-cases:*

It you can think of any use-cases for this hook, spell it out. If no, delete this section.