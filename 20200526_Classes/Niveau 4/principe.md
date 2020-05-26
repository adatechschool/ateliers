## Principe

Il s'agit de recréer le jeu "Puissance 4" : https://fr.wikipedia.org/wiki/Puissance_4

Dans ce jeu, il y a 7 colonnes de 6 lignes, et deux joueurs jouent tour à tour : l'objectif est de créer une ligne de 4 jetons de sa couleur (au moins). Cette ligne peut être verticale, horizontale ou diagonale.

Chaque joueur vient donc glisser un pion dans la colonne de son choix, et ce pion prend automatiquement la première place disponible (tout en bas si la colonne était vide, en deuxième ligne en partant du bas s'il y avait déjà un pion dedans, etc.)

L'objectif est de créer une classe "Partie" qui permette de jouer à Puissance 4 : cette classe aura notamment une méthode "jouer" qui prendra comme paramètre la colonne dans laquelle le joueur actuel veut placer son pion. Il faudra détecter quand un des deux joueurs a gagné, et afficher un message de fécilitations pour ce joueur (numéro 1 ou numéro 2).

Par convention, les colonnes seront numérotées de 1 à 7 (de gauche à droite) et c'est le joueur 1 qui commencera.

Bonus : afficher la grille à chaque coup :-)
