# Exercice individuel : SQL basics

## Installation initiale

1. Connectez vous à une interface Mysql pour pouvoir y exécuter des requêtes Mysql, par exemple `PHPMyadmin`.
2. Téléchargez le fichier de données de test "villes de France" : https://github.com/farnoux/ateliers/blob/patch-1/20210526_SQL_Basics/villes_france.sql.
3. Importer ce fichier au sein de Mysql.
4. Vous devriez désormais observer qu'une nouvelle table `villes_france_free` a été créée.


## Level 1

Écrivez une requête SQL permettant de récupérer :

- la liste des villes dont le nom commence par "Saint".

Vous devriez récolter 4260 résultats.

## Level 2

Écrivez une requête SQL permettant de récupérer : 

- uniquement les champs "ville_nom_simple", "ville_population_2012", "ville_code_postal", "ville_surface"
- dans la limite des 10 premières entrées

## Level 3

Écrivez une requête SQL permettant de récupérer :

- les 10 villes les plus peuplées en 2012

Le résultat doit s'apparenter à ce tableau : 

<img width="329" alt="Screenshot 2021-05-25 at 18 57 41" src="https://user-images.githubusercontent.com/98240/119538208-2abc0100-bd8b-11eb-8d50-48eb2537a569.png">

## Level 4

Écrivez une requête SQL permettant de récupérer :

- le nombre de villes rattachées à un département
- avec les départements ayant le moins de villes en premier
- dans la limite de 20

Le résultat doit s'apparenter à ce tableau : 

<img width="235" alt="Screenshot 2021-05-25 at 19 07 24" src="https://user-images.githubusercontent.com/98240/119539452-7c18c000-bd8c-11eb-9232-56bce2fbfc5e.png">


## Level 5

Écrivez une requête SQL permettant de :

- ajouter 3 millions dhabitants à la ville de votre choix pour l'annnée 2012

