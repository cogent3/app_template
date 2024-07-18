# A Cookiecutter template for creating cogent3 plug-in apps

Cookiecutter is a command-line utility that creates projects from cookiecutters (project templates). This is a cookiecutter template for creating a library that exports and registers cogent3 plugin apps.

## Requirements

- python 
- `cookiecutter` installed from the command line using: 
```bash
pip install cookiecutter
```
- `jinja2 ` installed from the command line using: 
```bash
pip install jinja2
```

## Running the cookiecutter to create cogent3 plug-in apps

- create a new directory for your library
- run cookie cutter with the url of this repository
```bash
cookiecutter https://github.com/yourusername/cookiecutter-cogent3-plugin

```

You will be asked to fill out 5 fields:
- library_name: This is the name of your library that will export the apps
- apps : This is a comma separated list of the apps you want to create in the library
- author: Your name
- email: Your email
- project_slug: The name of the project.  This will be the name of the root directory and likely your repository

In your current directory will be created a directory named with your project_slug, inside of which will be a project with documentation for how to 
test the apps and how to add new apps to the library.