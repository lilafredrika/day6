# {{ cookiecutter.project_name }} - Sphinx conf.py (cookiecutter template)
project = "{{ cookiecutter.project_name }}"
author = "{{ cookiecutter.author_name }}"

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
master_doc = 'index'
source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
