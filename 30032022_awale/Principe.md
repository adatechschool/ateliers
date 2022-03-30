## Étape 0: Avant de commencer...
Cette exercice vise à reproduire le jeu Awalé (ou Awelé) en adoptant une approche orientée objet. Aucun langage n'est imposé, seul le paradigme. Il est donc recommandé de partir sur un langage orienté objet ou un langage multi paradigme qui le supporte.
Vidéo explicative des règles du jeu : https://www.youtube.com/watch?v=J0c-vE-X1x8 (1m30)

## Étape 1: Le plateau de jeu, les bases
- Écrire la classe et les attributs qui matérialisera le plateau de jeu: les cases et les lettres
Il va donc falloir trouver une structure de donnée adaptée au format du plateau où chaque case va devoir contenir un nombre defini de graines
Le lettres servent à pointer une case.
- Y ajouter une première fonction display: affichage du plateau dans la console
- Une seconde fonction isEmpty: le plateau est-il vide ? (toutes les cases à zero)
```
     A  B  C  D  E  F
    (0)(0)(0)(0)(0)(0)
    (0)(0)(0)(0)(0)(0)
     G  H  I  J  K  L
```

## Étape 2: La representation du joueur
- Écrire la classe et les attributs qui serviront à représenter le joueur.
- Ajouter une fonction d'increment du score

## Étape 3: Le début de la fin, la logique de semer/recolter les graines
Voici le coeur du jeu. Notez bien que semer se fait dans un sens et récolter, dans l'autre.
Ces fonctions vont donc devoir s'ajouter à la classe du platedau de jeu.
- saw: semer les graines d'une case aux suivantes
- harvest: recolter les graines d'une case et des precedentes
Il est recommandé de creer une fonction qui retourne la case suivante, en parcourant le plateau de jeu dans un sens ou dans l'autre. Cette (ou ces fonctions si vous en faite deux: une pour un sens et une autre pour l'autre) pourra donc être appelée par les fonctions de saw/harvest.

## Étape 4: Le jeu
- Maintenant que le plus dur est passé, creer la classe et les attributs pour materialiser le jeu. Prendre en compte deux joueurs et une gestion des tours.
Il va donc falloir antinciper:
- l'affichage du plateau et des cores
- la demande demande de saisie et boucle de jeu.
- la gestion de la fin du jeu. Pour un souci de simplicité, on assumera que le jeu se termine quand le plateau et vide.
