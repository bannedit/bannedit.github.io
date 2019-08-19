#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'bannedit'
SITENAME = "bannedit's musings"
SITEURL = 'https://bannedit.github.io'
SITETITLE = "bannedit"
SITESUBTITLE ="Vulnerability Researcher"
SITELOGO = 'resources/profile.png'

GITHUB_URL = 'https://github.com/bannedit'
FAVICON = 'resources/favicon.ico'

STATIC_PATHS = ['resources', 'theme', 'theme/img']
PYGMENTS_STYLE = 'native'
PATH = 'content'

TWITTER_CARD = True
TWITTER_IMG = 'resources/profile.png'
TWITTER_USERNAME = "bannedit0"

TIMEZONE = 'America/New_York'
THEME = "theme/Flex"

DEFAULT_LANG = 'en'

DEFAULT_METADATA = {
    'status': 'draft',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

USE_FOLDER_AS_CATEGORY = True

MAIN_MENU = False
MENUITEMS = (
                ('Archives', '/archives.html'),
                ('Categories', '/categories.html'),
                ('Tags', '/tags.html'),
)

# Blogroll
LINKS = (
            ('Blog', '/'),
            ('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
            ('Tags', '/tags.html'),
            ('RSS', '/feeds/all.rss.xml'),
)

# Social widget
SOCIAL = (    
              ('github', 'https://github.com/bannedit'),
              ('twitter', 'https://twitter.com/bannedit0'),
              ('linkedin', 'https://linkedin.com/in/david-rude'),
              ('rss', 'feeds/all.rss.xml'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
