## Niveau 3

### Titres et principes

Coder la classe cuisinier avec les principes ci-dessous :

- Un cuisinier commence au niveau 1 et peur progresser jusqu'au niveau 100.

- Les cuisiniers ont tous un titre qui augmente progressivement : "plongeur", "garde-manger","aide cuisinier","commis", "cuistot", "chef de partie", "sous chef", "chef de cuisine", "MOF","chef étoilé", "champion du monde de cuisine"

- Les cuisiniers participent à des concours deux à deux.

- A chaque concours gagné, le cuisinier gagne de l'expérience (selon l'expérience de son adversaire et sa propre expérience, voir plus bas)

- Un cuisinier commence avec une expérience de 100, et à chaque fois qu'il gagne 100 points d'expérience, il passe un niveau. Cette expérience ne se perd pas (ne se remet jamais à zéro). Une fois qu'elle a atteint 10000, l'expérience cesse d'augmenter.

- Tous les 10 niveaux, le cuisinier change de titre : des niveaux 1 à 9, il a le titre de "plongeur", de 10 à 19 "garde-manger", etc.

```
julien_cadiou = Cuisinier()
julien_cadiou.niveau         # => 1
julien_cadiou.experience    # => 100
julien_cadiou.titre          # => "Commis"
```


### Concours et expérience

- Faire un concours contre un cuisinier du même rang accorde 10 points d'expérience

- Faire un concours contre un cuisinier du rang inférieur accorde 5 points d'expérience

- Faire un concours contre un cuisinier deux rangs (ou plus) inférieur accorde 0 points d'expérience

- Faire un concours contre un cuisinier de niveau supérieur accorde plus de points d'expérience : s'il y a N niveaux entre lui et vous, vous gagnez NxNx20 points d'expérience

- On ne peut pas se lancer dans un concours face à un cuisinier qui a plus de 5 niveaux de plus que soi : dans ce cas, il n'y a pas de gain d'expérience et on répond "je m'incline"

- Chaque concours se conclut par l'affichage d'une phrase qui résume le concours : s'il y a 2 niveaux de différence ou plus entre vos cuisiniers, la phrase est "Une victoire facile", s'il y a un niveau entre les deux cuisiniers, la phrase est "Un beau concours", si les deux sont du même niveau, la phrase est "Un très beau concours".

```
julien_cadiou.experience    # => 100
julien_cadiou.titre          # => "Commis"
julien_cadiou.concours(1);     // => "Un très beau concours"
julien_cadiou.experience    # => 110
```

## Entrainement et services

- En plus des concours, un cuisinier peut gagner de l'expérience en participant à des services : un service est défini par une phrase de description, le nombre de points d'expérience qu'il permet de gagner et le niveau minimum requis pour participer au service.

- Si le cuisinier a bien le niveau requis pour un service, il reçoit les points d'expérience associés et la phrase de description est stockée dans son CV. Le programme devrait afficher cette phrase comme retour

- Si le cuisinier n'a pas le niveau requis, on devrait lui renvoyer "Merci mais non merci"

```
philippe_conticini.service(["A lancé la patisserie des reves", 9000, 1]) # => "A lancé la patisserie des reves"
philippe_conticini.experience    # => 9100
philippe_conticini.level         # => 91
philippe_conticini.titre          # => "Chef étoilé"
philippe_conticini.experience    # => 9105
philippe_conticini.CV    # => ["A lancé la patisserie des reves"]
```
