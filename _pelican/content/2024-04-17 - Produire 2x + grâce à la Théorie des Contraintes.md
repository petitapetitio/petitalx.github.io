---
date: 2024-04-17T05:39:47.941Z
title: Produire 2x + grâce à la Théorie des Contraintes
subtitle: Explications et simulations de la méthode.
---

Hello !

Depuis le mois de février, mon focus est d'apprendre le DevOps.

En m'attaquant à cette compétence, je pensais baigner dans de la technique.

Et il y en a.

Mais j’ai aussi découvert une dimension culturelle super importante.

Remonter aux origines du DevOps m'a conduit au Lean Manufacturing et à des
livres comme _Toyota Production System - Beyond large scale production_ de
Taiichi Ohno ou encore _The Goal - A processus of ongoing improvements_ de
Goldratt Eliyahu.

Une des obsessions du Lean est de fluidifier les flux de production (le flow).

Dans cette édition, on va voir comment des principes simples mais parfois
contre-intuitifs nous permettent d'y parvenir.

Dans cette édition, on s'attaque à la Théorie des Contraintes.

# Le livre

The Goal est une _business fiction_ écrite par Eliyahu M. Goldratt, un
scientifique et gourou de la gestion d'entreprise Israëlien et Jeff Cox. Il a
été publié pour la première fois en 1984, introduit la Théorie des
Contraintes, et a été vendu à plus de 10 millions d'exemplaires.

L’intrigue du livre est la suivante : Alex Rogo est directeur d'usine dans une
ville avec un grand passé industriel mais un avenir incertain. Il aime
l'atmosphère de l'usine, et s'applique dans son travail, mais les résultats ne
sont pas au rendez-vous. Le site est menacé de fermeture. Il dispose de trois
mois pour renverser la vapeur.

Au hasard d'un voyage, il recroise Jonah. Son ancien professeur de physique
est aujourd'hui consultant pour de grandes entreprises. Jonah porte la
connaissance de Goldratt et sera son mentor tout au long du récit.

# La méthode

Dans The Goal, Goldratt expose une méthode d’amélioration en 1+5 étapes :

  0. Définir l’objectif

  1. Identifier la contrainte

  2. Exploiter la contrainte

  3. Subordonner à la contrainte

  4. Élever la contrainte

  5. Répéter

## Préalable : définir l'objectif

Cela paraît évident, mais la question n'est pas triviale.

Que cherche-t-on à réaliser, exactement ?

Dans les premiers chapitres de _The Goal_ , Jonah interroge Alex. Et Alex
s'interroge.

Quel est le premier but d'une entreprise ?

  * fournir des emplois ?

  * la technologie ? 

  * réduire les coûts ?

  * produire ?

  * implémenter les bonnes pratiques ?

  * être _compliant_ ?

  * satisfaire ses utilisateurs ?

  * faire de l'argent ? 

Vous avez un avis ?

Pour ma part, je n'étais pas bien sûr lorsqu'ils ont soulevé la question.

Et ce manque de certitude est intéressant car souligne plusieurs problèmes.

  1. Derrière les évidences, l'objectif n'est pas toujours clair. Or, il est difficile d'atteindre une cible lorsqu'on ne sait pas où elle est. À l'aveugle, on peut vite se retrouver à lancer des fléchettes en face alors que la cible est dans notre dos. Pour aller d'un point A à un point B, il faut commencer par définir le point B.

  2. Si chaque personne a une vision différente du but de l'entreprise, il va être difficile d'avancer tous ensemble dans la même direction.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/24688993-c3e6-4ba2-a781-2a223e813cce_991x677.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F24688993-c3e6-4ba2-a781-2a223e813cce_991x677.png)Mettez-
vous d’accord ^^’.

La réponse de Jonah est simple.

Les entreprises poursuivent un seul but, et ce but est généralement le même :

“faire de l'argent”

