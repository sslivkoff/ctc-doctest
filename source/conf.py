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

# since cannot use TYPE_CHECKING=True, load type system
# import typing
# typing.TYPE_CHECKING = True
# import ctc.spec.typedefs
# for key, value in vars(ctc.spec.typedefs).items():
#     setattr(ctc.spec, key, value)


# -- Project information -----------------------------------------------------

project = 'Check the Chain (ctc)'
copyright = '2022'
author = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    # 'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'myst_parser',
    # 'sphinx_rtd_dark_mode',  # for dark mode theme
    'sphinx_copybutton',
    # 'nbsphinx'
]

# autodoc_typehints = "none"
# always_document_param_types = True
always_document_param_types = False
typehints_fully_qualified = False

# from ctc.spec.formatting import typehints_formatter
set_type_checking_flag = True

# autodoc_type_aliases = True
# autodoc_typehints = 'description'
# autodoc_unqualified_typehints = True
# autodoc_typehints_format = 'short'
# autodoc_type_aliases = {
#     'spec.ProviderSpec': 'ProviderSpec',
#     'ProviderSpec': 'spec.ProviderSpec',
# }


myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


html_static_path = ['_static']


def setup(app):
    app.add_css_file('style.css')


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # 'collapse_navigation': True,
    'titles_only': True,
    # 'prev_next_buttons_location': 'top',
    'sticky_navigation': False,
    # 'body_max_width': '95%',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_copyright = False
html_show_sphinx = False

# user starts in dark mode
default_dark_mode = False

