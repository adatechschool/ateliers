## Principe

Il s'agit de recréer le jeu "Puissance 4" : https://fr.wikipedia.org/wiki/Puissance_4

Dans ce jeu, il y a 7 colonnes de 6 lignes, et deux joueurs jouent tour à tour : l'objectif est de créer une ligne de 4 jetons de sa couleur (au moins). Cette ligne peut être verticale, horizontale ou diagonale.

Chaque joueur vient donc glisser un pion dans la colonne de son choix, et ce pion prend automatiquement la première place disponible (tout en bas si la colonne était vide, en deuxième ligne en partant du bas s'il y avait déjà un pion dedans, etc.)

## Niveau 1 - structure

L'objectif est de créer une classe "Partie" qui permette de jouer à Puissance 4 : cette classe aura notamment une méthode "jouer" qui prendra comme paramètre la colonne dans laquelle le joueur actuel veut placer son pion. Il faudra détecter quand un des deux joueurs a gagné, et afficher un message de fécilitations pour ce joueur (numéro 1 ou numéro 2).

Par convention, les colonnes seront numérotées de 1 à 7 (de gauche à droite) et c'est le joueur 1 qui commencera.

## Niveau 2 - méthodes

Créer une méthode "afficher" qui affiche la grille de jeu

## Niveau 3 - encapsulation et instanciation

Nous allons maintenant créer une classe Joueur afin que chaque joueur puisse donner son nom en début de partie.

La classe devra aussi contenir le nombre de victoire de chaque joueur et ce compteur devra, bien sûr, être incrémenté à chaque victoire du joueur
Créer pour cela une methode "hasWon" appellée dans la méthode "jouer" qui vérifie si le coup est gagnant et qui devra incrémenter une valeur dans l'objet du joueur gagnat

## Niveau 4 - Heritage

Nous allons maintenant créer une nouvelle class qui devra hériter de la classe Partie mais qui changera les règles de jeu. 
Les joueurs doivent pouvoir choisir quel jeu ils lancent au début.

Nous vous proposons une variante où il faut aligner 5 pions et l'affichage se fait avec des couleurs (ou symbole différent), mais vous povez imaginer d'autres alternatives !
