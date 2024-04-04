# app_template
A template for creating cogent3 apps

- create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate
```

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

- clone cogent3 into a subdirectory of your clone of this repo and switch to the plugin-support branch and install it using flit -s

```bash
    git clone git@github.com:cogent3/cogent3.git
    cd cogent3
    git checkout plugin-support
    pip install flit
    flit install -s .
    cd ..
```

- install the app_template package using -e to install it in editable mode

```bash
    pip install -e .
```

- load trial_plugins.ipynb in VS Code, and set it to use your venv as the python interpreter

- test the sample uppercase app in the notebook

- make changes to setup.py to add/remove entry points and install_requires as needed

- rinse/repeat


