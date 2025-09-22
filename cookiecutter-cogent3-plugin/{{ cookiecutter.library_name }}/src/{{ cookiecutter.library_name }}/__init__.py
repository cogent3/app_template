# Auto-generated imports for cogent3 apps
{%- set lib_name = cookiecutter.library_name.strip().lower().replace(' ', '_') %}
from {{ lib_name }}.app import (
{%- for app in cookiecutter.apps.split(',') %}
    {{ app.strip().lower().replace(' ', '') }}_class,
    {{ app.strip().lower().replace(' ', '') }}_func{{ "," if not loop.last else "" }}
{%- endfor %}
)
