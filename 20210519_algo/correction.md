# Exercice individuel

## Algo


## Level 1
Variables N, i, Som en Entier

Debut
Ecrire "Entrez un nombre : "
Lire N Som ← 0
Pour i ← 1 à N Som ← Som + i i Suivant
Ecrire "La somme est : ", Som
Fin

## Level 2
Variable N en Entier

Debut
N ← 0
Ecrire "Entrez un nombre entre 10 et 20"
TantQue N < 10 ou N > 20
Lire N
Si N < 10 Alors Ecrire "Plus grand !" SinonSi N > 20 Alors Ecrire "Plus petit !"
FinSi
FinTantQue
Fin

## Level 3
Voici une solution possible sous Python :

import random

def soiree(n,p):
    c=0
    for i in range(n):
        if (random.random()<p):
            c=c+1
    return c
    
def repetitions(nb):
    succes=0
    for i in range(nb):
        if (soiree(70,0.4)<=30):
            succes=succes+1
    return (succes/nb)
    
La fonction soiree(n,p) simule le déroulement d'une soirée et renvoie le nombre de crèmes brûlées commandées au cours d'une soirée. La fonction repetitions(nb) propose de répéter un grand nombre de soirées. Pour chaque soirée où le nombre de crèmes brûlées commandées est inférieur à 30, on comptabilise un succès. On affiche ensuite la fréquence du nombre de succès. Une exécution de repetitions(10000) donne environ 0,73. Le restaurateur semble avoir raison!
Remarquons qu'il est aussi possible d'avoir une résolution mathématique du problème. Le nombre de crèmes brûlées commandé chaque soir est une variable aléatoire 
X  qui suit une loi binomiale de paramètres 70 et 0.4.

## Level 4
Solution 1: 

Variables N, P, i, Numé, Déno1, Déno2 en Entier

Debut
Ecrire "Entrez le nombre de chevaux partants : "
Lire N
Ecrire "Entrez le nombre de chevaux joués : "
Lire P Numé ← 1
Pour i ← 2 à N Numé ← Numé * i i Suivant
Déno1 ← 1
Pour i ← 2 à N-P Déno1 ← Déno1 * i i Suivant
Déno2 ← 1
Pour i ← 2 à P Déno2 ← Déno2 * i i Suivant
Ecrire "Dans l’ordre, une chance sur ", Numé / Déno1
Ecrire "Dans le désordre, une sur ", Numé / (Déno1 * Déno2)
Fin

Cette version, formellement juste, comporte tout de même deux faiblesses.

La première, et la plus grave, concerne la manière dont elle calcule le résultat final. Celui-ci est le quotient d'un nombre par un autre ; or, ces nombres auront rapidement tendance à être très grands. En calculant, comme on le fait ici, d'abord le numérateur, puis ensuite le dénominateur, on prend le risque de demander à la machine de stocker des nombres trop grands pour qu'elle soit capable de les coder (cf. le préambule). C'est d'autant plus bête que rien ne nous oblige à procéder ainsi : on n'est pas obligé de passer par la division de deux très grands nombres pour obtenir le résultat voulu.

La deuxième remarque est qu'on a programmé ici trois boucles successives. Or, en y regardant bien, on peut voir qu'après simplification de la formule, ces trois boucles comportent le même nombre de tours ! (si vous ne me croyez pas, écrivez un exemple de calcul et biffez les nombres identiques au numérateur et au dénominateur). Ce triple calcul (ces trois boucles) peut donc être ramené(es) à un(e) seul(e). Et voilà le travail, qui est non seulement bien plus court, mais aussi plus performant :

Solution 2:

Variables N, P, i, A, B en Numérique

Debut
Ecrire "Entrez le nombre de chevaux partants : "
Lire N
Ecrire "Entrez le nombre de chevaux joués : "
Lire P A ← 1
B ← 1
Pour i ← 1 à P
A ← A * (i + N - P)
B ← B * i i Suivant
Ecrire "Dans l’ordre, une chance sur ", A
Ecrire "Dans le désordre, une chance sur ", A / B
Fin

