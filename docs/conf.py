# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'neurogenpy'
copyright = '2022, Computational Intelligence Group (UPM)'
author = 'Computational Intelligence Group, Universidad Politécnica de Madrid'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'autoapi.extension',
    'numpydoc',
    "sphinx_rtd_theme",
    'sphinxcontrib.bibtex'
]

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'plain'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'display_version': False}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
# html_logo = "../imgs/cig.png"

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'neurogenpydoc'

html_context = {
    'display_github': False
}

# -- Extension configuration -------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ['../neurogenpy']
autoapi_options = ['members', 'undoc-members', 'show-inheritance',
                   'show-module-summary', 'imported-members',
                   'inherited-members', 'special-members']
numpydoc_validation_checks = {"PR01"}

# Grouping the document tree into LaTeX files. List of tuples# (source start
# file, target name, title, author, documentclass [howto/manual]).
# latex_documents = [
#     ('index', 'yourdoc.tex', u'NeurogenPy', u'Javier Gallego Gutiérrez',
#      'manual'),
# ]


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_util_classes)


def skip_util_classes(app, what, name, obj, skip, options):
    if what == "package" and "util" in name \
            or name == 'ProbabilisticClustering':
        skip = True
    return skip