Fournir des emplois, la technologie, produire, implémenter les bonnes
pratiques, être _compliant_ et satisfaire les utilisateurs sont des moyens
valables de parvenir au but de l’entreprise mais ne sont pas son objectif
premier.

## Étape 1 : Identifier la contrainte

On connaît désormais notre objectif. 🎉

L'étape suivante consiste à identifier ce qui nous freine vers notre objectif
: la contrainte, que l'on peut aussi voir comme un goulot d'étranglement
(bottleneck).

Pour la repérer, nous allons visualiser notre système et introduire la notion
de chaîne de valeur.

La chaîne de valeur est l'ensemble des étapes qui vont des premières étapes de
la création de valeur à la livraison chez le client.

Comme le dit la sagesse populaire et le confirme la physique, la force d'une
chaîne dépend de son maillon le plus faible. De la même façon, le débit d'un
système dépend de son élément le plus contraignant.

### Quelques simulations

L'essence de la théorie des contraintes est résumée par cette citation de
Goldratt :

> In any value stream, there is always a direction of flow, and there is
> always one and only constraint. Any improvement not made at that constraint
> is an illusion. If we improve a work center that is positioned before the
> constraint, work will merely pile up at the bottleneck even faster, waiting
> for work to be performed by the bottlenecked work center. On the other hand,
> if we improve a work center positioned after the bottleneck, it remains
> starved, waiting for work to clear the bottleneck.

Voici un système simple avec trois éléments, une direction de flow et une
contrainte. Dans la suite, nous allons faire varier ses caractéristiques et
mesurer le débit de chaque version.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/981df4bd-4d08-49e5-8ee4-7463dfcffce4_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F981df4bd-4d08-49e5-8ee4-7463dfcffce4_800x400.gif)La
contrainte (an centre) détermine le débit du système — Débit = 56

Si l’on optimise le système en **aval** de la contrainte, on obtient le flux
suivant :

[![](https://substack-post-
media.s3.amazonaws.com/public/images/29c55f86-5a66-4c79-9448-dd4794c00493_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F29c55f86-5a66-4c79-9448-dd4794c00493_800x400.gif)Simulation
d’une optimisation en aval de la contrainte : l’amélioration en aval n’a aucun
impact sur le débit du système. — Débit = 53

Si l’on optimise le système en **amont** de la contrainte, on obtient le flux
suivant :

[![](https://substack-post-
media.s3.amazonaws.com/public/images/51d141b6-83c1-4e69-acef-3897523df5b1_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F51d141b6-83c1-4e69-acef-3897523df5b1_800x400.gif)Simulation
d’une optimisation en amont de la contrainte. L’amélioration en amont a en
fait un impact négatif sur le débit du système. — Débit = 43

Jusque-là, ces simulations confirment l’affirmation de Goldratt. Les
améliorations en amont et en aval n’ont pas donné de résultats positifs. Pour
obtenir une amélioration globale, on va commencer par identifier la
contrainte.

### Mettre le doigt sur le bottleneck

Dans un système matériel comme usine, les goulots d'étranglement sont simples
à identifier : il suffit de se promener dans l'usine. Lorsque tu tombes sur
une machine avec beaucoup de travail qui s'accumule devant, tu tiens ton
bottleneck.

Dans un système virtuel, un travail préalable est nécessaire pour **rendre le
travail visible**. Les contours de la chaîne de valeur peuvent être dessinés
en réunissant les parties prenantes du système dans un atelier. Ensuite, le
flux des opérations peut être monitoré avec des techniques de management
visuelles comme Kanban.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/efb0124a-3564-4e2e-ad00-eb41fc4f004d_2704x642.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefb0124a-3564-4e2e-ad00-eb41fc4f004d_2704x642.png)Illustrations
d’un Kanban pour le développement d’une MarketPlace. Les tickets sont insérés
à gauche puis déplacé dans chaque colonne jusqu’au déploiement. Si le travail
s’accumule à l’étape “à déployer” (DevDone), c’est que le pipeline de
déploiement est un bottleneck :).

