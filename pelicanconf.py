#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = "Sameer Soi"
SITENAME = "Sameer Soi"
SITEURL = ""

THEME = os.environ["THEMEDIR"]

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"
DEFAULT_DATE = "fs"

MARKUP = ("md", "ipynb")
PELICANCONF_PATH = os.path.dirname(os.path.realpath(__file__))
PLUGIN_PATHS = [os.path.join(PELICANCONF_PATH, "plugins")]
PLUGINS = ["ipynb.markup"]

IGNORE_FILES = [".ipynb_checkpoints"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("github", "ssoi"),
    ("stackexchange", "328657/sameer"),
    ("twitter", "sameersoi"),
    ("linkedin", "sameer-soi-91a895b1"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
