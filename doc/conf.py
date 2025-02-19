# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u'GeoViews'
authors = u'HoloViz Developers'
copyright = u'2018-2021 ' + authors
description = 'Geographic visualizations for HoloViews.'

import geoviews
version = release = str(geoviews.__version__)

html_static_path += ['_static']

html_css_files = [
    'nbsite.css',
    'custom.css'
]

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/logo_horizontal.png"
html_favicon = "_static/favicon.ico"

html_theme_options = {
    "github_url": "https://github.com/holoviz/geoviews",
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/HoloViews",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.holoviz.org/",
            "icon": "fab fa-discourse",
        }
    ]
}

extensions += [
    'sphinx.ext.napoleon',
    'nbsite.gallery',
    'sphinx_copybutton',
]
napoleon_numpy_docstring = True

templates_path = ['_templates']

nbsite_gallery_conf = {
    'github_org': 'holoviz',
    'github_project': 'geoviews',
    'backends': ['bokeh', 'matplotlib'],
    'galleries': {
        'gallery': {
            'title': 'Gallery'
        }
    },
    'thumbnail_url': 'https://assets.holoviews.org/geoviews/thumbnails',
}

html_context.update({
    "last_release": f"v{'.'.join(geoviews.__version__.split('.')[:3])}",
    "github_user": "holoviz",
    "github_repo": "geoviews",
    "google_analytics_id": "UA-154795830-3",
})