Le bottleneck peut être n'importe où sur ta chaîne de valeur.

Et il peut être de différente nature :

  * **une machine critique**

  * **une personne** : dans les équipes informatiques, il arrive que certaines personnes soient le bottleneck. Loin d'être des incompétents, ce sont en général des personnes talentueuses. Elles connaissent bien le système et l'entreprise repose dessus pour résoudre ses problèmes. Ce sont des _Knowledge Holders_. Mais ces personnes sont une faiblesse dans le processus car elles sont les seules à savoir réaliser certaines opérations. Or leur temps disponible n'est pas scalable et elles présentent un risque pour l'entreprise si elles gagnent au Loto. 

  * **le marché** : la demande du marché borne ta capacité de vente. Si tu produis plus que ce dont le marché a besoin, alors tes inventaires vont exploser. L'argent que tu investis reste coincé dans le système, et la santé financière de l'entreprise est en danger.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/347a7f50-9755-4c5c-8b15-6e54b49776b9_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F347a7f50-9755-4c5c-8b15-6e54b49776b9_800x400.gif)Lorsque
le marché est le bottleneck.

Une fois la contrainte identifiée, on va pouvoir commencer à optimiser le
processus.

### Aparté : les optimisations aveugles dans le logiciel

Notons encore une fois que commencer à "optimiser" le système avant ce travail
d'identification est une source de gâchis.

Il faut garder en tête que

  * Travailler sur des parties non-critiques représente un **coût d'opportunité** : l'effort aurait pu être dépensé ailleurs et apporter davantage de résultats.

  * **Tout à un prix**. Le revers des optimisations est qu'elles se font souvent au prix de coupler le code et de dénormaliser des structures de données. Cela améliore les performances mais réduit la maintenabilité et complexifie le débogage.

Par exemple, le Domain Driven Design (DDD) est une approche du design
logicielle qui supporte le bien la complexité métier. La contrepartie du DDD
est que les performances sont réputées mauvaises. La maintenabilité se fait au
prix de la performance. À l’inverse, le code assembleur permet d'obtenir des
performances incomparables. Mais il est très difficile de lire, d'écrire et de
maintenir un programme en assembleur.

## Étape 2 : Exploiter la contrainte

La contrainte détermine le débit du système.

Comment tirer un maximum de la contrainte ?

On peut ici appliquer 4 techniques :

  * **le buffer.** S'assurer que la contrainte à toujours au moins un élément à traiter : une heure perdue sur la contrainte est une heure perdue dans tout le système. La contrainte ne doit jamais être en attente.

  * **l’offload.** Décharger la contrainte : si certaines tâches réalisées par la contrainte peuvent être réalisées par d'autres ressources alors leur réaffecter. 

  * **les contrôles.** Placer les contrôles qualités en amont de la contrainte : si les inputs de la contrainte sont défectueux et que le défaut est détecté après être passé par la contrainte, le produit sera rejeté et on aura gâché un temps précieux.

  * **la protection.** Empêcher le _travail non planifié_ de perturber les tâches importantes. Le travail non planifié est la matière noire du système. Il est souvent invisible et chasse le travail planifié. 

La vidéo ci-dessus illustre l’impact du travail non planifié sur la fluidité
du système.

Sur la route 1, on observe le travail tiré du backlog.

Tout se passe bien, jusqu’à l’entrée en jeu de la route 2.

## Étape 3 : Subordonner les opérations à la contrainte

Cette étape est la plus contre-intuitive.

Une des grandes leçons du Lean Manufacturing est que l'inventaire est un
passif, et que les excès d’inventaire sont une source de gâchis :

  * lorsque notre liste de tâches à accomplir s'accumule, cela génère du stress et nous rend plus susceptible de commettre des erreurs.

  * lorsque la quantité de pièces "à traiter" s'accumule devant une étape de la production, cela génère du stock. Lorsque ce stock grandit, il faut le gérer : créer un endroit pour le stocker, le stocker, le ressortir au bon moment. Cela entraîne des coûts de manutentions et des risques d'abîmer les pièces.

