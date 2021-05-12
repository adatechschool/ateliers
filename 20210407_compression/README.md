# Compression de texte

## Introduction

Cet exercice traite de la compression, qui est un procédé permettant de représenter une certaine quantité d'information en utilisant et en occupant un espace plus petit qu'originellement.

Il existe plusieurs type de compression, dans cet exercice nous nous intéresserons à la compression :

- **sans perte**, c'est à dire que le résultat final ne sera pas dégradé par rapport à l'information originelle ;
- **par dictionnaire**, c'est à dire que nous gagnerons de la place en remplaçant certaines bribes d'information par une référence plus courte.
  Nous stockerons cette référence et la bribe associée dans un dictionnaire, afin de nous permettre de reconstruire l'information originelle lors d'une étape de décompression.

Nous nous baserons sur le texte d'exemple suivant :

----

généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement sur l'aspect graphique. ce texte a pour autre avantage d'utiliser des mots de longueur variable, essayant de simuler une occupation normale. la méthode simpliste consistant à copier-coller un court texte plusieurs fois ( « ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte » ) a l'inconvénient de ne pas permettre une juste appréciation typographique du résultat final. il circule des centaines de versions différentes du lorem ipsum, mais ce texte aurait originellement été tiré de l'ouvrage de cicéron, de finibus bonorum et malorum ( liber primus ), texte populaire à cette époque, dont l'une des premières phrases est : « neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... » ( « il n'existe personne qui aime la souffrance pour elle-même, ni qui la recherche ni qui la veuille pour ce qu'elle est... » ). expert en utilisabilité des sites web et des logiciels, jakob nielsen souligne que l'une des limites de l'utilisation du faux-texte dans la conception de sites web est que ce texte n'étant jamais lu, il ne permet pas de vérifier sa lisibilité effective. la lecture à l'écran étant plus difficile, cet aspect est pourtant essentiel. nielsen préconise donc l'utilisation de textes représentatifs plutôt que du lorem ipsum. on peut aussi faire remarquer que les formules conçues avec du faux-texte ont tendance à sous-estimer l'espace nécessaire à une titraille immédiatement intelligible, ce qui oblige les rédactions à formuler ensuite des titres simplificateurs, voire inexacts, pour ne pas dépasser l'espace imparti. contrairement à une idée répandue, le faux-texte ne donne même pas un aperçu réaliste du gris typographique, en particulier dans le cas des textes justifiés : en effet, les mots fictifs employés dans le faux-texte ne faisant évidemment pas partie des dictionnaires des logiciels de pao, les programmes de césure ne peuvent pas effectuer leur travail habituel sur de tels textes. par conséquent, l'interlettrage du faux-texte sera toujours quelque peu supérieur à ce qu'il aurait été avec un texte réel, qui présentera donc un aspect plus sombre et moins lisible que le faux-texte avec lequel le graphiste a effectué ses essais. un vrai texte pose aussi des problèmes de lisibilité spécifiques ( noms propres, numéros de téléphone, retours à la ligne fréquents, composition des citations en italiques, intertitres de plus de deux lignes ... ) qu'on n'observe jamais dans le faux-texte.

----


## Étape 1 - Découper et reconstruire le texte

### Découpage

Nous allons tout d'abord transformer le texte pour le rendre plus facilement manipulable.

