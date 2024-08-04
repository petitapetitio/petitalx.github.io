---
date: 2023-10-17T14:36:25.392Z
title: Créer un générateur de recommandations LinkedIn
subtitle: Produit #2
---

Hello !

Aujourd'hui, je vous partage mon aventure dans le développement d'un
générateur de recommandation LinkedIn.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/c17a2939-aec2-4065-b1c1-395edf57c8f4_3024x1902.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc17a2939-aec2-4065-b1c1-395edf57c8f4_3024x1902.png)ça
ressemble à ça à la fin ! ☝️

Au programme de cette édition :

  * Introduction

    * Qu’est-ce qu’une recommandation LinkedIn ?

    * Pourquoi écrire une recommandation LinkedIn ?

    * La difficulté

    * Le concept

  * Exécution

    * Quelques recherches en amont

    * Construire le produit

    * Diffuser le produit

  * Bilan

    * Leçons

    * Monétisation

    * Conclusion

C'est parti !

# Introduction

> Quoi !? Pourquoi ?

Début 2023, je reçois le message d'un ancien collègue. Il est en plein
recrutement et me demande si je peux lui écrire une recommandation LinkedIn
pour le supporter dans ce processus.

Je réponds : oui, pas de soucis !

J'y pense.

Je prends quelques notes.

Je veux que la recommandation soit top.

J'hésite.

Je laisse maturer.

Bref, ça traine ...

## Mais déjà, c'est quoi une recommandation LinkedIn ?

Les recommandations LinkedIn sont une version moderne des lettres de
recommandation, sauf qu'elles sont affichées en public sur ton profil
LinkedIn.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/49c78c2b-6a5d-40e0-8006-8f9dad4a9551_3024x1676.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F49c78c2b-6a5d-40e0-8006-8f9dad4a9551_3024x1676.png)

## Pourquoi écrire une recommandation LinkedIn ?

Pour la personne qui reçoit la recommandation

  * Une recommandation est un gage de confiance, de crédibilité et de réputation

  * Cela fait toujours plaisir d'apprendre qu'on est apprécié dans notre travail

  * Cela aide à identifier ses forces et donc à mieux se connaître

Pour la personne qui écrit, cela permet de

  * générer de la réciprocité

  * démontrer que vous êtes enclin à aider votre entourage

  * conscientiser les qualités de l'autre : certaines collaborations sont parfaites sur toute la ligne, d'autres sont plus chaotiques. Quoiqu'il en soit, cet exercice aide à réaliser ce que l'on a apprécié chez l'autre et à relativiser les difficultés que l'on a pu rencontrer ensemble.

Pour l'analogie, c'est comme laisser un avis positif sur un lieu sur Maps :
cela permet de supporter la personne et de lui donner de la crédibilité.

## La difficulté

Écrire une recommandation présente de nombreux intérêts. Mais, écrire une
recommandation pertinente est un exercice délicat, qui peut facilement prendre
beaucoup de temps.

Au cours des 10 dernières années j'en ai écris deux.

C'est peu.

Pourtant, Je pense qu'elle sont plutôt réussies. Les personnes pour qui je les
ai écrites en étaient très contentes, et cela m'a fait plaisir qu'elles soient
touchées. Cependant, chacune m'a demandé plusieurs jours de maturation et j'ai
procédé à plusieurs essais avant de trouver la forme qui me convenait. À
chaque fois, cela m'a demandé beaucoup d'énergie.

C'est là que ChatGPT entre en jeu !

## Le concept

Proposer un outil facilite la génération de recommandation LinkedIn

# Exécution

## Quelques recherches en amont

### Comment écrire une bonne recommandation LinkedIn ?

En recoupant plusieurs articles sur le web et en ajoutant mon expérience
personnelle, je dirais qu'une bonne recommandation LinkedIn :

  * est écrite par une personne légitime : ancien collègue, clients, mentor, ...

  * met en avant les talents de la personne en lien avec ses aspirations professionnelles

  * est authentique : élogieuse sans tomber dans l'excès

  * précise : 

    * le contexte de la relation : la durée, le lieu, la nature de la relation

    * les résultats obtenus ou les contributions apportées par la personne à l'équipe

  * contient une anecdote mettant en avant les soft skills de la personne

  * conclut sur le poste, les missions ou les besoins pour lesquels vous recommandez la personne

### Existe-t-il déjà des générateurs ?

En écumant le web, j'ai pu trouver les générateurs de recommandation LinkedIn
suivants :

