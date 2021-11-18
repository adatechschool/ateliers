## Calculator

### STEP 1

Designez une page HTML qui prendra la forme d'une calculatrice. 
- Afficher les chiffres de `0` à `9`
- Afficher un bouton `+`

```javascript
<button id="0">0</button>
```

### STEP 2

Afficher le cadrant de la calculatrice, qui affichera le chiffre sélectionné par l'utilisateur.

Hints:

```javascript
<button id="1" onclick="button1clicked()">1</button>
var cadrant = document.getElementById("cadrant");
cadrant.text += "1"
```

### STEP 3

Afficher aussi l'opérateur `+` dans le cadrant lorsqu'il est sélectionné, afin de pouvoir construire une opération.

### STEP 4

Intégrer l'opérateur `=` qui déclanchera le calcule de votre opération et affichera le résultat dans le cadrant.

### STEP 5

Intégrer l'opérateur `-`

### STEP 6

Intégrer les opérateurs `/` et `*`

> Attention, ces opérateurs ont un ordre d'exécution !

Si l'on a un calcul du type `3+3*3` l'opérateur `*` à la priorité !

### STEP 7

On ajoute des parenthèses ?