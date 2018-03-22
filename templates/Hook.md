Short description of this hook.

Remember to mention when it's called, what should it do, what inputs supplied to this hook,
what output is expected and (shortly) how postgres changes its behavior based on received output.
It may be helpful to mention any common use-cases for this hook or some
extensions that are using this hook.

*Inputs:*

{% if hook.type.inputs -%}
Briefly describe hook inputs. Are inputs preprocessed somehow before calling the hook?
Are there any special input states? Can they be null (e.g. `nullptr`)?

{% for input in hook.type.inputs -%}
* <i>{{ input.type }}</i> <b>{{ input.name }}</b> — ...
{% endfor %}
{%- else -%}
There are no inputs for this hook. Is there a global state this hook should introspect?
{%- endif %}
*Output:*

{% if hook.type.output != 'void' -%}
Describe hook output. Are there any constraints for the output value?
How postgres changes its behavior based on received output?
Are there any special cases for output, e.g. returning `-1` or `nullptr`?
Are there any mutable inputs this hook should change?
{%- endif %}
