# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


sys.path.insert(0, os.path.abspath(".."))

os.environ.setdefault("SENTRY_DSN", "")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

import django  # noqa: E402
django.setup()

# Auto-generate ERD on RTD using pydot
if os.getenv("READTHEDOCS") == "True":
    from django.core.management import call_command
    out_dir = os.path.join(os.path.dirname(__file__), "_static")
    os.makedirs(out_dir, exist_ok=True)

    # Generate the DOT file
    dot_file = os.path.join(out_dir, "erd.dot")
    call_command("graph_models", "lettings", "profiles", "-o", dot_file)

    # Convert it to SVG
    svg_file = os.path.join(out_dir, "erd.svg")
    subprocess.run(["dot", "-Tsvg", dot_file, "-o", svg_file], check=True)

project = 'Python-OC-Lettings-FR'
copyright = '2025, OC Lettings'
author = 'OC Lettings'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",  # resolve external refs (Python/Django)
]

autosummary_generate = True

# Link to external inventories
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/stable/", None),
}

# Render type hints in the description to reduce cross-ref noise
autodoc_typehints = "description"

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

napoleon_google_docstring = True
napoleon_numpy_docstring = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = "en"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
