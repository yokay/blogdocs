# -*- coding: utf-8 -*-
#
# yokay documentation build configuration file, created by
# sphinx-quickstart on Tue Jul 21 00:27:45 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('.'))

extensions = ["sphinx.ext.intersphinx",
              "recommonmark",
              "sphinx_tabs.tabs",
              "sphinx_markdown_tables",
              "sphinx.ext.todo",
              "sphinx-material"]


todo_include_todos = True

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# extensions = ['sphinx.ext.intersphinx',
#   'breathe',
#   'exhale',
#              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Mythbird'
copyright = u'2019-2023, Yokay'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'zh_CN'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'default'
html_theme = 'sphinx_material'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'nav_title': 'Mythbird's Documents",

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://doc.mythbird.com',

    # Set the color and the accent color
    'color_primary': 'light-blue',
    # 'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    # 'repo_url': 'https://github.com/project/project/',
    # 'repo_name': 'Project',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Mythbird Blog"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'Deutzia.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = True

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
#htmlhelp_basename = 'yokaydoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

latex_engine = 'xelatex'
latex_use_xindy = False

latex_elements = {
    'preamble': '\\usepackage{CJKutf8}\n',
    'preamble': '\\usepackage{CJK}\n',
    'preamble': '\\usepackage{CTEX}\n',
}
# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     # 'papersize': 'letterpaper',
#     # The font size ('10pt', '11pt' or '12pt').
#     # 'pointsize': '10pt',
#     # Additional stuff for the LaTeX preamble.
#     # 'preamble': '\\hypersetup{unicode=true}\n',
#     'preamble': '\\usepackage{CJKutf8}\n',
#     'preamble': '\\DeclareUnicodeCharacter{00A0}{\nobreakspace}\n',
#     'preamble': '\\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{2713}{x}\n',
#     'preamble': '\\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}\n',
#     'preamble': '\\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}\n',
#     'preamble': '\\begin{CJK}{UTF8}\n',
#     'preamble': '\\AtEndDocument{\end{CJK}}\n',
#     'preamble': '\\usepackage[UTF8]{ctex}\n',
#     'preamble': '\\usepackage{xeCJK}\n',
# }
# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'yokay.tex', u'Mythbird Design Documentation',
     u'Yokay', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'Deutzia.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# for external links to standard library
# intersphinx_mapping = {
#        #~ 'python': ('http://docs.python.org', None),
#        'py': ('http://docs.python.org', None),
#        }
# Setup the breathe extension
# breathe_projects = {
#     "doc": "./doxyoutput/xml"
# }
# breathe_default_project = "doc"
# extensions = ['sphinx.ext.autodoc',
#               'sphinx.ext.doctest',
#               'sphinx.ext.intersphinx',
#               'sphinx.ext.todo',
#               'sphinx.ext.coverage',
#               'sphinx.ext.mathjax',
#               'sphinx.ext.ifconfig',
#               'sphinx.ext.viewcode',
#               'sphinx.ext.githubpages']
# # Setup the exhale extension
# exhale_args = {
#     # These arguments are required
#     "containmentFolder":     "./api",
#     "rootFileName":          "library_root.rst",
#     "rootFileTitle":         "Library API",
#     "doxygenStripFromPath":  ".",
#     # Suggested optional arguments
#     "createTreeView":        True,
#     # TIP: if using the sphinx-bootstrap-theme, you need
#     # "treeViewIsBootstrap": True,
#     "exhaleExecutesDoxygen": True,
#     "exhaleDoxygenStdin":    "INPUT = ../include"
# }

# # Tell sphinx what the primary language being documented is.
# primary_domain = 'c'

# # Tell sphinx what the pygments highlight language should be.
# highlight_language = 'c'
