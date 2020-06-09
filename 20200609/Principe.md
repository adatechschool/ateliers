# Katas de déconfinement

## Niveau 1
Je sors de chez moi et je me balade dans la rue. Il y a encore les affiches des élections municipales, mais celles-ci se sont bien usées depuis : sur certaines, le texte s'est tellement effacé que je crois lire des 5 à la place des S, des 0 à la place des O et des 1 à la place des I. Pourriez-vous m'écrire une fonction à qui je donne une chaîne de caractères que je crois lire et qui me renvoie la version corrigée ? Comme les politiciens ne s'engagent pas sur les résultats, vous pouvez être sûr(e) qu'il n'y avait aucun chiffre dans le texte de base :-)

Exemples
```texte_soumis = "PAR15"```
--> votre fonction devrait retourner "PARIS"

## Niveau 2
Je continue ma sortie et je me rends au centre commercial : j'ai besoin d'acheter des composants électroniques. D'habitude, c'est assez simple : le stock de produits sont sur des étagères, et devant chaque produit, une étiquette électronique comme celle-ci indique son prix (comme au supermarché) : https://ixtenso.com/media/story/14774/content-1349010811_hires.jpg.
Malheureusement, quand j'arrive au magasin, les étiquettes de prix ne sont pas encore mises sur les étagères : elles sont toutes dans une boîte, et le nom du produit n'a pas encore été mis sur chacune, juste le prix.

Sachant que j'ai une liste de composants à acheter, pouvez-vous écrire une fonction qui calcule le prix le plus haut et le prix le plus bas que je vais payer ? Vous recevrez en entrée la liste des prix sur les étiquettes + ma liste d'achats.

Exemples

```
etiquettes = [5,7,2,1,4]
liste = ["resistance","condensateur","ecran"]
```

--> votre fonction devrait retourner/afficher "Dans le pire des cas tu paies 16 euros et dans le meilleur des cas 7 euros"
(explications : 5+7+4 = 16 et 2+1+4=7)

``` 
etiquettes = [5,7,2,1,4]
liste = ["microcontroleur","bobine de fil","DEL","bobine de fil"]
```

--> votre fonction devrait retourner/afficher "Dans le pire des cas tu paies 23 euros et dans le meilleur des cas 8 euros"
(explications : 5+7+4+7 = 23 et 2+1+4+1=8)


## Niveau 3

Je décide cette fois-ci d'aller au tabac acheter un jeu à gratter. Le jeu est assez simple, il y a 4 zones à gratter sur chaque ticket : les trois premières zones sont des noms d'animaux, et la dernière est un montant. Si les trois noms d'animaux sont les mêmes, alors on gagne le montant indiqué. Par exemple, "lion lion lion 100" me fait gagner 100 euros.

Les gains possibles sont 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000 et 10000 euros.

Les animaux possibles sont "ane", "baleine", "caribou", "chat", "cheval", "chien", "coq", "daim", "lapin", "lion", "loutre", "rat", "tigre".


Coup de chance pour moi, les tickets sont restés longtemps stockés pendant le confinement, et la partie à gratter s'est un peu enlevée par endroits : si on se dit que le caractère # représente la zone à gratter, on a par exemple : ##o# #### #i## ##0.

Sachant que je n'achète mes tickets que par 6, et en supposant qu'il y a maximum un caractère découvert par mot, sauriez-vous me dire quel est le montant maximum que je peux gagner si je vous montre mes tickets ?

Exemples :
```
tickets = [
"t#### #i### ####r 1##",
"r##### d##### ###### ####0",
"### ane ### ###0",
"### ### ### 1#",
"####e #####y r## ###0",
"r##### r## r## ###"
]
```

--> votre fonction devrait retourner "5110"

Explications:

```
"t#### #i### ####r 1##" --> pourrait me faire gagner 100 euros si c'est tiger tiger tiger
"r##### d##### ###### ####0" --> perdant
"### ane ### ###0" --> pourrait me faire gagner jusqu'à 5000 euros si c'est ane ane ane
"### ### ### 10" --> pourrait me faire gagner 10 euros
"####e #####y r## ###0" --> perdant
"r##### r## r## ###" --> perdant
```
Je peux donc gagner jusqu'à 100+5000+10= 5110 euros