\- [Gener-IA-teur de Swile](https://generiateur.swile.co/)

\- [Social Recommendator](https://ai.socialrecommendator.com/) : le générateur
indie

\- [LinkedJetPack](https://www.linkedjetpack.com/linkedin-recommendation-
generator/) : alambiqué

\- [EasyPeasy](https://easy-peasy.ai/fr/templates/linkedin-recommendation-
generator)

\- [Vanling](https://vanling.net/LinkedIn.htm) : le générateur old school

\- [LogicBalls](https://logicballs.com/tools/linkedin-recommendation-
generator)

\- [LazyApply](https://lazyapply.com/linkedin-recommendation-generator)

J'en ai tiré plusieurs observations :

  * il y a une demande pour de tels générateurs : vanling, le plus cheap de tous, a déjà généré plus de 100k recommandations

  * il est possible de faire mieux. Les produits disponibles sont souvent superficiels. Certains sont diablement simple d'utilisation. Ils permettent de générer une recommandation en 3 clic. Mais ils recueillent trop peu de context. Ils produisent ainsi des recommendations génériques qui sonnent creux et manquent d'authenticité.

  * ces générateurs sont tous gratuits : il est peu probable qu'un utilisateur soit enclin à payer pour utiliser un tel outil

## Construire le produit

Mon objectif est d'aider les personnes à générer une recommandation LinkedIn.

La version la plus élémentaire de cet outil serait de partager le prompt que
j'ai conçu. L'avantage est que cela permet de lancer très rapidement et de
toucher un premier public. L'inconvénient, c'est qu'une fois le prompt
partagé, il m'est difficile de suivre sa vie et de collecter du feedback
utilisateur.

Une approche possible serait d'utiliser des outils NoCode ou de programmation
visuelle comme Retool, Noodl ou encore Wized.

Ce projet étant aussi un prétexte pour que je déploie une application web,
j'ai décidé d'aller directement vers un outil plus abouti et de créer un site
dédié à cet unique fonctionnalité.

Le service que j'ai en tête présente la forme suivante :

1\. Poser des questions à la personne

2\. Construire un prompt à partir des réponses

3\. Générer une recommandation avec GPT

4\. Présenter la recommandation à l'utilisateur

### Choisir la stack

De quoi ai-je besoin ?

  * un front-end pour collecter les informations puis afficher les résultats

  * une partie backend pour effectuer des appels à l'API d'OpenAI

  * un système de persistence des données pour analyser les usages

  * une solution d'hébergement

Bon, quelles sont les options ?

Il existe une quantité étourdissante de langages front, back, de frameworks,
de solution d'hébergement et de combinaison de tout cela. Pour simplifier ma
décision, je vais me concentrer sur les langages JavaScript, Python et .NET
que je connais déjà bien. Encore une fois, une bonne façon de procéder ici est
de commencer par la fin : où est-ce qu'on va héberger tout ça ?

#### L'hébergement

Du plus bas niveau au plus haut, on en gros trouver les approches suivantes :

  * Configurer son propre serveur et le faire tourner dans sa chambre, back to basics ! 

  * Louer un serveur virtuel privé et configurer sois-même le serveur : on bascule dans le cloud computing. On s'épargne un ronfleur, mais on est encore sur quelque choses de très bas niveau. Il faut configurer Apache HTTP Server, gérer les sécurité, ...

  * Infrastructure as a Service (IaaS) : Encore trop complexe pour mon besoin, je ne veux pas passer ma semaine à configurer la couche infrastructure. Je n'ai jamais testé AWS et ai eu une expérience laborieuse d'Azure. Je préfère garder ça pour une prochaine fois. 

  * Platform as a Service (Paas) : les PaaS sont moins flexibles que les IaaS, mais permettent de se concentrer sur l'application et de démarrer rapidement, ce qui est idéal pour un minimum viable product (MVP).

Parmis les PaaS, les 4 solutions suivantes me paraissent intéressantes :

  * **Firebase** : existe depuis 2011, Firebase est une solution propriétaire développée par Google. FireBase regroupe un ensemble de composants modulaires qui peuvent être facilement reliés entre eux pour construire une solution complète : base de donnée NoSQL (Cloud FireStore), service d'authentification (Authentication), création de points d'api avec des [[serverless functions - Function as a Service (FaaS)]] (Cloud Functions).

  * **Supabase** : existe depuis 2020, Supabase est une solutions open source qui se positionne directement comme une alternative à Firebase. La société compte dans ses investisseurs des partenaires prestigieux comme le Y Combinator et Mozilla. Elle offre des fonctionnalités similaires à Firebase.

  * **Vercel** : existe depuis 2015. C’est la société qui est derrière le framework React Next.js. Bien qu'initialement centré sur le déploiement du front-end, Vercel offre auhourd'hui une solution quasi-complète avec des solutions de stockage (NoSQL, SQL et Blob) et des fonctions serverless. La plateforme n'offre par contre pas de solution d'authentification clé en main à ce stade.

  * **Netlify** : existe depuis 2014. Couplé à FaunaDB, la plateforme offre elle aussi une solution d'hébergement complète.

Partons sur Firebase.

#### Langage et frameworks

Le fait de partir sur du "pur" Firebase va fortement orienter la suite.

Firebase a récemment introduit des templates dédiés à certains framework
front-end. Cela facilite par exemple le setup d'applications basés sur Angular
ou Next.js (React). J'ai déjà une expérience positive de React. Go pour ce
framework.

De la même façon, Cloud Functions supporte trois langages : Javascript, Python
ou TypeScript (Beta). J'ai d'abord pensé à utiliser TypeScript pour bénéficier
du typage, mais la documentation pour TypeScript est bien moins détaillée.
Finalement, je suis parti sur Python.

Il y a plusieurs intérêts à utiliser python pour le backend :

  * Cela créer une séparation claire entre le front et le back : en fonction du langage, on sait où on est !

  * L'écosystème python est juste dingue en terme de bibliothèques. Que ce soit pour faire du traitement d'image, de l'analyse de données, du machine learning, il est possible de tout faire.

  * Contrairement à TypeScript, il n'est pas nécessaire de transpiler python (ce qui veut dire moins de configuration à gérer)

  * j'adore python

OK, on a notre stack !

  * Hébergement du front-end : Firebase Hosting

  * Authentification : Firebase Auth

  * Framework front-end : [[Next.js]] (React/TypeScript)

  * Backend : Cloud Function for Firebase (Python)

  * Persistence des données : Cloud Firestore

### Développer

> Je ne vas pas entrer dans le détail pas à pas de comment créer une
> application avec Firebase — mais si c'est quelque chose qui t'intéresse,
> fais le moi savoir !

Un truc amusant à raconter ici c'est que, si, après coup, la fonction et le
périmètre de chaque service me parait clair, j'étais dans le brouillard en
abordant les services de Firebase. La première approche que j'ai eu a été
d'avancer pas à pas, de faire avec les zones de flou et de suivre la
documentation.

Il y a de nombreuses façons de monter une app.

#### Premier jet

En première approche, je suis parti de `npm create-next-app` et ai intégré
Firebase à posteriori. J'ai utilisé TypeScript pour le backend et ai setup des
tests automatisés avec jest ainsi qu'un système de formattage automatique avec
Prettier.

Je me suis retrouvé avec une véritable usine à gaz.

L'organisation imbriquée du code source était source de confusion. Avec la
transpilation, je n'étais pas bien sûr de quel code était exécuté où et à quel
moment. Aussi, je rencontrais des problèmes avec la version déployée que je ne
parvenais pas à comprendre.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/ebb9a15f-5b6c-4421-89d1-8eb9532006a5_2336x1712.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2Febb9a15f-5b6c-4421-89d1-8eb9532006a5_2336x1712.jpeg)

#### Remise au propre et simplification

J'ai finalement remis de l'ordre en recréant l'architecture du projet de zéro.
Cette fois-ci, j'ai utilisé uniquement les client firebase. Aussi, j'ai décidé
de ne pas mettre en place de tests automatisés et ni de formatage automatique
du code à ce stade.

Pour se faire, rien de plus simple.

1\. Installer [Node.js](https://www.nodejs.org/) en utilisant
[nvm](https://github.com/creationix/nvm/blob/master/README.md) (Node Version
Manager)

2\. Installer le client Firebase à l'aide de npm (gestionnaire de paquets
installé avec Node.js)

    
    
       npm install -g firebase-tools

3\. Connecter sa machine à Firebase

    
    
       firebase login

4\. Créer un dossier pour le projet et se placer à la racine du projet

    
    
    mkdir writing-a-linkedin-reco
    cd writing-a-linkedin-reco 

5\. Utiliser le client Firebase pour créer l'architecture du projet et se
laisser guider

    
    
       firebase init hosting
       firebase init functions

[![](https://substack-post-
media.s3.amazonaws.com/public/images/abd435ab-54c1-4515-954a-4e2b312bb5b0_2156x1697.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabd435ab-54c1-4515-954a-4e2b312bb5b0_2156x1697.jpeg)

#### La question du formatage

Les outils de formatage automatique sont précieux lorsque la codebase est
maintenue par de nombreuses personnes. Ils permettent d'uniformiser le style
et donc de réduire la charge cognitive qu'implique de lire le code existant.
Dans notre cas, je suis seul, il y a peu de code, et mon style est cohérent
avec moi même. J'ai donc jugé qu'un formatter n'était pas nécessaire.

De plus, pour que ce type d'outil soit vraiment à ton service (et non
l'inverse ...) il est indispensable d'aller au bout de la configuration.
Configurer un hook de pre-commit par exemple permet de lancer le formatage de
façon automatique avant chaque commit, ce qui assure que l'outil est exécuté à
intervalle régulière sans que l'on ai à y penser. Lorsque l'outil est installé
mais configuré à moitié, il représente finalement davantage une charge mentale
puisqu'il faut penser à le lancer manuellement.

### Designer le produit

Afin de designer l'application, j'ai utilisé les techniques suivantes :

  * m'inspirer du design des autres compétiteurs : ce qui marchait bien, ce qui ne me plaisait pas.

  * lire le livre [Refactoring UI](https://www.refactoringui.com/) et appliquer pas à pas les conseils données dans le livre.

  * utiliser le générateur de [Framer](https://www.framer.com/) avec comme instruction "a linkedin recommendation generator app" pour avoir une proposition de design

## Diffuser le produit

Les pistes de diffusions identifiées :

  * publier 50 recommandations à l'aide de l'outil et faire un poste LinkedIn à ce propos

  * proposer l'outil à mon entourage

  * commenter des posts qui listent les outils indispensable pour LinkedIn

  * faire une vidéo Youtube qui présente l'outil

### Exact match domain

En SEO, on parle d'"exact match domain" lorsque l'adresse de site web contient
les mots clés des requêtes ciblées. Un vecteur sur lequel j'ai parié est qu'en
choisissant le nom de domaine `ecrire-une-recommandation-linkedin.fr`, le site
ressortirait naturellement des recherches google "Comment écrire une
recommandation LinkedIn".

A posteriori, il s'avère cependant que "écrire une recommandation linkedin"
correspond à un volume de recherche extrêmement faible :

[![](https://substack-post-
media.s3.amazonaws.com/public/images/98cbd3d8-131e-46db-92f0-97fbf3f020d7_2582x1440.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F98cbd3d8-131e-46db-92f0-97fbf3f020d7_2582x1440.png)Recherche
de mots clés sur [Semrush](https://www.semrush.com/) \- les volumes sont
faibles !

🥴

# Bilan

## Leçons

### Mobile first !

J'ai développé l'application sur desktop. Lorsque je demandais à mon entourage
de tester pour faire des retours, il se produisait systématiquement la même
chose : ils testaient sur mobile et des bugs d'affichages se présentaient.

De fait, en France, [65% du trafic provient des
mobiles](https://www.similarweb.com/fr/platforms/france/). Il semble donc
logique d'optimiser l'affichage en premier lieu pour les mobiles.

Par ailleurs, il est plus simple d'adapter un design mobile vers un design
desktop que l'inverse.

Donc, mobile first !

### Just in time

Je réalise à quel points certains outils qui me paraissent indispensable
lorsque l'on travaille en équipe ne le sont pas lorsque l'on travaille seul et
sur un prototype. Ici, ma priorité est de délivrer le plus rapidement
possible. Mettre en place proprement des outils de formatage automatique et de
test automatisé demande un investissement que je n'ai pas trouvé nécessaire
ici.

### Side-project vs side-business

Je suis allé trop loin dans le développement du produit et dans le design de
l'interface utilisateur pour un minimum viable product (MVP). Le fait de
mélanger un objectif de création de valeur et de génération de revenus
(business) avec un objectif d’apprentissage (project) me conduit à prendre des
décisions qui n’ont pas de sens d’un point de vue économique.

D’un point de vue technique, j’ai pu mettre en pratique et apprendre. Mais
d’un point de vue business, j’ai gâché énormément de ressources car j’aurais
pu tester mes hypothèses plus rapidement.

Pour les prochains produits, je serai davantage focus sur la démarche
économique.

## Monétisation

Je ne pense pas que les gens soient prêt à payer pour accéder à ce service
seul. Les coûts d'exploitation sont cependant relativement faible. S'il y a un
product market fit, la piste du sponsoring me paraît la plus prometteuse.

## Conclusion

Les premiers designs de prompt étaient catastrophiques, j'ai hésité un moment
à laisser tomber. Mais je suis content du résultat final.

Écrire une recommandation permet de réaliser ce qu'il y a de bon chez l'autre.
C'est comme une lettre d'amour. Alors écrivez des recommandations de vos
anciens collègues, le liens est 👉 [ici](https://ecrire-une-recommandation-
linkedin.fr/) 👈 !

Merci de m’avoir lu jusqu’ici et à la prochaine !

🙂

Alexandre

Thanks for reading 100 produits! Subscribe for free to receive new posts and
support my work.

