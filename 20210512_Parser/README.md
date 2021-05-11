# Parser d'expression mathématique

## Introduction

Nous allons essayer de coder un parser d'expressions mathématique simples.

Simples, car nous poserons les limitations suivantes :

1. les seules opérateurs possibles seront `+`, `-`, `*` et `/` (cette dernière en
   division réelle, pas entière),
2. les règles de priorités seront les plus simples : `*` et `/` doivent se
   résoudre avant `+` et `-`, mais les parenthèses ou tout syntaxe changeant les
   priorités ne seront pas utilisées,
3. les nombres ne peuvent pas être négatifs, même si le résultat final peut
   l'être,
4. tous les éléments des expressions seront séparés les uns des autres par un
   espace.

Les expressions mathématiques seront sous la forme d'une chaîne de caractères,
par exemple :

- `"0"`
- `"4 + 8"`
- `"98 * 6.3 + 45 - 7 / 2 + 87"`

Ces expressions ne seront **pas** valides :

- `"3 * -2"` (nombre négatif)
- `"4 * ( 5 + 6 )"` (parenthèses)
- `"4*3"` (espaces manquants)

Le choix du langage utilisé est libre.


## Étape 1 - Parsing

Créez une première fonction `A` qui prend une chaîne de caractère et retourne
une liste de tous ses éléments dans l'ordre (nombres et opérateurs).

```
A("4 + 6.2 * 8")
> ["4", "+", "6.2", "*", "8"]
```

## Étape 2 - Qualification des éléments

Pour le moment, en sortie de `A` tous les éléments sont des chaînes de
caractères - pas bien utile pour faire une opération mathématique.

Développer une fonction `B` qui prend en entrée une liste de chaîne de
caractères (typiquement le résultat de la fonction `A`) et retourne
une liste d'éléments ayant pour type :
- soit un nombre pour les nombres (attention, ces nombres peuvent être des flottants),
- soit une chaîne de caractère pour les opérateurs.

```
B(["4", "+", "6.2", "*", "8"])
> [4, "+", 6.2, "*", 8]
```

## Étape 3 - Opérations de base

Pour chaque opérateur, créer une fonction implémentant son opération. Tous les
opérateurs sont ici binaires : les fonctions devront donc prendre deux arguments
et retourner le résultat.

En partant du principe que ces fonctions s'appeleraient `add`, `minux`,
`multiply`, `true_divide`, il nous faudrait donc des fonctions :

```
add(5, 0)
> 5
minus(3, 9)
> -6
multiply(2, 0)
> 0
true_divide(1, 2)
> 0.5

```
## Étapes 4 - Calcul de l'expression

C'est maintenant que le jus de cerveau va commencer à suinter : il faut calculer
enfin notre expression mathématique. Pour cela, deux approches :

- une approche itérative, qui va parcourir les éléments de l'expression pour
  résoudre toutes les opérations prioritaires, puis reparcourir les éléments
  pour résoudre les opérations restantes, jusqu'à ce que le tableau ne
  contiennent plus qu'un élément : le résultat ;
- une approche récursive, qui va parcourir les éléments de l'expression de
  gauche à droite et choisira soit de résoudre l'opération (cas prioritaire),
  soit de s'appeler elle-même sur le reste de l'expression.

Nous allons expliciter ces deux méthodes à partir d'un exemple, ensuite, à
charge à vous d'implémenter celle qui vous convient le mieux !

L'exemple pris sera le suivant :

```
"98 - 6 * 8 * 1.5 + 4 - 1 / 5"
```

Cette chaîne de caractère, passée dans les fonctions `A` et `B` nous produit
la liste :

```
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
```

### Approche itérative

Nous savons que les opérateurs `*` et `/` sont prioritaires sur les autres.

Nous allons donc d'abord les résoudre. Pour cela, nous parcourons les éléments
du tableaux pour les vérifier un à un. Nous stockerons les résultats dans une
nouvelle liste.

- dans le cas où l'élément est un opérateur non prioritaire, nous pouvons l'ajouter
  dans la nouvelle liste sans transformation ;
- dans le cas où l'éléments est un nombre, il peut être ajouté dans la liste ;
- enfin, dans le cas où l'élément est un `*` ou un `/`, il nous faut résoudre
  l'opération : nous pouvons appeler une des fonctions implémentées à l'étape 3
  pour calculer le résultat à partir des nombres précédants et suivant
  l'opérateur. Le résultat sera stockée dans la nouvelle liste.
  Attention : le résultat ne devra cette fois pas être directement ajouté dans
  la nouvelle liste, mais il devra remplacer le dernier élément de la liste,
  puisqu'il a été "consommé" dans l'opération !
  Attention : dans la suite de l'algorithme, il va falloir sauter le prochain élément,
  puisqu'il a également été "consommé" dans l'opération !

Illustration :

