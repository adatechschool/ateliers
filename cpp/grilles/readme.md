# Découverte des grilles en C++

L'objectif est ici de comprendre comment manipuler une grille (ou tableau multi-dimensionnel) dans le langage C++.
Pour cet atelier, il y a besoin d'ouvrir un nouveau fichier compilable en C++.

## Outils

Si vous ne disposez pas d'une installation C++ fonctionnelle, vous pouvez utiliser
des compilateurs en ligne existants tels que [OnlineGDB](https://www.onlinegdb.com/online_c++_compiler).

## Construction de la grille

Le but de cette étape est de construire une grille à deux dimensions dont les
dimensions (lignes et colonnes) sont choisies aléatoirement (au minimum 4 et au maximum 100 par exemple). Chaque case de la grille pourrait etre remplie d'un caractère aléatoire.

### Ressources
Si ça peut vous aider à construire la grille, vous pouvez faire en sorte de l'afficher
dans le terminal. Allez jeter un oeil à ces histoires [de gestion des flux](https://fr.wikibooks.org/wiki/Programmation_C%2B%2B/Les_entr%C3%A9es-sorties) par exemple.

## Ajout de conditions

Maintenant que nous avons notre grille construite, il est temps de l'utiliser !
Faites en sorte de demander un nombre à l'utilisateur·trice. Si le nombre correspond
à un indice d'une case de la grille, alors le programme affiche la position de la case.
Si ce n'est pas le cas, alors on peut afficher le message `La case n'existe pas!`.

Par exemple, si notre grille a 4 colonnes et 3 lignes, alors notre grille a 12 cases.
Si l'utilisateur·trice indique 3, alors le programme répond `Case(colonne 4, ligne 1)`.
