import logging
import os
import sys

from pelican.readers import MarkdownReader
from pelican.settings import DEFAULT_CONFIG

sys.path.append(os.curdir)
from pygments_formatter import HtmlFormatterWithCopyButton  # nopep8 (current dir needs to be added to path before)
from plugins import readtime  # nopep8 (current dir needs to be added to path before)

PLUGINS = [readtime]

AUTHOR = 'Alexandre Petit'
SITENAME = 'Alexandre Petit'
SITEURL = ""

PATH = "content"
THEME = "themes/petitalxio"

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

HOME, _ = MarkdownReader(DEFAULT_CONFIG.copy()).read("content/pages/home.md")

LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]

STATIC_PATHS = ['images']

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "pygments_formatter": HtmlFormatterWithCopyButton,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

FEED_ALL_RSS = "feeds/all.rss.xml"
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Short-url doesn't work on the dev server
PAGE_SAVE_AS = PAGE_URL = ARTICLE_SAVE_AS = ARTICLE_URL = "{slug}.html"

# Disable the generation of these pages
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
