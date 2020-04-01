L'escargot Parisien

Ecrire une fonction qui reçoive un tableau de n x n caractères et qui renvoie une liste avec ces caractères 
dans l'ordre d'un escargot, de l'extérieur vers l'intérieur, en commencçant par la gauche (un peu comme les arrondissements 
de Paris) : 

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
         
escargot(array) = [1,2,3,6,9,8,7,4,5]

array = [['A','B','C','D'],
         ['E','F','G','H'],
         ['I','J','K','L'],
         ['M','N','O','P']]
         
escargot(array) = ['A','B','C','D','H','L','P','O','N','M','I','E','F','G','K','J']

Les caractères sont lus dans cet ordre : 


------> 

puis 

-------
      |
      |
      |
     \/

puis 

------ 
      |
      |
      |
< ---- 

puis 

------ 
^     |
|     |
|     |
------ 

puis 

------ 
----> |
|     |
|     |
------ 

et ainsi de suite
