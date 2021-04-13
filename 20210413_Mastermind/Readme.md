# Exercice individuel

## Mastermind

Un grand classique des jeux de société !
Ce jeu se joue avec un joueur qui choisit une combinaison de couleur et un autre joueur qui doit deviner ces couleurs et dans quel ordre. Un codemaker et un codebreaker. A chaque tour, le codebreaker doit faire une proposition, le codemaker doit lui répondre en indiquant le nombre de couleurs bien placées et le nombre de bonne couleur mais mal placées.
Je vous propose de faire cet exercice en python.

### Exemple :
Le code secret : [blue, red, yellow, green]
1er tour : [blue, yellow, purple, red] -> [1,2] = 1 bien placé et bonne couleur et 2 mal placés mais bonne couleur
2eme : [blue, yellow, red, green] -> [2, 2]
…

### Étape par étape :
Faites simple sur les interactions avec l’utilisateur, ne cherchez pas a gerer des le depart les erreurs.
Commencez avec uniquement 2 couleurs et puis vous pourrez augmenter le choix.

## Level 1
Un mastermind simple. Vous rentrez une combinaison de 4 couleurs. Il n'y a que 4 couleurs dans les choix proposés.

## Level 2
Il faut trouver une combinaison de 4 couleurs mais il y a 8 couleurs proposées.

## Level 3
Cette fois-ci vous pourrez jouer sans l'aide de personne puisque c'est l'ordinateur qui compose le code secret à deviner.

## Level 4
Proposez une vraie interface graphique à votre utilisateur pour ce mastermind qui comprend le level 2 et 3.


Comme d'habitude, on vous demande de mettre vos solutions dans votre repo dédié.