Produire à fond la caisse en amont de la contrainte est une source de gâchis.

Parfois, il vaut mieux ne rien faire.

Le lead-time est le temps moyen que prend un élément pour aller de gauche à
droite de la chaîne de valeur. Le stock fait exploser le _lead-time_ et crée
des bouchons dans le pipeline.

Subordonner les opérations à la contrainte permet de garder un bon lead-time.

Un bon lead-time permet de "win in the marketplace".

[![](https://substack-post-
media.s3.amazonaws.com/public/images/556ccf6b-6831-4d4e-97ec-398687bf7cb7_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F556ccf6b-6831-4d4e-97ec-398687bf7cb7_800x400.gif)Ralentir
la production en amont de la contrainte et produire plus. — Débit = 74

## Étape 4 : Élever la contrainte

C'est le moment de sortir le cric.

Une façon d'augmenter le débit des opérations est simplement d'augmenter la
capacité de la contrainte.

Dans le cas d'une machine, il s'agit d'en ajouter une de même capacité en
parallèle. Dans le cas _d'un détenteur de connaissance_ , il s'agit de
documenter chaque action qu'il réalise.

[![](https://substack-post-
media.s3.amazonaws.com/public/images/a9b53e89-038e-4bea-8053-d666c0d9b885_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9b53e89-038e-4bea-8053-d666c0d9b885_800x400.gif)

## Étape 6 : Répéter avec la nouvelle contrainte

La théorie des contraintes est un processus d'amélioration continu. Une fois
le bottleneck traité, un autre va apparaître à un autre endroit de la chaîne
de valeur. C'est désormais cette contrainte qui va dimensionner le flux des
opérations.

# Conclusion

Lorsque l’on cherche à améliorer un système, notre première réaction est
souvent de chercher à ajouter de la capacité. C’est notre tendance à penser de
façon additive.  
  
Ce que nous montre la théorie des contraintes, c’est que cette stratégie n’est
pas la seule façon d’atteindre nos objectifs. Conduite à l’aveugle, ajouter de
la capacité peut même desservir le système.

Une fois clarifié notre but et identifié la contrainte, plusieurs approches
s’offrent à nous. Désoptimiser des ressources en amont pour les mettre au
service de la contrainte. Adapter la cadence à la contrainte. Décharger la
contrainte. Protéger son temps. Ou enfin augmenter la capacité de la
contrainte.

Un des grandes leçons que je retiens de cette théorie est que tu peux faire
mieux avec ce que tu as déjà. Dans bien des cas, il suffit de réorganiser les
ressources existantes et de corriger les déséquilibres pour améliorer le
système.

Dans le prochain épisode, je te partagerai comment j’ai appliqué les principes
de la Théorie des contraintes à mon processus de création de contenu et les
changements surprenants que cela m’a amené à considérer.

D’ici là, est-ce que tu vois un domaine ou tu pourrais l’appliquer ?

Portez-vous bien et à la semaine prochaine :)

Alex

Thank you for reading 100 produits. This post is public so feel free to share
it.

[Share](https://100produits.substack.com/p/produire-2x-grace-a-la-theorie-
des?utm_source=substack&utm_medium=email&utm_content=share&action=share)

# Bonus

  * [le code que j’ai utilisé pour créer les animations est disponible ici](https://github.com/lxnd-dune/theory-of-constraints)

  * l’autre hack pour optimiser le système est de réduire la taille des lots :

[![](https://substack-post-
media.s3.amazonaws.com/public/images/6d2f6e65-add6-4d67-8db0-f9b0ba42fca7_800x400.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-
post-
media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d2f6e65-add6-4d67-8db0-f9b0ba42fca7_800x400.gif)Lorsque
l’on réduit la taille des lots, il même possible d’augmenter la cadence sans
entraîner de blocage dans le système.

