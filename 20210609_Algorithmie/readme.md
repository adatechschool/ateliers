# L'algorithme du sapin 🌲🎄

Ecrivez une fonction `sapin()` dans le langage de votre choix, qui prend en entrée un nombre entier et qui affiche un sapin, avec la logique suivante :

## Niveau 1

`sapin(1)` affiche à l'écran :
```
  +
 /*\
/***\
```

`sapin(2)` affiche à l'écran :
```
   +
  /*\
 /***\
/*****\
```

`sapin(5)` affiche à l'écran :
```
      + 
     /*\
    /***\
   /*****\
  /*******\
 /*********\
/***********\
```

## Niveau 2

`sapin(1)` affiche à l'écran :
```
  +
 /*\
/***\
```

`sapin(2)` affiche à l'écran :
```
   + 
  /*\
 /***\
/*****\
```

`sapin(5)` affiche à l'écran :
```
      + 
     /*\
    /***\
   /*****\
   /*****\
  /*******\
 /*********\
```

`sapin(7)` affiche à l'écran :
```
      + 
     /*\
    /***\
   /*****\
   /*****\
  /*******\
 /*********\
  /*******\
 /*********\
```

## Niveau 3

`sapin(1)` affiche à l'écran :
```
  +
 /*\
/***\
  #
```

`sapin(2)` affiche à l'écran :
```
   + 
  /*\
 /***\
/*****\
   #  
```

`sapin(5)` affiche à l'écran :
```
      + 
     /*\
    /***\
   /*****\
   /*****\
  /*******\
 /*********\
     ##
     ##
```

`sapin(7)` affiche à l'écran :
```
      + 
     /*\
    /***\
   /*****\
   /*****\
  /*******\
 /*********\
  /*******\
 /*********\
     ##
     ##
     ##
```

## Niveau 4 

Même principe que le niveau 3 mais avec des décorations (`o` et `+`) ajoutées aléatoirement (vous choisissez la fréquence), de façon à ne jamais être totalement sur le bord du sapin.

`sapin(1)` affiche à l'écran :
```
  +
 /*\
/*o*\
  #
```

`sapin(2)` affiche à l'écran :
```
   + 
  /*\
 /*o*\
/*o***\
   #  
```

`sapin(5)` affiche à l'écran :
```
      + 
     /*\
    /***\
   /***o*\
   /***+*\
  /*o***+*\
 /**+***o**\
     ##
     ##
```

`sapin(7)` affiche à l'écran :
```
      + 
     /*\
    /*o*\
   /**+**\
   /*o***\
  /***+***\
 /**+***o**\
  /*****+*\
 /**o****+*\
     ##
     ##
     ##
```

## Niveau 5 

Faites en sorte de demander à l'utilisateur/trice le nombre d'étages qu'il/elle veut sur son sapin (par exemple en mode console).

## Niveau 6 

Faites en sorte que l'utilisateur/trice puisse demander plusieurs arbres d'affilée jusqu'à choisir une option pour quitter.

## Niveau 7 

Faites en sorte que la console s'efface entre chaque arbre.

## Niveau 8 

Animer l'arbre ! 

Par exemple, effacer la console toutes les 500 millisecondes et dessiner l'arbre au même endroit, avec les décorations fixes (`o`) qui n'auront pas bougé et les lumières (`+`) placées aléatoirement pour un effet de clignotement.
 
## Niveau bonus

Modifer le paramétrage de votre console pour que l'arbre ait les bonnes couleurs !
 

