# Postgresql hooks documentation

{% include "templates/Header.md" %}

{% for section in sections -%}
* [{{ section.name }}](#{{ section.slug }})
{% endfor %}

{% for section in sections -%}
## [{{ section.name }}](Detailed.md#{{ section.slug }})

{{ section.short_desc }}

{% for hook in section.hooks -%}
* [{{ hook.name }}](Detailed.md#{{ hook.name }}) — {{ make_short_description(hook) }}
{% endfor %}
{% endfor %}
