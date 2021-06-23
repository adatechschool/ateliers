# Comparaison de performances de langages

## Introduction

Un élément (mais rarement le seul) qui peut influer le choix d'un langage
informatique est sa performance en temps d'exécution.

Nous allons essayer dans cet exercice d'évaluer ce genre de problématique, puis
de comparer deux langages de programmation différents : un compilé (le `C`), un
autre interprété (le `Python`).

## Étape 1 - Évaluer un temps d'exécution

Écrivez en Python une fonction très simple ; par exemple qui fait la somme de
deux arguments entiers.

Créer maintenant une autre fonction pour calculer le temps d'exécution de votre
première fonction. par exemple, votre code peut avoir la forme :

```
def sum(arg1, arg2):
    return arg1 + arg2

def calculate_time():
    start = <... get_current_time>
    sum(2, 3)
    print("Spent time: " + <... get_current_time> - start)
```

Le but est de pouvoir calculer précisément le temps pris par votre fonction.
**Précisément** car il est probable que le temps d'exécution ne soit que de
quelques millisecondes voir microsecondes. Un temps en secondes est donc trop
grossier. Il faudra donc se renseigner, langage par langage, sur le (les ?)
moyen(s) de calculer un temps avec une bonne précision.

## Étape 2 - Fonction lente

Développez maintenant une fonction délibérément complexe, qui va produire
beaucoup de calculs. Le résultat de cette fonction n'a aucun intérêt, il s'agit
simplement de forcer le code à durer un peu plus longtemps.

Par exemple, on peut choisir, à partir d'un entier `N`, de calculer le produit
de chaque entier de 1 jusqu'à `N` avec tous les entiers de 1 jusqu'à `N` :

```
def complex():
    N = 2345
    for i in range(N):
        for j in range(N):
            storage = i * j
```

Remplacer la première fonction très simple développée à l'étape 1 par votre
nouvelle fonction, et modifier la valeur de `number` pour avoir une durée
d'exécution qui soit de l'ordre de quelques secondes (2-3, pas besoin de plus).

## Étape 3 - Équivalent en `C`

Développer maintenant **le même** algorithme en `C`, en utilisant la même
valeur de `number`.

Comparez les résultats. Vous devriez avoir une différence très nette.

## Étape 4 - Autres langages

Essayez d'autres langages : `PHP`, `JavaScript`, ... Vous pourriez être surpris
des résultats, notamment pour ce dernier langage.