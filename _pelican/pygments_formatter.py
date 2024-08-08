from pygments.formatters.html import HtmlFormatter


class HtmlFormatterWithCopyButton(HtmlFormatter):
    def __init__(self, **options):
        super().__init__(**options)

    def _wrap_div(self, inner):
        yield 0, ('<div' + (self.cssclass and f' class="{self.cssclass}"') + '>\n')
        yield 0, '<button class="copy-button" onclick="copyToClipboard(this)">Copy code</button>'
        yield from inner
        yield 0, '</div>\n'
