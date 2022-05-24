# La vie de Pi

Vous vous réveillez ce matin avec l'envie incontrôlable de connaître la valeur
de $\pi$. Pas de bol, vous n'avez rien sous la main qui vous permette de la
calculer !

En bonne informaticienne, vous décidez de coder un programme pour le calculer
vous-même...

## Un peu de théorie

La méthode qu'on cherchera à développer est celle dite de Monte-Carlo. Elle se
base sur les nombres aléatoires pour obtenir une approximation de $\pi$.

Cette méthode est abondamment expliquée sur Internet, avec le défaut que la
plupart des explications sont accompagnées d'une implémentation (en `Python`
généralement) ! Si vous ne voulez pas vous gâcher la surprise, je vous propose
cette explication rapide. Si vous ne voulez pas vous prendre la tête avec les
math, passez directement au chapitre [TL;DR](#tldr).

### Surfaces et ratio

Prenons un cercle de rayon $1$, enfermé dans un carré de côté $2$. Les deux formes
ont le même centre.

Les surfaces de ces figures géométriques sont: pour le carré, $2 ^ 2$, soit
$4$, et pour le cercle, $\pi * r ^ 2$, soit ici avec un rayon de 1, exactement
$\pi$.

À ce stade, nous voyons que le ratio entre la surface du cercle, et la surface
du carré vaut $\pi / 4$ : le cercle occupe $\pi / 4$, soit environ un peu plus
de 78%, de la surface du carré.

### Construction d'un plan

Maintenant, prenons un quart (par exemple le quart en haut à droite) de ces
figures. Les surfaces de ces quarts sont maintenant 1 pour le quart de carré,
et $\pi / 4$ pour le quart de cercle. On retombe naturellement sur le même ratio
que tout à l'heure : le quart de cercle occupe toujours $\pi / 4$ de la surface
du quart de carré.

Utilisons les bords du bas et de gauche comme axes $x$ et $y$, $(0, 0)$ étant le
point en bas à gauche. Tous les points répartis sur la surface peuvent ainsi
être définis avec des coordonnées $(x, y)$. On peut également calculer la
distance $d$ de chaque point par rapport au point $(0, 0)$ en appliquant la formule
de Pythagore : $x^2 + y^2 = d^2$.

Par exemple, tous les points sur le bord du cercle, qui est de rayon 1, sont à
des coordonnées $(x, y)$ telles que $x^2 + y^2 = 1$. les points dans le cercle
sont donc tous les points tels que $x^2 + y^2 <= 1$

![Illustration](https://media.eduscol.education.fr/ftp_eduscol/2019/Ressources/Mathematiques/img/monteCarlo.png)

### Nombres aléatoires

Pour cet exercice, nous avons besoin d'une fonction qui retourne des nombres
aléatoires entre $0$ et $1$.

Nous allons en générer un grand nombre, deux par deux. Chaque couple de nombre
aléatoire nous servira à représenter un point sur notre surface, avec les
coordonnées $(x, y) = (premiernombrealéatoire, secondnombrealéatoire)$.

Les données étant aléatoires, si on en demandait à l'infini, les points qui nous
construisons finiraient par recouvrir toute la surface de nos figures ! C'est à
dire qu'on aurait une équivalence entre le nombre de point qui tomberaient à
l'intérieur du cercle par rapport à l'ensemble des points (qui tombent à
l'intérieur du carré) et le ratio entre la surface du cercle par rapport à la
surface du carré : $\pi / 4$ !

La formule serait : $(nombre de points dans le cercle) / (nombre total de points) = \pi / 4$.

Mais comme nous cherchons une approximation, nous n'avons pas besoin d'une
infinité de nombres aléatoires. Un grand nombre nous suffira.

### TL;DR

- Nous allons tirer une grande quantité de nombres aléatoires entre 0 et 1,
  regroupés deux par deux.
- Pour chaque groupe de deux nombres aléatoires $(x, y)$, nous calculons la
  formule $x ^ 2 + y ^ 2$.

  - si le résultat est plus petit ou égal à 1, alors nous incrémentons de 1
    une variable `inside` (nom de la variable au choix),
  - dans tous les cas, nous incrémentons de 1 une autre variable `total`.

- Une fois un grand nombre de points calculés, nous allons faire le ratio
  entre le nombre `inside` et le nombre `total`.

- Nous utiliserons ce ration pour calculer $\pi$ grâce à la formule
  $inside / total = \pi / 4$, que nous pouvons écrire
  $\pi = 4 * (inside / total)$

## Découverte

Codez votre calculateur de $\pi$ dans un langage avec lequel vous êtes
confortable.

Augmentez petit à petit la quantité de nombres aléatoires ; vous devriez voir
que votre estimation est de plus en plus précise (même si, les nombres étant
aléatoires, vous pouvez parfois avoir l'impression de régresser).

Si vous avez utilisé un langage comme `JavaScript` ou `Python`, vous
expérimenterez probablement un certain ralentissement lorsque vous calculerez
avec plusieurs millions de points.

## Performance

Une fois confortable avec l'algorithme, et lorsque vous touchez aux limites
de votre premier choix de langage, recodez-le en `C`. Vous devriez expérimenter
une amélioration des performances.