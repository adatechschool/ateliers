# Grid Game Tycoon

Votre passion, ce sont les jeux, vous adorez ça ! Surtout lorsque vous vous trouvez devant un Sudoku, un mot fléché, un plateau d'échec, un Scrabble, bref, une **grille**, que vous devez interagir avec, et que la grille évolue.

Vous décidez donc en toute logique de faire de cette passion votre métier.

Malheureusement, vous n'avez pas les fonds pour faire un triple A immédiatement. Vous vous orientez donc d'abord sur quelque chose de plus modeste.

## From scratch

Les grilles, souvenez-vous, c'est vraiment votre truc. Personne ne sait pourquoi, votre entourage trouve ça un peu bizarre, mais c'est ainsi.

Alors évidemment, tous les jeux que vous allez développer seront basés sur une grille d'une façon ou d'une autre.

Il vous faut donc un bon générateur de grille.

- Un générateur qui pourrait, à partir d'une taille de côté `M` - ou 2 tailles `(M,N)` pour une grille rectangulaire -, générer une superbe grille.
- Un générateur qui pourrait, à partir d'un entier `K`, générer une grille (superbe rappelons-le) parsemée de `K` merveilleuses cases pleines (ou noires, ou `True`) dans un océan de `M*N-K` cases vides (ou blanches, ou `False`).
- Ces `K` cases pleines seraient, tel le sel de la vie, réparties aléatoirement sur la grille. À moins que ce ne soient les `M*N-K` qui soient réparties aléatoirement... ¬¬

Générer cette grille en ligne de commande vous semble un premier objectif déjà ambitieux !

## Cachez cette case que je ne saurais voir

Parfait, vous générez des grilles en pagaille ! C'est si apaisant...

Mais imaginez, si la grille était d'abord neutre, et que vous puissiez, les une après les autres, sélectionner les cases (par exemple en renseignant leurs coordonnées en ligne de commande), et les découvrir : soit pleines (ou noires, ou `True`), soit vides (ou blanches, ou `False`) ?

Ce serait tout de même diablement intriguant !

Il vous faut pour cela une logique en boucle :

- La grille est affichée dans un certain état `A`. Au début, cette état est "neutre" : on ne connait pas le contenu des cases.
- Le jeu attend une action, un ordre ; vous l'exécutez (vous renseignez des coordonnées par exemple, ou - si vous vous êtes déjà diversifié dans le graphisme - vous cliquer sur une case, ...).
- Le jeu vous affiche le nouvel état `B` de la grille (l'état `A` plus le résultat de votre action).
- On recommence la boucle avec ce nouvel état `B`.

## Diversifications

### Diversification 1 - Full graphix

La ligne de commande, c'est cool, mais les retours que vous avez eu à la Gamescom étaient mitigés. Vous vous dites que pouvoir faire la même chose, mais avec une interface graphique, ça serait quand même mieux.

L'air du temps pousse dans le sens des clients légers, à travers un navigateur, mais rien ne vous empêche de développer votre propre moteur d'interface !

### Diversification 2 - Démineur FTW

Vous avez un générateur de grille, c'est superbe. L'utiliser pour implémenter un bon vieux démineur, encore mieux !

Les règles du démineur sont assez simples :

- La grille est générée avec un nombre de mines connu, et leurs emplacements sont figés.
- Lorsqu'on interroge la grille (on clique sur une case, ou on renseigne en ligne de commande les coordonnées d'une case, ...), deux cas possibles :
  - La case est occupée par une mine : désolé, vous avez perdu !
  - La case n'est pas occupée par une mine : la chance, vous pouvez continuer !
    - Et en plus, cette case affiche maintenant le nombre de mines dans l'ensemble des 8 cases adjacentes.

### Diversification 3 - Trafalgar

Le démineur s'est très bien vendu ! Ou alors, vous n'êtes pas très fan de ce jeu, il est vrai un peu planplan.

Vous souhaitez utiliser votre générateur de grille dans un autre jeu : la bataille navale.

Les règles sont assez différentes :

- Le jeu se joue à 2, il y a donc 2 grilles à générer en début de partie.
  - Chaque joueur se voit attribué le même lot de bateaux de tailles variables.
  - Chaque joueur doit répartir tous ses bateaux sur sa grille.
  - La grille d'un joueur est invisible pour l'autre joueur.
- Les joueurs jouent les uns après les autres en interrogeant une case de la grille de l'autre joueur. Deux cas possibles :
  - La case n'est pas occupée par un bateau, le tour est fini.
  - La case est occupée par un bateau, dans ce cas le joueur peut rejouer son tour.
  Dans les deux cas, la case devient connu du joueur (il sait si elle était vide, ou occupée par un bateau).
- Le jeu se termine lorsqu'un joueur a découvert tous les bateaux de l'autre joueur.

#### Première étape

Pour commencer, vous vous dites que développer une bataille navale à jouer seul contre l'ordinateur, c'est déjà franchement pas mal.

L'ordinateur peut générer les deux grilles aléatoirement (les formes des bateaux doivent néanmoins êtres respectées !), et lors de son tour, choisir d'interroger aléatoirement une case non découverte de votre grille.

#### Deuxième étape

Vraiment, ça vous chagrine de ne pas pouvoir placer vous-même vos bateaux. Peut-être qu'avant le jeu, vous pourriez sélectionner des cases qui représenteraient vos bateaux, et l'ordinateur vérifierait, avant de lancer le jeu, que votre grille est correcte ?

Ou vous êtes en pleine confiance, et à partir juste d'une case, d'une taille de bateau et d'une direction, bim le bateau se pose tout seul. Attention dans ce cas de bien vérifier que le bateau ne dépasse pas de la grille, ou ne se superpose pas à un autre bateau...

#### Troisième étape

L'ordinateur triche, vous en êtes sûr ! Vous décidez de rajouter un peu de code pour faire un vrai jeu à deux joueur.

Avec par exemple une commande, ou un bouton, qui découvrirait une grille et cacherait l'autre pour permettre au joueur suivant de jouer son tour sans voir vos positions...