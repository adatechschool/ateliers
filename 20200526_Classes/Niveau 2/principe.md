## Niveau 2

Vous disposez d'une classe "Animal" décrite ci-dessous : Créer les classes "Chien", "Chat", et "Poulpe" comme suit

```class Animal {
  constructor(nom, age, pattes, espece, status) {
    this.nom = nom;
    this.age = age;
    this.pattes = pattes;
    this.espece = espece;
    this.status = status;
  }
  sePresenter() {
    return `Bonjour, mon nom est ${this.nom} et j'ai  ${this.age} ans.`;
  }
}
```

- Définir une classe Poulpe grâce à la classe animal : un poulpe a toujours 8 "pattes", son espèce est égale à "poulpe"

- Définir une classe Chat grâce à la classe animal : un chat a toujours 4 "pattes", son espèce est égale à "chat". La fonction "se présenter" du chat devrait par contre donner la même phrase que les autres animaux, mais avec "miaou miaou" ajouté à la fin

- Définir une classe Chien grâce à la classe animal : un chien a toujours 4 "pattes", son espèce est égale à "chien". Le chien possède en plus une méthode "accueillirSonMaitre" qui ne prend pas d'argument et qui renvoie "Bonjour" ${this.maitre}
