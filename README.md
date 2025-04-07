# transcribe-and-test

Poetry:

Dependency management and packaging:
poetry is a tool for dependency management and packaging in Python.
It uses pyproject.toml for configuration.

Install: pip install poetry
Create: poetry new myproject
Initialize in existing project: poetry init
Activate: poetry env activate
Install packages: poetry add package_name

Generate EXE
************
poetry run pyinstaller --onefile --windowed main.py

