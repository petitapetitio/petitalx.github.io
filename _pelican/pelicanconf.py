from pelican.readers import MarkdownReader
from pelican.settings import DEFAULT_CONFIG
from pygments.formatters.html import HtmlFormatter

AUTHOR = 'Alexandre Petit'
SITENAME = 'Alexandre Petit'
SITEURL = ""

PATH = "content"
THEME = "themes/petitalxio"

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

HOME, _ = MarkdownReader(DEFAULT_CONFIG.copy()).read("content/pages/home.md")


class HtmlFormatterWithCopyButton(HtmlFormatter):
    def __init__(self, **options):
        super().__init__(**options)

    def _wrap_div(self, inner):
        yield 0, ('<div' + (self.cssclass and f' class="{self.cssclass}"') + '>\n')
        yield 0, '<button class="copy-button" onclick="copyToClipboard(this)">Copy code</button>'
        yield from inner
        yield 0, '</div>\n'


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

PAGE_SAVE_AS = "{slug}.html"

# Disable the generation of these pages
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
