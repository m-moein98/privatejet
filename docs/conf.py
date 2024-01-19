"""
Sphinx configuration file.
"""


import os
import sys


sys.path.insert(0, os.path.abspath(".."))

project = "PrivateJet"
copyright = "2024, Mohammed Moein"
author = "Mohammed Moein"
release = "0.0.3"

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme", "sphinx.ext.intersphinx"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
