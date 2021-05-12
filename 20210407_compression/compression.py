#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Dict, Tuple

TEXT = """généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement sur l'aspect graphique. ce texte a pour autre avantage d'utiliser des mots de longueur variable, essayant de simuler une occupation normale. la méthode simpliste consistant à copier-coller un court texte plusieurs fois ( « ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte ceci est un faux-texte » ) a l'inconvénient de ne pas permettre une juste appréciation typographique du résultat final. il circule des centaines de versions différentes du lorem ipsum, mais ce texte aurait originellement été tiré de l'ouvrage de cicéron, de finibus bonorum et malorum ( liber primus ), texte populaire à cette époque, dont l'une des premières phrases est : « neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... » ( « il n'existe personne qui aime la souffrance pour elle-même, ni qui la recherche ni qui la veuille pour ce qu'elle est... » ). expert en utilisabilité des sites web et des logiciels, jakob nielsen souligne que l'une des limites de l'utilisation du faux-texte dans la conception de sites web est que ce texte n'étant jamais lu, il ne permet pas de vérifier sa lisibilité effective. la lecture à l'écran étant plus difficile, cet aspect est pourtant essentiel. nielsen préconise donc l'utilisation de textes représentatifs plutôt que du lorem ipsum. on peut aussi faire remarquer que les formules conçues avec du faux-texte ont tendance à sous-estimer l'espace nécessaire à une titraille immédiatement intelligible, ce qui oblige les rédactions à formuler ensuite des titres simplificateurs, voire inexacts, pour ne pas dépasser l'espace imparti. contrairement à une idée répandue, le faux-texte ne donne même pas un aperçu réaliste du gris typographique, en particulier dans le cas des textes justifiés : en effet, les mots fictifs employés dans le faux-texte ne faisant évidemment pas partie des dictionnaires des logiciels de pao, les programmes de césure ne peuvent pas effectuer leur travail habituel sur de tels textes. par conséquent, l'interlettrage du faux-texte sera toujours quelque peu supérieur à ce qu'il aurait été avec un texte réel, qui présentera donc un aspect plus sombre et moins lisible que le faux-texte avec lequel le graphiste a effectué ses essais. un vrai texte pose aussi des problèmes de lisibilité spécifiques ( noms propres, numéros de téléphone, retours à la ligne fréquents, composition des citations en italiques, intertitres de plus de deux lignes ... ) qu'on n'observe jamais dans le faux-texte."""

print('Taille du texte non compressé: {} caractères'.format(len(TEXT)))

#-- Step 1 --#

def A(text: str) -> List[str]:
    return text.split()

def B(words: List[str]) -> str:
    return ' '.join(words)

assert B(A(TEXT)) == TEXT

#-- Step 2 --#

COMPRESSION_DICT = {
    'texte': '1',
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
    'avec': '12'
}

def C(words: List[str], compression_dict: Dict[str, str]) -> List[str]:
    result = []
    for word in words:
        if word in compression_dict:
            result.append(compression_dict[word])
        else:
            result.append(word)
    return result

test_list = ['voiture', 'texte', 'faux-texte', 'dans', 'journal', 'lorem']
expected_list = ['voiture', '1', '9', '10', 'journal', '2']

assert C(test_list, COMPRESSION_DICT) == expected_list

COMPRESSED_TEXT = B(C(A(TEXT), COMPRESSION_DICT))
print('Première compression ({} caractères): \n---\n{}\n---' \
      .format(len(COMPRESSED_TEXT), COMPRESSED_TEXT))

#-- Step 3 --#

# Cette syntaxe assez spécifique à Python s'appelle une 'dictionnary comprehension"
# les listes et autres itérables (comme les tuples) permettent des approches
# similaires qui permet de se passer élégamment de boucle for
REVERSE_DICT = { v: k for (k, v) in COMPRESSION_DICT.items() }

assert B(C(A(COMPRESSED_TEXT), REVERSE_DICT)) == TEXT

#-- Step 4 --#

def D(words: List[str]) -> Dict[str, int]:
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

assert D(['ceci', 'est', 'un', 'faux-texte', 'ceci', 'est']) == \
    {'ceci': 2, 'est': 2, 'un': 1, 'faux-texte': 1}

def E(word_occurences: Dict[str, int],
      min_size: int = 3,
      min_occurence: int = 2) -> Dict[str, str]:
    result = {}
    substitution = 1
    for (word, occurence) in word_occurences.items():
        if not len(word) >= min_size:
            continue
        if not occurence >= min_occurence:
            continue
        result[word] = str(substitution)
        substitution += 1
    return result

assert E({'avec': 3, 'tous': 1, 'un': 23, 'nuit': 10}) == \
    {'avec': '1', 'nuit': '2'}

NEW_COMPRESSION_DICT = E(D(A(TEXT)))
print('\nNouveau dictionnaire de substitution (taille min: 3, occurence min: ' \
      '2): \n---\n{}\n---'.format(NEW_COMPRESSION_DICT))

NEW_COMPRESSED_TEXT = B(C(A(TEXT), NEW_COMPRESSION_DICT))
print('Seconde compression ({} caractères): \n---\n{}\n---' \
      .format(len(NEW_COMPRESSED_TEXT), NEW_COMPRESSED_TEXT))

def generate_best_compression() -> Tuple[str, Dict[str, str], int, int]:
    print('\nGénération de dictionnaires de substitution et calcul de ' \
          'compression optimal (taille du dictionnaire comprise)')
    best = None
    # on fait varier la taille minimale des mots ainsi que
    # le nombre d'occurence entre 1 et 6
    for size in range(1, 6):
        for occurence in range(1, 6):
            # on calcule le dictionnaire de substitution selon les contraintes
            compression_dict = E(D(A(TEXT)), min_size=size, min_occurence=occurence)
            # on compresse le texte
            text = B(C(A(TEXT), compression_dict))

            # chaîne de caractère pré-remplie pour faire les prints plus loin
            new_best_text = ' -> Nouveau meilleur résultat trouvé avec mot de ' \
                'taille minimale {} et nombre d\'occurence minimale {}: {} ' \
                'caractères (texte {} caractères + dictionnaire {} caractères)'

            # premier passage: 'best' est vide, on le remplit avec ce qui nous
            # passe sous la main
            if best is None:
                best = (text, compression_dict, size, occurence)
                print(new_best_text.format(size,
                                           occurence,
                                           len(text + str(compression_dict)),
                                           len(text),
                                           len(str(compression_dict))))
            # dans les autres cas on vérifie, et on update 'best'
            # si on trouve mieux
            else:
                # jusqu'à maitenant on n'a considéré que la taille du texte
                # compressé mais un système de compression va également
                # considéré la taille du dictionnaire de substitution,
                # puisqu'il est nécessaire pour décompresser le texte (et devra
                # donc être envoyé avec le texte).
                # Il faut donc également compter la taille du dictionnaire
                # lorsqu'on recherche un optimum
                if len(text + str(compression_dict)) < len(best[0] + str(best[1])):
                    best = (text, compression_dict, size, occurence)
                    print(new_best_text.format(size,
                                               occurence,
                                               len(text + str(compression_dict)),
                                               len(text),
                                               len(str(compression_dict))))
    return best

BEST = generate_best_compression()

print('\n'+'-'*30)
print('Meilleur rapport trouvé: remplacer les mots de taille >= à {} apparaissant au moins {} fois dans le texte'.format(BEST[2], BEST[3]))
print('Dictionnaire utilisé: \n---\n{}\n---'.format(BEST[1]))
print('Meilleure compression ({} caractères): \n---\n{}\n---'.format(len(BEST[0]), BEST[0]))
