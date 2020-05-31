# Les pointeurs

## Outils

Si vous ne disposez pas d'une installation C++ fonctionnelle, vous pouvez utiliser
des compilateurs en ligne existants tels que [OnlineGDB](https://www.onlinegdb.com/online_c++_compiler).

Pour faire de la visualisation de l'execution de votre code, vous pouvez utiliser des outils tels que [pythontutor](
http://pythontutor.com/visualize.html#mode=display)

## Petite introduction

Imaginons la mémoire de notre ordinateur comme un grand tableau [d'octets](https://fr.wikipedia.org/wiki/Byte).
Chaque variable que nous instancions prend un peu de place dans ce grand tableau.
Prenons comme exemple une variable `nombre_de_mots` de type `Int`.
`nombre_de_mots` a une position dans notre mémoire. Nous appelons ça son adresse.
C'est l'index du premier octet utilisé dans la mémoire de l'ordinateur pour stocker notre variable.

L'adresse de la variable `nombre_de_mots` peut etre utilisée pour référencer notre variable dans du code.

Une variable représentant un pointeur de `nombre_de_mots` va stocker l'adresse de `nombre_de_mots`.

L'adresse de `nombre_de_mots` est récupérable en utilisant l'opérateur `&`: `&nombre_de_mots`.
L'adresse de `nombre_de_mots` peut etre stockée dans un pointeur de type `Int*`.
La valeur pointée par un pointeur peut etre obtenue en utilisant l'opérateur `*`: `*pointeur`.

##
