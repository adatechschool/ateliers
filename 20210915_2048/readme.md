# 2048

2048 est un jeu de puzzle en 2D, consistant à déplacer sur une grille des blocs contenant des valeurs de nombres, les valeurs de ces blocs étant combinés et additionnés lors de déplacements successifs.

Pour bien comprendre, vous trouverez une implémentation fonctionnelle ici : https://play2048.co/

## Objectif
Implémenter une version basique du jeu 2048.

## Règles du jeu

- A chaque tour, la joueuse choisit une direction (haut, bas, gauche, droite).
- Tous les blocs se déplacent ensuite aussi loin que possible dans cette direction, certains se déplacent ainsi plus que d'autres.
- Deux blocs adjacents (dans cette direction uniquement) avec des valeurs similaires se combinent en un seul portant la somme de ces valeurs.
- Un déplacement est valide lorsqu'au moins un bloc peut être déplacé, ne serait-ce que par combinaison.
- Un nouveau bloc de valeur 2 apparaît à la fin de chaque tour sur une case vide choisie au hasard (s'il y en a une).
- Ajout d'une nouvelle tuile sur un espace vide. La plupart du temps, un nouveau 2 est à ajouter, et occasionnellement (10% du temps), un 4.
- Pour gagner, la joueuse doit créer un bloc avec le numéro 2048.
- La joueuse perd si aucun mouvement valide n'est possible.

## Requirements

- Mouvement "non gourmand".
  Les blocs qui ont été créés en combinant d'autres blocs ne doivent pas être combinés à nouveau au cours du même tour (déplacement).
  
  Par exemple, déplacer la rangée de blocs de `[2][2][2][2]` à droite, doit résulter en `......[4][4]`, et non en `.........[8]`.

- "Priorité au sens de déplacement".
  Si plus d'une variante de combinaison est possible, la direction du mouvement doit indiquer quelle combinaison prendra effet.
  
  Par exemple, déplacer la rangée de blocs de `...[2][2][2]` vers la droite, doit résulter en `......[2][4]`, et non en `......[4][2]`.

- Vérifiez les mouvements valides. Le joueur ne devrait pas pouvoir sauter son tour en essayant un mouvement qui ne change pas le plateau.

- Vérifiez une condition de victoire.

- Recherchez une condition de perte.
