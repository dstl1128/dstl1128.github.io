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
    ('github', 'https://github.com/dstl1128'),
    ('bitbucket', 'https://bitbucket.org/dereks'),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='./pelican-bootstrap3'

TAG_CLOUD_MAX_ITEMS=20

USE_PAGER=True
BOOTSTRAP_FLUID=False
DISPLAY_CATEGORY_IN_BREADCRUMBS=True
BOOTSTRAP_NAVBAR_INVERSE=True
DISPLAY_SERIES_ON_SIDEBAR=True
DISPLAY_ARTICLE_INFO_ON_INDEX=False
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_CATEGORIES_ON_SIDEBAR=True
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
RECENT_POST_COUNT=7

HIDE_SIDEBAR=False

USE_OPEN_GRAPH=True
#OPEN_GRAPH_FB_APP_ID=


