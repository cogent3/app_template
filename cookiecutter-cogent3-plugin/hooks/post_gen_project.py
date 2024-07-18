import os
from jinja2 import Template

# Load the template content
app_template_content = """
{% raw %}
from cogent3.app.composable import define_app

@define_app()
class {{ app_class_name }}:
    def main(self, data: str) -> str:
        return data
{% endraw %}
"""

test_template_content = """
{% raw %}
import pytest
from cogent3 import get_app
from {{ project_slug }} import {{ app_class_name }}

def test_{{ app_slug }}_installed():
    app = get_app("{{ app_class_name }}")
    got = app("test")
    expected = None  # replace with expected result
    assert got == expected, f"got {got}, expected {expected}"
{% endraw %}
"""

# Get the cookiecutter context
library_name = "{{ cookiecutter.library_name }}"
apps = "{{ cookiecutter.apps }}"
author = "{{ cookiecutter.author }}"
project_slug = "{{ cookiecutter.project_slug }}"

# Split and process the apps
apps_list = [app.strip() for app in apps.split(',')]

for app in apps_list:
    app_slug = app.lower().replace(' ', '_')
    app_class_name = app.title().replace(' ', '')

    # Render the app file
    app_template = Template(app_template_content)
    app_file_content = app_template.render(app_class_name=app_class_name)
    app_file_path = os.path.join("src", project_slug, f"{app_slug}.py")

    with open(app_file_path, "w") as app_file:
        app_file.write(app_file_content)

    # Render the test file
    test_template = Template(test_template_content)
    test_file_content = test_template.render(project_slug=project_slug, app_class_name=app_class_name, app_slug=app_slug)
    test_file_path = os.path.join("tests", f"test_{app_slug}_installed.py")

    with open(test_file_path, "w") as test_file:
        test_file.write(test_file_content)
