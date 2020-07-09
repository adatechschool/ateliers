function decoder (chaine) {
  resultat = ""

  for (let car of chaine) {
    switch (car) {
      case '1':
        car = 'I'
        break
      case '0':
        car = 'O'
        break
      case '5':
        car = 'S'
        break
      default:
        break
    }

    resultat += car
  }

  return resultat
}

console.log ("Une chaine de caractères SVP ?")
quoi = readline()

console.log (decoder(quoi))

