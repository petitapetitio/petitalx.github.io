Title: Créer son site personnel gratuitement avec Githbub Pages et Python, et Pelican
Date: 2024-07-27

## Contexte

Cela fait plusieurs mois que j'expérimente différents supports d'écriture :

- je me suis lancé sur [LinkedIn](https://www.linkedin.com/in/petitalx/)
- j'ai créé une [newsletter sur Substack](https://100produits.substack.com/)
- j'écrire deux pages par jour dans un carnet physique depuis 20 jours

Une difficulté que je rencontre est que je n'ai pas de ligne éditoriale claire, pas de promesse. 

J'ai envie d'écrire sur des sujets variés : 

- de retours d'expérience de projets techniques
- des "récits" de voyage
- des points d'avancement de projet
- ...

Et je n'ai pas envie de m'imposer de façon "push". 

Pour ces deux raisons, donc un site personnel me semble être une bonne solution.

En complément de The Developer's Brain, je veux réaliser 30 projets en Python. 

Créer un site personnel en python apparaît comme bon challenge !

## Cadrer le projet

Ma motivation est de "Claim a personal domain"

Ce qui est important pour moi est de :

- livrer
- choisir une solution simple
- avoir un processus de décision clair dans le choix des technologies
- faire un projet en python pour pousser mon expertise sur ce langage

Les risques que je perçois sont : 

- de tomber dans un rabbit hole lors du choix de la technologie
- de me torturer le cerveau pour choisir une solution d'hébergement
- de choisir un outil trop complexe pour mon besoin

OK.

À présent, je suis mis en garde !

## Choisir la technologie

Pour créer un site avec Python, j'ai d'abord pensé aux technologies suivantes : 

- Django : un framework fullstack populaire pour créer des applications web
- Flask : un framework léger pour créer des applications web

Je me suis posé la question 

> Quelle framework choisir pour créer un site personnel ?

Je suis tombé sur ce fil Reddit [Best framework for portfolio website?](https://www.reddit.com/r/Python/comments/166xf22/best_framework_for_portfolio_website/).

Les réponses sont unanimes. Utiliser Django ou Flask revient à se compliquer la vie. Un générateur de site statique est plus simple, moins cher et plus rapide

En effet, les générateurs de site statique ont les avantages suivants : 
- Simplicité : ils sont en général plus simple à utiliser que les frameworks fullstack complets
- Prix : il existe de nombreuses solutions d'hébergement gratuit
- SEO : les pages sont statiques et donc facilement indexables par les moteurs de recherche

Je me suis donc tourné vers les générateurs de site statique.

## Choisir un générateur de site statique

Les solutions les plus tendances sont : 
- Jekyll
- Hugo
- Astro

**Jekyll** existe depuis 2008. L'outil est écrit en Ruby. Plus de [180k](https://trends.builtwith.com/fr/cms/Jekyll) sites web sont construit avec, et c'est la technologie qui est proposée par défaut pour Github Pages. Il bénéficie communauté, d'un écosystème de plugins. La [galerie](https://jekyllrb.com/showcase/) démontre qu'il est possible de faire des sites esthétiques et complets avec. 

**Hugo** existe depuis 2013. Il est écrit en Go et se veut le générateur statique le plus rapide (en termes de compilation). Il est utilisé par [presque 300k sites](https://trends.builtwith.com/fr/cms/Hugo). Il dispose de fonctionnalités de localisation, et peut être associé à des frameworks CSS comme Tailwind. 

**Astro** est un générateur de site statique qui permet de combiner Svelte, React et Vue. Je l'ai tout de suite écarté car un wrapper autour de frameworks indique une complexité élevée. 

Et python ?

Il existe bien un générateur de sites statiques en python : Pelican.

**Pelican** existe depuis 2010. Il est écrit en python et a été créé par [Alexis Metaireau](http://blog.notmyidea.org/). Il est utilisé par seulement [3500 sites](https://trends.builtwith.com/websitelist/Pelican), mais il dispose d'une documentation claire. Et comme il est écrit en python, je pourrai contribuer au code source ! 

Je choisis donc Pelican.

## Choisir une solution de déploiement

Il existe plusieurs solutions pour déployer un site statique :

- AWS
- Netlify
- Github Pages
- Mon propre serveur

Je veux une solution gratuite et simple.

J'ai entendu beaucoup de bien de Github Pages. 

Je vais tester cette solution.

## Créer le site

Ok, on entre dans le vif du sujet.

Dans la suite de l'article, on va suivre ensemble les étapes que j'ai suivi pour construire mon site personnel `petitalx.io`. `petitalx` est mon username github. Naturellement, vous pouvez remplacer toutes les occurences de `petitalx` par votre username.

### Créer un walking skeleton

Notre premier objectif est de configurer et déployer un site le plus rapidement possible. On pourra ensuite itérer pour ajuster le style et simplifier le code.

Prérequis :

- avoir un terminal 
- avoir python installé
- avoir un compte github
- connaître le ba-ba de git

On commence par créer le projet en local.
```shell
cd ~/dev
mkdir petitalxio
cd petitalxio

python --version 
python -m venv .venv
source .venv/bin/activate
```

Créer le fichier requirements.txt suivant
```text
pelican[markdown]
```

Puis installer les dépendances
```shell
pip install -r requirements.txt
```

Lancer l'assistant de création de site
```shell
pelican-quickstart
```

- créer le site dans un dossier `_pelican` 
- choisir `fr` comme langue par défaut
- ne pas préciser de préfixe d'url
- désactiver la pagination
- choisir 'Europe/Paris' comme timezone
- demander à générer le fichier Makefile
- répondre oui à la question "Do you want to upload your website using GitHub Pages?"

OK ! 

Pour visionner le site en local, lancer la commande
```shell
cd ~/dev/petitalxio/_pelican
pelican content
pelican --listen
```

#### Publier sur Github Pages

Rendez-vous sur votre compte github : https://github.com/. 

Créer un nouveau repository `username.github.io` où `username` est votre nom d'utilisateur github.


De retour sur votre poste, se replacer à la racine du projet
```shell
cd ~/dev/petitalxio`
```

Créer un fichier .gitignore avec le contenu suivant
```text
.venv  
**__pycache__**/
```

Initialiser le dépôt git
```shell
echo "# petitalx.github.io" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/petitalx/petitalx.github.io.git
git push -u origin main
```

La façon la plus simple de déployer le site est de générer le contenu du site à la racine du répertoire.

On va donc modifier le fichier `Makefile` pour que la commande `make publish` génère le site à la racine du répertoire.

Modifier le fichier `_pelican/Makefile` pour que la variable `OUTPUTDIR` soit égale à `$(BASEDIR)/..`.

Lancer `make publish` depuis `~/dev/petitalxio/_pelican`.

Lancer `git add .`, `git commit -m "generate content"`, `git push`.

Vérifier que le déploiement est en cours dans le volet https://github.com/petitalx/petitalx.github.io/actions.


# Brouillon

- Choisir la technologie
- Choisir le solution de déploiement
- Créer le site
- Conclusion
  - Ressources
  - Mes notes de second cerveau
  - J'ai pris une décision confiant !!
  - Pistes pour aller plus loin : créer mon propre générateur, crééer un thème, contribuer à la doc de Pelican, prendre une issue