Créez une fonction `A` (donnez-lui le nom que vous voulez, c'est simplement pour y faire référence dans cet exercice) prenant en paramètre ce texte (ou tout autre chaîne de caractères) et retourne une liste de mots.

Nous définissons un mot comme un ensemble de caractères, quels qu'ils soient, à l'exception des espaces, qui séparent les mots entre eux.
Par exemple, pour le texte suivant :

```
----
qu'elle est... » ). expert en utilisabilité des
----
```

... la liste des mots est : `['qu'elle', 'est...', '»', ').', 'expert', 'en', 'utilisabilité', 'des']`.

Il est possible d'utiliser la fonction `split`, présente dans de nombreux langages (souvent sous forme de méthode du type `String`), ou tout autre équivalent.

### Reconstruction

Créez également une fonction `B` prenant en paramètre une liste de mots, et retournant une chaîne de charactère composée de l'ensemble des mots dans l'ordre, séparés par un espace.

Cette fonction est "l'inverse" de la fonction `A` créée à l'étape **Découpage** : actuellement, sans aucune modification des mots, elle vous permet de reformer le texte originel à partir du résultat de la fonction `A`.


## Étape 2 - Compression avec dictionnaire fixe

Nous allons maintenant remplacer certains mots du texte par des références.

Nous utiliserons le dictionnaire suivant :

```
{'texte': '1',
 'lorem': '2',
 'qui': '3',
 'donc': '4',
 'est': '5',
 'que': '6',
 'pour': '7',
 'ceci': '8',
 'faux-texte': '9',
 'dans': '10',
 'plus': '11',
 'avec': '12'}
```

Créez une fonction `C` prennant en paramètre une liste de mots et un dictionnaire.

Pour chaque mot dans la liste, si le mot existe dans le dictionnaire en tant que clef, remplacez-le par la valeur associée.

Par exemple, avec le dictionnaire précédent et la liste `['mais', 'ceci', 'est', 'un', 'long', 'faux-texte']`, la fonction doit retourner `['mais', '8', '5', 'un', 'long', '9']`.

Vous pouvez maintenant enchaîner vos fonctions `A`, `C` et `B` pour produire un nouveau texte :

- `A` divise le texte originel en liste de mots,
- `C` remplace certains de ces mots par les références du dictionnaire,
- `B` récupère la liste de mots et reconstruit un texte complet.

Vous venez de compresser le texte !


## Étape 3 - Décompression

Le texte produit à l'étape 3 est certe plus court, mais il n'est pas lisible en l'état. Il faut donc passer par une étape de décompression : remplacer les références par les mots originels.

C'est le but de cette étape.

On peut penser intuitivement que l'étape de substitution des références par les mots originels est très proche de ce que faisait la fonction `C`, et c'est vrai !

À un détail près, qui est que maintenant les mots que nous cherchons dans le texte ne sont plus les clefs du dictionnaire, mais ses valeurs.

Pour résoudre ce détail, il y a une possibilité simple : "inverser" le dictionnaire, par exemple transformer `{'texte': '1', 'lorem': '2'}` en `{'1': 'texte', '2': 'lorem'}`. Dans ce cas, la fonction `C` peut être utilisée directement : il suffit de changer le dictionnaire passé en argument.

Il est bien évidemment possible d'y arriver en ne gardant qu'un seul dictionnaire.

Dans tous les cas, vous avez maintenant un ensemble de fonction vous permettant de compresser et décompresser le texte.

Prenez un peu de temps pour analyser le gain de place de votre compression. Vous pouvez également ajouter ou enlever des mots de votre dictionnaire pour évaluer leurs impacts.


## Étape 4 - Un meilleur dictionnaire

Le dictionnaire proposé est loin d'être complet, et même s'il l'était, peut-être ne serait-il pas adapté à tous les textes.

Nous allons donc faire une fonction pour générer notre propre dictionnaire.

Créez une fonction `D` qui prend en paramètre une liste de mots, et retourne un dictionnaire dont les clefs sont les mots du texte, et les valeurs leur nombre d'apparition.

Par exemple, avec la liste `['ceci', 'est', 'un', 'faux-texte', 'ceci', 'est']`, la fonction retournera : `{'ceci': 2, 'est': 2, 'un': 1, 'faux-texte': 1}`.

Cette fonction vous permet de voir quels mots apparaissent le plus souvent dans le texte, et s'il est efficace de les remplacer par une référence : par exemple, remplacer le mot `'un'` par la référence `'254'` n'entraîne pas de gain de place, mais au contraire une perte !

À partir de vos observations, construisez un dictionnaire plus riche que celui proposé en exemple, tester votre compression / décompression et regardez le gain de place.

Il vous est également possible de générer automatiquement un dictionnaire de références à partir des contraintes de votre choix, par exemple *"je ne veux remplacer que les mots de plus de 3 caractères qui apparaissent au moins 2 fois"*.

Il vous faut pour cela une fonction `E` qui prend en paramètre un dictionnaire de nombre d'apparition des mots, et qui retourne un dictionnaire de référence.

Par exemple, si vous ne voulez que substituer les mots de plus de 3 caractères qui apparaissent au moins 2 fois, avec l'argument `{'avec': 3, 'tous': 1, 'un': 23, 'nuit': 10}`, la fonction retournera : `{'avec': '1', 'nuit': '2'}`.

Vous pouvez donc, à partir de ces contraintes, filtrer le dictionnaire produit par votre fonction `D`, puis associer à chacun des mots conservés une référence unique

Lorsque vous avez cette fonction, vous aurez un code de compression adaptatif au texte compressé :

- `A` divise le texte originel en liste de mots,
- `D` analyse cette liste de mot pour construire un dictionnaire du nombre d'apparition des mots,
- `E` utilise ce dictionnaire pour produire un dictionnaire de références,
- `C` remplace certains de ces mots par les références du dictionnaire de références produit par `E`,
- `B` récupère la liste de mots et reconstruit un texte compressé complet.

À partir de ça, essayer de changer les contraintes de génération de votre dictionnaire de référence, pour trouver les paramètres les plus efficaces !

## Étape 5 - ...

Essayez votre code de compression sur d'autres textes. Attention : jusqu'à présent, un certain nombre de subtilités n'étaient pas traitées, car le texte était simplifié :

- absence de saut de ligne,
- absence de majuscule,
- absence de nombre (qui rentrent en colision avec les références utilisées dans le dictionnaire de compression),
- espaces ajoutés autour de certains caractère (comme autour des parenthèses `(`, `)`),
- ...