# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BaSyx Wiki'
copyright = '2023, Eclipse BaSyx™'
author = 'Eclipse BaSyx™'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/aaronzi/basyx-wiki",
    "use_repository_button": True,
    "use_sidenodes": True,

    "icon_links": [
        {
            "name": "Eclipse BaSyx™",
            "url": "https://github.com/eclipse-basyx",
            "icon": "_static/basyx_icon.png",
            "type": "local",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/eclipse-basyx",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Eclipse BaSyx™",
            "url": "https://github.com/eclipse-basyx",
            "icon": "https://img.shields.io/readthedocs/basyx-wiki",
            "type": "url",
        },
    ],
}

html_logo = "./_static/basyx_logo.png"

html_title = "Eclipse BaSyx™"

html_favicon = "_static/basyx_icon.ico"

# -- Options for EPUB output
epub_show_urls = 'footnote'