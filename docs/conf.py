from datetime import date

import guzzle_sphinx_theme

from pyinfra import __version__


copyright = 'Nick Barrett {0} — pyinfra v{1}'.format(
    date.today().year,
    __version__,
)

extensions = [
    # Official
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

extensions.append('guzzle_sphinx_theme')

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

master_doc = 'index'
project = 'pyinfra'
author = 'Fizzadar'
version = 'develop'
pygments_style = 'sphinx'

# Theme style override
html_short_title = 'Home'
html_theme = 'guzzle_sphinx_theme'
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_static_path = ['static']

templates_path = ['templates']

html_favicon = 'static/logo_small.png'

html_sidebars = {
    '**': ['pyinfra_sidebar.html', 'searchbox.html'],
}
