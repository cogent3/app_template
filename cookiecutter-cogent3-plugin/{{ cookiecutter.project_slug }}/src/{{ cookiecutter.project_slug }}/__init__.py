{% set apps_list = cookiecutter.apps.split(',') %}
{% for app_name in apps_list %}from .{{ app_name.strip().lower().replace(' ', '_') }} import {{ app_name.strip().title().replace(' ', '') }}
{% endfor %}
