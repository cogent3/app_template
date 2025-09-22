import os
from jinja2 import Template

# Load the template content
app_template_content = '''{% raw -%}
from cogent3.app.composable import define_app, NotCompleted

@define_app
class {{ app_class_name }}_class:
    """Documentation for {{ app_class_name }} class."""
    def __init__(self, param: float | None = None):
        """
            Parameters
            ----------
            param
                description of initialization parameter.
        """
        self.param = param

    # for a class based app, the main method is essential, as is
    # the type hint on its argument and its return type
    def main(self, data: str) -> str:
        # create NotCompleted if a condition for your app to complete
        # successfully is not met
        if not bool(data):
            return NotCompleted("FAIL", origin=self, message="Input data is empty", source=data)

        return data


# for a function based app, type hints on the first argument
# and the return type are essential
@define_app
def {{ app_class_name }}_func(data: str, param: float | None = None) -> str:
    """Documentation for {{ app_class_name }} function."""
    # create NotCompleted if a condition for your app to complete
    # successfully is not met
    if not bool(data):
        return NotCompleted("FAIL", origin="{{ app_class_name }}_func", message="Input data is empty", source=data)

    return data
{%- endraw %}
'''

test_template_content = """{% raw -%}
import pytest
from cogent3 import get_app
from {{ library_name }}.app import {{ app_class_name }}

@pytest.mark.xfail(reason="Expected to fail because it is using cookiecutter values")
def test_{{ app_slug }}_installed():
    app = get_app("{{ app_class_name }}")
    got = app("test")
    expected = None  # replace with expected result
    assert got == expected, f"got {got}, expected {expected}"
{%- endraw %}
"""

# Get the cookiecutter context
library_name = "{{ cookiecutter.library_name }}"
apps = "{{ cookiecutter.apps }}"
author = "{{ cookiecutter.author }}"
test_dir = "tests"
os.makedirs(test_dir, exist_ok=True)

# Split and process the apps
apps_list = [app.strip() for app in apps.split(",")]

for app in apps_list:
    app_slug = app.lower().replace(" ", "_")
    app_class_name = app.lower().replace(" ", "")

    # Render the app file
    app_template = Template(app_template_content)
    app_file_content = app_template.render(app_class_name=app_class_name)
    app_file_path = os.path.join("src", library_name, "app.py")

    with open(app_file_path, "w") as app_file:
        app_file.write(app_file_content)

    # Render the test file
    test_template = Template(test_template_content)
    test_file_content = test_template.render(
        library_name=library_name, app_class_name=app_class_name, app_slug=app_slug
    )
    test_file_path = os.path.join(test_dir, f"test_{app_slug}_installed.py")
    with open(test_file_path, "w") as test_file:
        test_file.write(test_file_content)