```
 v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98]

      v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-"]

          v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 6]

              v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 48] # 6 * 8, on saute alors l'élément 8,
              # au prochain tour on tombera tout de suite sur l'élément "*"

                      v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 72] # 45 * 1.5, on saute alors l'élément 1.5,
              # au prochain tour on tombera tout de suite sur l'élément "+"

                                v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 72, "+", ]

                                    v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 72, "+", 4]

                                        v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 72, "+", "4", "-"]

                                            v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 72, "+", "4", "-", 1]

                                                v
[98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]
[98, "-", 72, "+", "4", "-", 0.2] # 1 / 5 , on saute alors l'élément 1.5,
                                  # au prochain tour on tombera... sur du vide : le tableau est parcouru
```

Les opérateurs prioritaires sont résolus, on peut maintenant calculer le
résultat final en parcourant à nouveau le tableau, et appliquer au fur et à
mesure  les opérations non prioritaires `+` et `-`:

```
 v
[98, "-", 72, "+", "4", "-", 0.2]
98

      v
[98, "-", 72, "+", "4", "-", 0.2]
26 # 98 - 72, on saute le 72 pour arriver au "+" suivant

               v
[98, "-", 72, "+", "4", "-", 0.2]
30 # 26 + 4, on saute le 4 pour arriver au "-" suivant

                         v
[98, "-", 72, "+", "4", "-", 0.2]
29.8 # 30 - 0.2, on saute le 0.2 et on finit le parcours du tableau :
     # nous avons notre résultat !

```

### Approche récursive

La solution itérative est juste et simple, mais assez peu élégante.
Elle est probablement constituée de plusieurs boucles `for`, des indices `i` sur
lesquels on fait parfois des `+1` obscurs, ... bref elle est un peu pataude.

Avec une approche récursive, on va définir une fonction qui ne s'occupera que
d'un petit morceau de l'expression, puis déléguera la résolution du reste de
l'expression... à elle-même. Cet appel (sur une expression plus petite)
résoudra lui-même une petite partie de l'expression, puis se rappelera sur
le reste, et ainsi de suite jusqu'à ce qu'il n'y ait plus de reste : toute
l'expression sera évaluée. Ce sera la condition d'arrêt de la récursion.

Nous ferons dans la suite l'hypothèse que cette fonction récursive sera appelée
`recc`.

En prenant en argument un tableau d'éléments de l'expression (le résultat de
`B`), `recc` a 3 comportements possibles :

- soit elle reçoit en argument un tableau composé d'un seul élément
  (forcément un nombre, sauf bug). Dans ce cas son job est simple : c'est
  simplement de **retourner** ce nombre !
- soit elle reçoi en argument un tableau de plus d'un éléments. Ce tableau sera
  forcément de la forme `[<nombre1> <opérateur> <nombre2> ...]` (`...` étant la
  suite des éléments de l'expression, ou rien dans le cas où l'expression est
  presque terminée).
  Il y a alors deux cas :
  - `<opérateur>` est un opérateur non prioritaire (`+` ou `-`). On **retourne**
    alors la fonction idoine comme défini à l'étape 3 (`add` ou `minus`),
    avec comme arguments `<nombre1>` et `recc(<reste de la liste>)`.
  - `<opérateur>` est un opérateur prioritaire (`*` ou `/`). Il faut alors
    résoudre l'opération immédiatement ! Dans ce cas, nous faisons immédiatement
    l'opération (`multiply` ou `true_divide`) avec les arguments `<nombre1>` et
    `<nombre2>`, puis on **retourne** `recc([<résultat>, ...])` (`...` étant
    comme tout à l'heure le reste de la liste, ou rien).

Voici une illustration de ce comportement :

```
recc([98, "-", 6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5])
# "-" pas prioritaire

minus(98, recc([6, "*", 8, "*", 1.5, "+", 4, "-", 1, "/", 5]))
# "*" prioritaire, on fait multiply(6, 8) et on réinjecte le résultat

minus(98, recc([48, "*", 1.5, "+", 4, "-", 1, "/", 5]))
# "*" prioritaire, on fait multiply(48, 1.5) et on réinjecte le résultat

minus(98, recc([72, "+", 4, "-", 1, "/", 5]))
# "+" pas prioritaire

minus(98, add(72, recc([4, "-", 1, "/", 5])))
# "-" pas prioritaire

minus(98, add(72, minus(4, recc([1, "/", 5])))
# "/" prioritaire, on fait true_divide(1, 5) et on réinjecte le résultat

minus(98, add(72, minus(4, recc([0.2]))))
# plus qu'un seul élément dans la liste, c'est notre condition d'arrêt !
# on retourne directement le nombre

minus(98, add(72, minus(4, 0.2))))
# comme on n'appelle plus recc (fin de la récursivité), tout se dépile d'un coup !

29.8
```
