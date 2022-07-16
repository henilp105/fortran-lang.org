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
import yaml
from pathlib import Path
from collections import Counter
import json
import requests
import sys
import datetime


info = requests.get('https://raw.githubusercontent.com/henilp105/fortran-lang.org/master/fortran_learn.json').text
conf = json.loads(info)
info = requests.get('https://raw.githubusercontent.com/henilp105/fortran-lang.org/master/fortran_package.json').text
fortran_tags = json.loads(info)
info = requests.get('https://raw.githubusercontent.com/henilp105/fortran-lang.org/master/contributor.json').text
contributors = json.loads(info)

# -- Project information -----------------------------------------------------

project = 'Fortran-lang.org website'
copyright = '2022, Fortran Community'
author = 'Fortran Community'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx_jinja",
    'matplotlib.sphinxext.plot_directive',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'numpydoc',
    'sphinx_charts.charts',
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    "html_image",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
locale_dirs = ["../locale/"]
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.

language = str(sys.argv[2][-2:])
html_search_language = str(sys.argv[2][-2:])

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['learn/intrinsics/**']
html_additional_pages = {}
suppress_warnings = ["myst.header"]

jinja_contexts = {
    'conf':conf,
    'fortran_index':fortran_tags,
    'contributors':contributors,
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    "favicons" : [
        {
            "rel": "icon",
            "sizes": "256x256",
            "href": "images/favicon.ico",
        },
    ],
    "show_prev_next": True,
    "show_nav_level": 4,
    "footer_items": ["copyright"],
    "navbar_align": "right",
    "navbar_start": ["navbar-logo"],
    "page_sidebar_items": ['index_news.html'],
    "navbar_end": ["theme-switcher.html","navbar-icon-links"],
    "icon_links": [
        {
            "name": "Discourse",
            "url": "https://fortran-lang.discourse.group/",
            "icon": "fab fa-discourse",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/fortranlang",
            "icon": "fab fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/fortran-lang",
            "icon": "fab fa-github",
        },
        {
            "name": "RSS",
            "url": "https://fortran-lang.org/news.xml",
            "icon": "fas fa-rss",
        },
    ]
}

html_sidebars = {
    "news": [
        "tagcloud.html",
        "archives.html",
        "recentposts.html",
    ],
    "news/**": [
        "postcard.html",
        "recentposts.html",
        "archives.html",
    ],
    "learn/**": ["sidebar-nav-bs.html"],
    "learn":[],
    "index":['index_joinus.html'],
    "compilers": [],
    "packages": [],
    "community": [],
    "packages/**": [],
}
html_title = "Fortran Programming Language"
html_logo = "_static/images/fortran-logo-256x256.png"

master_doc = 'index'

fontawesome_link_cdn = True 

blog_path = "news"
blog_post_pattern = "news/*"
blog_baseurl = "https://fortran-lang.org/" 
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2