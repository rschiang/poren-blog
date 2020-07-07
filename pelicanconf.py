#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = 'Poren Chiang'
SITENAME = '任任的藍色虛空'
SITESUBTITLE = '漫思於粼粼極光'
# SITEURL

TIMEZONE = 'Asia/Taipei'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

DEFAULT_LANG = 'zh-Hant'
LOCALE = 'zh_TW'

DISPLAY_CATEGORIES_ON_MENU = False

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<slug>.*)'

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/{lang}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/{lang}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = False
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = False

PATH = 'content'
OUTPUT_PATH = 'output'

STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/favicon.png': {'path': 'favicon.png'},
    'extras/robots.txt': {'path': 'robots.txt'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
MENUITEMS = (
    ('部落格', 'https://blog.poren.tw'),
    ('筆記本', 'https://blog.poren.tw/category/'),
    ('晷跡', 'https://blog.poren.tw/archives/'),
    ('漫遊檔案', 'https://poren.tw'),
)

SOCIAL = (
    ('GitHub', 'https://github.com/rschiang'),
)

LICENSE = ['BY', 'SA']

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown_del_ins': {},
    },
    'output_format': 'html5',
}

# Plugins
THEME = 'theme/dawn'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['gravatar', 'summary']

# Plugin configuration
SUMMARY_BEGIN_MARKER = '<!-- summary -->'
SUMMARY_END_MARKER = '<!-- more -->'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
