# 1. Enoncé

L'objectif de cet exercice est de manipuler des données dans une base de donnée et écrire des requêtes pour l'interroger.
Il est recommandé de travailler sur un outil en ligne tel que [sqlfiddle](http://sqlfiddle.com/).

Le principe de la conception et l'architecture d'une base de donnée est d'éviter au maximum la redondance d'informations.

## Etape 1

Commencez par concevoir le schéma d'une base de donnée qui correspond à la stucture Ada Tech School. On va donc identifier les tables représentant les apprenant.e.s et les encadrant.e.s.

## Etape 2

Écrivons quelques requêtes à présent.
Interrogez la base de donnée de manière à recevoir une liste de tous les membres d'Ada. Apprenant.e.s et encadrant.e.s confondues.
Écrire ensuite une requête pour distinguer les apprenant.e.s des encadrant.e.s.

## Etape 3

À présent, nous allons introduire le concept de promotion. Concevez une table pour représenter les promo Ada, n'oubliez pas le nom et l'année de la promo. Trouvez ensuite une manière d'associer un.e apprenant.e.s à une promo.

## Etape 4

Écrire la requête qui retournera une promo complètes, donc, la liste de ses apprenant.e.s.
Les promo ayant une année en plus d'un nom, écrire aussi une requête qui retournera la listes des promo pour une année donnée.
