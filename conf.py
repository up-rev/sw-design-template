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

project = 'FCD SW design'
author = 'Jason Berger'


docx_pagebreak_before_section = 2
docx_style = '_templates/style.docx'

docx_style_names = {
   'strike': 'Strike',
   'default-table': 'Grid Table 5 Dark - Accent 2',
}

html_favicon = 'assets/images/favicon.ico'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.plantuml','docxbuilder']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

latex_elements = {
  'extraclassoptions': 'openany,oneside',
  'preamble' : '\\renewcommand\FmN[1]{}'
  
}



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

html_logo = "assets/images/logo.png"

html_theme_options = {
    "collapse_navigation" : False
}

source_suffix = {
    '.rst': 'restructuredtext'
}

html_sidebars = {
        '**': [
                 'localtoc.html',
                 'relations.html',
                 'searchbox.html',
                 # located at _templates/
                 'foo.html',
            ]

        }

# Define setup function in conf.py
def setup(app):
    # Define visit method for plantuml node generated by sphinxcontrib.plantuml
    # https://pypi.org/project/sphinxcontrib-plantuml/
    def docx_visit_plantuml(self, node):
        def get_filepath(self, node):
            from sphinxcontrib import plantuml
            _, filepath = plantuml.render_plantuml(self, node, 'png')
            return filepath
        alt = node.get('alt', (node['uml'], None))
        # Docxbuilder provides useful methods. See Docxbuilder API reference.
        self.visit_image_node(node, alt, get_filepath)
    # Add the visit method to Docxbuilder
    import docxbuilder
    translator = docxbuilder.DocxBuilder.default_translator_class
    setattr(translator, 'visit_plantuml', docx_visit_plantuml)