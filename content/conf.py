# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = "Vampyr coven"
copyright = "2024, The contributors"
author = "The contributors"
github_user = "MRChemSoft"
github_repo_name = "vampyr-coven"  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/content/"  # with leading and trailing slash
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    "sphinx_lesson",
    "sphinx.ext.duration",
    "sphinxcontrib.bibtex",
    "sphinx_thebe",
    "myst_nb",
]
# configure myst_nb
source_suffix = {".rst": "restructuredtext", ".ipynb": "myst-nb", ".myst": "myst-nb"}
# configure sphinxcontrib.bibtex
bibtex_bibfiles = ["bibliography.bib"]

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/computation/execute.html
# *only* execute if at least one output is missing.
nb_execution_mode = "off"
nb_execution_show_tb = True

# settings for myst_parser
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]
myst_url_schemes = ("http", "https", "mailto")

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "img/vampyr-logo.png"
html_title = ""  # project
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
    "https://3Dmol.org/build/3Dmol-min.js"
]
# sphinx-book-theme options
html_theme_options = {
    "repository_url": f"https://github.com/{github_user}/{github_repo_name}",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": f"{github_version}",
    "path_to_docs": "content",
    "use_download_button": True,
    "home_page_in_toc": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "thebe": True,
        "notebook_interface": "jupyterlab",
    },
}
