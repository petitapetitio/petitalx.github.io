---
Title: Script de la vidéo
---
Inspiration
- https://sive.rs/
- https://perfectmotherfuckingwebsite.com/

```
HOME, _ = MarkdownReader(DEFAULT_CONFIG.copy()).read("content/pages/home.md")
```

```
FEED_ALL_RSS = "feeds/all.rss.xml"  
FEED_ALL_ATOM = "feeds/all.atom.xml"  
CATEGORY_FEED_ATOM = None  
TRANSLATION_FEED_ATOM = None  
AUTHOR_FEED_ATOM = None  
AUTHOR_FEED_RSS = None
```


Snippets
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
