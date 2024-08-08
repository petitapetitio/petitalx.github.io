# petitalx.github.io

![](https://github.com/petitalx/petitalx.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)

## Description

Hello ! 

Ce dépôt contient le code source de mon site personnel. Il est généré avec [Pelican](https://docs.getpelican.com/en/stable/), un générateur de site statique écrit en Python. 

Le site est en ligne à l'adresse suivante : [petitalx.io](https://petitalx.io/)

## How to install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to run

Pour lancer le serveur de développement, il suffit de lancer la commande suivante :
```bash
cd _pelican
make devserver
```

> Attention, tout les commandes Make sont à lancer depuis le sous-dossier `_pelican`.


Pour déployer le site, il suffit de lancer la commande suivante :
```bash
make github
```
