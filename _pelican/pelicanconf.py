from pelican.readers import MarkdownReader
from pelican.settings import DEFAULT_CONFIG

AUTHOR = 'Alexandre Petit'
SITENAME = 'petitalxio'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

THEME = "themes/petitalxio"

config = DEFAULT_CONFIG.copy()
HOME, _ = MarkdownReader(config).read("content/pages/home.md")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Disable the generation of these pages
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
