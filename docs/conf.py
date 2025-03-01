# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

import os
import sys
import time
import pingouin

sys.path.insert(0, os.path.abspath("sphinxext"))


# -- Project information -----------------------------------------------------

project = "pingouin"
author = "Raphael Vallat"
copyright = "2018-{}, Raphael Vallat".format(time.strftime("%Y"))

# sys.path.insert(0, os.path.abspath(os.path.pardir))
version = pingouin.__version__
release = pingouin.__version__

# Sphinx-issues configuration
issues_github_path = "raphaelvallat/pingouin"


# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "matplotlib.sphinxext.plot_directive",
    "numpydoc",
    "sphinx_copybutton",
    "sphinx_design",
    "notfound.extension",
]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# Path to templates
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# List of patterns, that match files and directories
# to ignore when looking for source files.
exclude_patterns = ["_build", "docstrings", "nextgen", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# Generate the API documentation when building
autosummary_generate = True
numpydoc_show_class_members = True  # FALSE ?

# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False


# -- Options for HTML output ----------------------------------------------

html_theme = "pydata_sphinx_theme"
html_favicon = "pictures/pingouin_blue.svg"

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

html_show_sourcelink = True
html_copy_source = False

html_theme_options = {
    "logo": {
        "text": project,
        "image_light": "pictures/pingouin.svg",
        "image_dark": "pictures/pingouin.svg",
        "alt_text": "pingouin homepage",
    },
    "navbar_persistent": ["search-button"],
    "navbar_end": ["navbar-icon-links", "theme-switcher"],
    "navbar_align": "left",
    "header_links_before_dropdown": 3,
    "back_to_top_button": True,
    "show_prev_next": False,
    "navigation_depth": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/raphaelvallat/pingouin",
            "icon": "fa-brands fa-github",
        },
    ],
    "use_edit_page_button": True,
    "pygments_light_style": "vs",
    "pygments_dark_style": "monokai",
}

html_sidebars = {
    "citing": [],
    "contributing": [],
    "changelog": [],
    "faq": [],
    "guidelines": [],
    "index": [],
}

html_context = {
    "github_user": "raphaelvallat",
    "github_repo": "pingouin",
    "github_version": "main",
    "doc_path": "docs",
}


# -- Intersphinx ------------------------------------------------

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "statsmodels": ("https://www.statsmodels.org/stable/", None),
    "seaborn": ("https://seaborn.pydata.org/", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
}
