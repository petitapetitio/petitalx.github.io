import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://petitapetit.io"
RELATIVE_URLS = False

# I want short-urls on my server
PAGE_SAVE_AS = PAGE_URL = ARTICLE_SAVE_AS = ARTICLE_URL = "{slug}"

# DISQUS_SITENAME = ""