# Sphinx configuration file for the day6 documentation.
project = 'day6 Documentation'
author = 'Lila Fredrika'

# Add any Sphinx extension module names here, as strings.
extensions = [
    'myst_parser',
]

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The theme to use for HTML output
html_theme = 'sphinx_rtd_theme'

# The master toctree document.
master_doc = 'index'

# Support both reStructuredText and Markdown source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Options for myst-parser (if needed)
# myst_enable_extensions = [
#     "deflist",
#     "html_admonition",
#     "html_image",
# ]
