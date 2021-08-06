# Calcul de nombres premiers

## Introduction

Un nombre premier se définit comme un entier ayant exactement 2 diviseurs :
``1`` et lui-même. Avec cette définition, ``2`` est le premier nombre premier.

Les nombres premiers ont une place spéciale en cryptographie, notamment dans
[l'algorithme RSA](https://interstices.info/nombres-premiers-et-cryptologie-lalgorithme-rsa/),
publié en 1978 et encore massivement utilisé pour chiffrer les échanges sur
Internet.

Il y a plusieurs méthodes pour calculer des nombres premiers, nous chercherons
aujourd'hui à implémenter la méthode la plus naturelle, qui colle à la
définition d'un nombre premier, pour ensuite l'optimiser.

Langage : libre


## Étape 1 - Test de divisibilité

La toute première étape est d'avoir une fonction qui dit si un entier est
divisable par un autre. Cette fonction peut être très courte, au point de se
demander s'il est bien utile d'en faire une fonction - mais oui, c'est le genre
de code qu'on ne veut pas dupliquer, et ça nous servira à plusieurs endroits.

Codez une fonction prenant en argument deux entiers : l'entier à tester, et un
diviseur ; et qui retourne un booléen renseignant si oui ou non l'entier à
tester est bien divisible (de façon entière) par le diviseur.


## Étape 2 - Test de primauté

Pour déterminer si un nombre est premier, nous allons implémenter l'algorithme de
détection suivante :

1. soit un entier ``N``,
2. pour chaque entier ``k`` strictement supérieur à ``1`` et strictement inférieur à ``N`` :

  - soit ``N`` est divisible par ``k``, dans ce cas on a notre réponse : **``N``
    n'est pas un nombre premier**,
  - soit ``N`` n'est pas divisible par ``k``, il faut continuer à tester des
    diviseurs,

3. si ``N``n'est divisible par aucun des ``k``, alors **``N`` est un nombre
   premier**.

En utilisant la fonction codée lors de l'étape 1, développez une fonction
prenant en argument un entier à tester, et qui essaie de le diviser par tous
les entiers inférieurs à lui, et qui retourne si oui (il n'est pas premier) on
non (il est premier) il est divisible par un de ces entiers.

Vous avez maintenant un code qui vous permet de vérifier si un entier est
premier ou non.


## Étape 3 - Recherche de nombre premiers

Imaginons maintenant que nous voulions non pas vérifier qu'un entier est premier
ou non, mais itérer l'ensemble des entiers pour ne sélectionner que les
premiers. Par exemple, nous pourrions vouloir un programme qui nous calcule les
``N`` premiers nombres premiers.

Nous pouvons réutiliser le code développé à l'étape 2 pour résoudre ce problème.
L'algorithme peut s'exprimer de cette façon :

1. soit une liste ``L``, initialisée avec le premier nombre premier (``2``),
   devant contenir les nombres premiers trouvés,
2. soit un entier ``k``, dont la primauté sera testée, initialisé à ``3``
   (l'entier suivant ``2``)
3. tant que la taille de la liste ``L`` est inférieure à ``N``, le nombre de
   premiers désirés:

   - si ``k`` est un nombre premier (utiliser la fonction de l'étape 2), on
     l'ajoute à la liste ``L``
   - dans tous les cas, on incrémente ``k`` de ``1``

4. une fois sortie de la boucle, on affiche la liste ``L`` des ``N`` premiers
   nombres premiers calculés.


> **N.B :** On remarquera que cet algorithme renvoie une réponse fausse si
> ``N = 0`` (puisqu'on initialise ``L`` à ``[2]``, l'algorithme nous répondra
> ``[2]`` si on lui demande les ``0`` premiers nombres premiers), mais on
> s'autorisera cette petite liberté.


## Étapes 4 - Optimisations


> Lorsqu'on se lance dans de l'optimisation logiciel, il est important de mettre
> en place des systèmes de relevés de métriques permettant de valider nos
> tentatives d'optimisations.

> Il est donc conseillé à ce stade de d'abord développer du code permettant
> d'afficher le temps pris par nos fonctions pour calculer la liste des nombres
> premiers demandée.

Notre algorithme fonctionne, mais il pourrait être beaucoup plus efficace.

Actuellement, il utilise deux boucles, car il se base sur deux postulats :

- tous les entiers sont considérés comme des candidats potentiels à la primauté
  (étape 3)
- tous les entiers inférieurs à un candidats sont considérés comme des
  diviseurs intéressants (étape 2)

Hors ces deux postulats peuvent être rafinés :

### Limiter le nombre de candidats

Il existe un moyen assez simple de diviser par deux le nombre de candidats à la
primauté : par définition, ne devant pas être divisible par un autre entier que
``1`` ou eux-même, **aucun nombre pair, sauf ``2``, ne peut être un nombre
premier**.

Trouver le moyen, dans la fonction développée à l'étape 3, de ne tester que les
entiers impaires.

### Limiter le nombre de diviseurs

#### Premier découpage

Actuellement, les diviseurs ``k`` d'un candidat ``N`` sont tous les entiers
entre ``2`` et ``N``.

Par définition d'une division entière, on cherche à vérifier si ``N = k * l``.

On peut avoir l'intuition qu'il n'y a tout d'abord aucun intérêt à tester des
diviseurs tels que ``k > N/2`` ; par exemple on voit qu'il est inutile d'essayer
de diviser ``12`` par ``7``, ``8``, ``9``, ``10`` ou ``11``.

Mais en fait, on peut démontrer que les seuls diviseurs intéressants sont ceux
tels que ``k^2 < N`` ! (les ``k`` inférieurs à la racine carrée de ``N``)

Par exemple, les diviseurs possibles de ``264`` sont ``2``, ``3``, ``4``, ``6``,
``8``, ``11``, ``12``, ``22``, ``24``, ``33``, ``44``, ``66``, ``88`` et
``132``. On a également `` 16^2 (256) < 264 < 17^2 (289)``. Il n'est pas
nécessaire de tester des entier ``k`` plus grand que ``16``, il suffit de
diviser par ``2``, ``3``, ``4``, ``6``, ``8``, ``11``, ``12``, car les entiers
``22``, ``24``, ``33``, ``44``, ``66``, ``88`` et ``132`` sont déjà testés :
ils correspondent à des ``l`` (``264 = 22*12 = 24*11 = 33*8 = 44*6 = 66*4 =
88*3 = 132*2``).

Il faut donc modifier la fonction développée à l'étape 2 pour qu'elle n'utilise
pas comme diviseurs

> *chaque entier ``k`` inférieur à ``N``*

mais plutôt

> *chaque entier ``k`` inférieur à la racine carrée de ``N``*

> **N.B :** en [complexité logicielle](https://fr.wikipedia.org/wiki/Analyse_de_la_complexit%C3%A9_des_algorithmes),
> cette optimisation en racine carrée est beaucoup plus intéressante que la
> première (division par deux) car elle permet de changer d'ordre de grandeur
> lorsqu'on utilise des grands nombres en entrée.

> Avec des petits nombres, par exemple si on avait initialement ``6`` diviseurs
> possibles, diviser le nombre de ces diviseurs par deux permet de ne tester que
> ``3`` diviseurs, alors que la racine carrée permet de ne tester que ``2``
> diviseurs ; la différence n'est pas énorme (voire négligeable).

> Par contre avec ``10 000`` diviseurs, une division par ``2`` permet de descendre
> à ``5 000`` diviseurs ; c'est pas mal mais on reste dans le même ordre de
> grandeur : les milliers. Par contre une racine carrée permet de descendre à
> ``100``, ce qui est là très significatif.

#### Deuxième découpage

Il est possible de limiter encore plus le nombre de diviseurs.

Comme dans le découpage des candidats, on voit qu'il ne sert à rien de tester
des diviseurs pairs, à part ``2`` : inutile d'essayer de diviser par ``4``,
``6``, ``8``, ``10``, ... car si un candidat est divisible par ces nombres,
ça signifie qu'il est également divisible par ``2``, qui aura déjà été testé.

Mais c'est également vrai pour les multiples de ``3`` (``6``, ``9``, ``12``,
...). Et également les multiples de ``5``, de ``7``, de ``11``, de ``13``, ...

En fait c'est vrai pour tous les multiples de nombres premiers : **il n'est pas
utile de tester d'autres diviseurs que les nombres premiers**. En reprennant
l'exemple de l'entier ``264``, les seuls diviseurs à tester sont : ``2``, ``3``,
``5``, ``7``, ``11`` et ``13`` (les nombres premiers inférieurs ou égaux à
``16``).

Ça tombe bien : dans notre étape 3, on manipule une liste ``L`` qui contient
les nombres premiers justement.

Il faut donc modifier la fonction développée à l'étape 2 et amélioré à l'étape
précédente, pour qu'elle n'utilise pas comme diviseurs

> *chaque entier ``k`` inférieur à la racine carrée de ``N``*

mais plutôt

> *chaque entier ``k`` de la liste ``L``, inférieur à la racine carrée de ``N``*
