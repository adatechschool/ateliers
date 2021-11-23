Pour cet exercice, le choix du langage est libre. Il va s'agir de manipuler des chaines de caractères représentant des dates.
### Niveau 1:
Créer une fonction `isValidDate` qui prend en paramètre une date en string et determine si elle est valide.
Pour qu'une date soit valide, il faut qu'elle existe et qu'elle soit au format dd/mm/aaaa.

### Niveau 2:
Créer une fonction `isPalindrome` qui prend une date en string en paramètre et retourne un booleen qui indique si la date est un palindrome. Si la date est invalide, retourner false. (Exemple de dates palindromes = qui se lit dans les deux sens)

### Niveau 3:
Créer une fonction `getNextPalindromes` qui donne les `x` prochaines dates palindromes à compter d’aujourd’hui. La fonction prend le `x` en paramètre.

#### Exemple d’usage :
Niveau 1

    isValidDate("03/04/2001") // true
    isValidDate("03/14/2001") // false

Niveau 2

    isPalindrome("11/02/2011") // true
    isPalindrome("03/04/2001") // false

Niveau 3

    getNextPalindromes(8)
    22/02/2022
    03/02/2030
    13/02/2031
    23/02/2032
    04/02/2040
    14/02/2041
    24/02/2042
    05/02/2050
