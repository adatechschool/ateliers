Ecrire une fonction qui sache décoder du Morse : les courts bips seront indiqués par des points (.) et les longs
bips seront indiqués par des tirets (-). Chaque lettre doit être espacée de la suivante par un espace, et chaque mot 
doit être espacé du suivant par trois espaces. Se limiter aux lettres de l'alphabet et aux chiffres de 0 à 9

decoder("... --- ...") = "sos"
decoder("-... --- -. .--- --- ..- .-.") = "bonjour"

Voici l'alphabet morse :

```
a .-                        
b -...                       
c -.-.                      
d -..                     
e .                         
f ..-.             
g --.
h ....
i .. 
j .---
k -.- 
l .-..
m --  
n -.
o ---
p .--.
q --.-
r .-. 
s ...
t - 
u ..- 
v ...-
w .-- 
x -..- 
y -.--
z --..

1 .---- 
2 ..---
3 ...--
4 ....- 
5 ..... 
6 -....
7 --...
8 ---..
9 ----.
0 -----
```
