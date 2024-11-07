#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Basic settings
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Miscellaneous'
DELETE_OUTPUT_DIRECTORY = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.nl2br': {},
        'markdown.extensions.toc': {'permalink': True, 'permalink_title': 'パーマリンク', 'toc_depth': 3},
    },
    'output_format': 'html5',
}
PATH = 'assets/content'
PLUGINS = ['assets', 'extract_toc', 'minify', 'neighbors', 'related_posts', 'tipue_search']
PLUGIN_PATHS = ['assets/plugins']
SITENAME = 'うずらの備忘録'
TYPOGRIFY = True
BIND = '0.0.0.0'

# URL settings
ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''

# Time and Date
TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE_FORMAT = '%Y年%-m月%-d日'

# Template pages
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives', 'search', '404']

# Metadata
AUTHOR = 'うずら'
FILENAME_METADATA = r'(?P<slug>(?P<date>\d{14}))'

# Feed settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Translations
DEFAULT_LANG = 'ja'
TRANSLATION_FEED_ATOM = None

# Themes
THEME = 'assets/elegant'

# Others
MINIFY = {'remove_comments': True, 'remove_empty_space': True, 'reduce_boolean_attributes': True}
SITE_DESCRIPTION = 'Webエンジニアのうずらが、日々の開発で生じた問題とその解決方法をメモするブログです。'
LANDING_PAGE_TITLE = "うずらの備忘録 - Quail's Notes That Are Related to Web Development"
PROJECTS_TITLE = 'マイプロジェクト'
PROJECTS = [
    {
        'name': 'ChipTube',
        'url': 'https://chiptu.be',
        'description': 'Web MIDI Player',
    },
]
RELATED_POSTS_LABEL = '関連記事'
HOSTED_ON = {'name': 'Amazon S3', 'url': 'https://aws.amazon.com/s3/'}
ARCHIVES_URL = 'archives'
CATEGORIES_URL = 'categories'
SEARCH_URL = 'search'
TAGS_URL = 'tags'
