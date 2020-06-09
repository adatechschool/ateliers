# Les pointeurs

Cet atelier peut aussi bien se faire en plénière dirigée par l'encadrante qu'en atelier.

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

Une variable représentant un pointeur sur `nombre_de_mots` va stocker l'adresse de `nombre_de_mots`.

L'adresse de `nombre_de_mots` est récupérable en utilisant l'opérateur `&`: `&nombre_de_mots`.
L'adresse de `nombre_de_mots` peut etre stockée dans un pointeur de type `Int*`.
La valeur pointée par un pointeur peut etre obtenue en utilisant l'opérateur `*`: `*pointeur`.

## Mettons les mains dans le cambouis

### Manipulons quelques variables

Imaginons le code suivant:

```
#include <iostream>
using namespace std;

int main ()
{
  char variable_1 = 'a';
  char variable_2 = 'b';
  char* mon_pointeur = nullptr;

  mon_pointeur = &variable_1;
  *mon_pointeur = 'c';

  mon_pointeur = &variable_2;
  *mon_pointeur = 'd';

  cout << "variable_1 a pour valeur " << variable_1 << '\n';
  cout << "variable_2 a pour valeur " << variable_2 << '\n';

  return 0;
}
```

Utilisez ce code dans [pythontutor](http://pythontutor.com/visualize.html#mode=display) pour voir comment se déroule le programme et comment se comportent les variables conjointement avec le pointeur.

### Manipulons des pointeurs dans une fonction

#### Construction de la fonction

Construisez une fonction prenant deux entiers en paramètres et qui multiplie chacun de ces paramètres par 5. Puis affichez dans le `main` de votre fichier les deux nombres entiers qui ont été passés en paramètres à la fonction.

En voici le [prototype](https://fr.wikibooks.org/wiki/Programmation_C%2B%2B/Les_fonctions#Prototype_d'une_fonction):
```
void multiplier_par_5(int premier_nombre, int second_nombre);
```

Que constatez-vous ?

#### Mise en place des pointeurs

Nous voudrions maintenant qu'à l'affichage des deux variables, celles ci aient
la valeur générée dans notre fonction.

Que pensez-vous qu'il faille changer dans le prototype de la fonction pour que cela fonctionne ?
Et dans le corps de la fonction ?

PS: n'oubliez pas, vous pouvez vous aider de [pythontutor](http://pythontutor.com/visualize.html#mode=display) pour visualiser l'execution de votre code.
