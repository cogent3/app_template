# Library {{ cookiecutter.library_name.strip().lower().replace(' ', '_') }} exporting apps for cogent3

Exports the following cogent3 apps;
{% set apps_list = cookiecutter.apps.split(',') %}
{% for app_name in apps_list %} 
- {{ app_name.strip().title().replace(' ', '') }}
{% endfor %}


## Installation

### create a virtual environment and activate it

#### Linux or MacOS
```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
### install the app library

- install the library in the src folder using -e to install it in editable mode

```bash
    pip install -e .
```

### test the app

To install the test Nox suite use the following command

```bash
    pip install nox
```

To run the test suite use the following command to validate the app (for python 3.12)

```bash
    nox -s test-3.12 
```

### See the app working

- load trial_plugins.ipynb from the docs folder into VS Code, and set it to use your venv as the notebooks python interpreter
- test the sample uppercase app in the notebook
- note that the pyproject.toml file for this project includes the following

```python
[project.entry-points."cogent3.app"]{% set apps_list = cookiecutter.apps.split(',') %}
{% for app_name in apps_list %} {{ app_name.strip().title().replace(' ', '') }} = {{ cookiecutter.library_name.strip().lower().replace(' ', '_') }}.{{ app_name.strip().lower().replace(' ', '_') }}:{{ app_name.strip().title().replace(' ', '') }}
{% endfor %}
```
This will expose your apps to the plug-in architecture of cogent3.

## To add a new app

- add a new python file to the src\upper folder that imports define_app from cogent3
- add a class with a main method that takes the input data and returns the output data
- decorate the class with @define_app()
- add a docstring to the class that will be shown in the apps documentation

### example declaration of an app that converts input to lower case 
```python 
from cogent3.app.composable import define_app

@define_app()
class to_lower:
    def main(self, data: str) -> str:
        return data.lower()
```
- Add an entry-point to pyproject.toml that poionts to the library, file and class 
