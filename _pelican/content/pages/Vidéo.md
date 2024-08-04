---
Title: Script de la vidéo
---
Inspiration
- https://sive.rs/
- https://perfectmotherfuckingwebsite.com/


#### Snippets

pelicanconf.py
```
HOME, _ = MarkdownReader(DEFAULT_CONFIG.copy()).read("content/pages/home.md")

FEED_ALL_RSS = "feeds/all.rss.xml"  
FEED_ALL_ATOM = "feeds/all.atom.xml"  
CATEGORY_FEED_ATOM = None  
TRANSLATION_FEED_ATOM = None  
AUTHOR_FEED_ATOM = None  
AUTHOR_FEED_RSS = None

TAG_SAVE_AS = ''  
TAGS_SAVE_AS = ''  
CATEGORY_SAVE_AS = ''  
CATEGORIES_SAVE_AS = ''  
AUTHOR_SAVE_AS = ''  
AUTHORS_SAVE_AS = ''  
ARCHIVES_SAVE_AS = ''
```

Makefile
```
clean:
	rm $(OUTPUTDIR)/**.html || true
	rm -rf "$(OUTPUTDIR)/feeds"
	rm -rf "$(OUTPUTDIR)/pages"
	rm -rf "$(OUTPUTDIR)/theme"
	rm -rf "$(OUTPUTDIR)/images"
	
github: clean publish
	git add -A
	git commit -m "Update site"
	git push origin $(GITHUB_PAGES_BRANCH)
```


```
FEED_ALL_RSS = "feeds/all.rss.xml"  
FEED_ALL_ATOM = "feeds/all.atom.xml"  
CATEGORY_FEED_ATOM = None  
TRANSLATION_FEED_ATOM = None  
AUTHOR_FEED_ATOM = None  
AUTHOR_FEED_RSS = None
```


```
# Disable the generation of these pages  
TAG_SAVE_AS = ''  
TAGS_SAVE_AS = ''  
CATEGORY_SAVE_AS = ''  
CATEGORIES_SAVE_AS = ''  
AUTHOR_SAVE_AS = ''  
AUTHORS_SAVE_AS = ''  
ARCHIVES_SAVE_AS = ''
```
