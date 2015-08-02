#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Derek Saw'
SITENAME = u"Rambo Coder"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog', 'download', 'images', 'extra/robots.txt', 'extra/favicon.ico']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

EXTRA_PATH_METADATA = {
    'extra/robots.txt':     {'path': 'robots.txt'},
    'extra/favicon.ico':    {'path': 'favicon.ico'},
}

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='./pelican-bootstrap3'

TAG_CLOUD_MAX_ITEMS=20
