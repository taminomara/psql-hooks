# Postgresql hooks documentation

{% include "templates/DetailedHeader.md" %}

{% for section in sections -%}
* [{{ section.name }}](#{{ section.slug }})
{% endfor %}

{% for section in sections -%}
## {{ section.name }}

{{ section.long_desc }}

{% for hook in section.hooks %}
<a name="{{ hook.name }}" href="#{{ hook.name }}">#</a> <i>{{ hook.type.output }}</i> <b>{{ hook.name }}</b>({% for input in hook.type.inputs %}{{ input.name }}{% if loop.nextitem is defined %}, {% endif %}{% endfor %}) [<>]({{ hook.source_link }} "Source")

{% include "templates/hooks/" + hook.name + ".md" %}

{% endfor %}
{% endfor %}
