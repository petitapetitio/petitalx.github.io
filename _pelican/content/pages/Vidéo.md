---
Title: Script de la vidéo
---
Inspiration

- https://sive.rs/
- https://perfectmotherfuckingwebsite.com/

Script

0. Intro 
	-  Inspiration
		- https://sive.rs/
		- https://perfectmotherfuckingwebsite.com/
	- Code minimalisme
1. Initialiser le projet 
	- Setup
	- Architecture du projet
	- Les 3 paramètres importants (content, output, settings) | listen
	- Un premier aperçu du site
	- Le Makefile
	- tasks.py
2. Publier sur Github
3. Ajouter du contenu
	1. Articles
	2. Pages
4. Mettre en forme
	1. Template explicite
	2. CSS
	3. Home
5. Conclusion
	1. Article
	2. Questions
	3. Partagez votre site dans les commentaires !


#### Snippets

.gitignore
```
.venv  
.idea  
.obsidian  
**__pycache__**/
```


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

