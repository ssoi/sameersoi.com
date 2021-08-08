#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup

import os

AUTHOR = "Sameer Soi"
SITENAME = "Sameer Soi"
SITEURL = ""

THEME = os.environ["THEMEDIR"]

PATH = "content"

TIMEZONE = "America/Los_Angeles"

AVATAR = "https://secure.gravatar.com/avatar/28510cc609a757ebf02fe6db2058cfb7?size=500"

PELICANCONF_PATH = os.path.dirname(os.path.realpath(__file__))
PLUGIN_PATHS = [os.path.join(PELICANCONF_PATH, "plugins")]
PLUGINS = [nb_markup]
IPYNB_SKIP_CSS=True

DEFAULT_LANG = "en"
DEFAULT_DATE = "fs"
DISPLAY_CATEGORIES_ON_MENU = False
MARKUP = ("md", "ipynb")

IGNORE_FILES = [".ipynb_checkpoints"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Add blog template
TEMPLATE_PAGES = {"blog.html": "blog.html"}

# Sidebar menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ("About", "/pages/about.html"),
    ("Blog", '/blog.html'),
    ("Email", "https://mailhide.io/e/VZyUPbTJ"),
    ("Résumé", "/pdfs/sameer_soi_resume.pdf")
)

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("github", "https://github.com/ssoi"),
    ("twitter", "https://twitter.com/sameersoi"),
    ("linkedin", "https://www.linkedin.com/in/sameersoi/")
)
TWITTER_USERNAME = "sameersoi"

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
