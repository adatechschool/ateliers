Ecrire une fonction qui sache décoder du Morse : les courts bips seront indiqués par des points (.) et les longs
bips seront indiqués par des tirets (-). Chaque lettre doit être espacée de la suivante par un espace, et chaque mot 
doit être espacé du suivant par trois espaces. Se limiter aux lettres de l'alphabet et aux chiffres de 0 à 9

decoder("... --- ...") = "sos"
decoder("-... --- -. .--- --- ..- .-.") = "bonjour"

Voici l'alphabet morse :

a .-      h ....    o ---     u ..-      1 .----     6 -....
b -...    i ..      p .--.    v ...-     2 ..---     7 --...
c -.-.    j .---    q --.-    w .--      3 ...--     8 ---..
d -..     k -.-     r .-.     x -..-     4 ....-     9 ----.
e .       l .-..    s ...     y -.--     5 .....     0 -----
f ..-.    m --      t -       z --..
g --.     n -.
