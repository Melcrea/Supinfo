import string
import unicodedata
import os

def clear():
    os.system("cls")

def keyOK(n, offset):
    return offset >= 0 and offset <= 2*n-3

def computeCoordinates(n, l, offset):
    coordinates = []
    row = 0
    isRising = False
    if offset > n-1:
        offset = (n-1)-(offset-(n-1))
        isRising = True
    for column in range(l):
        coordinates.append((row+offset, column))
        if isRising == False:
            if row+offset < n-1:
                row += 1
            else:
                isRising = True
        if isRising == True:
            if row+offset > 0:
                row -= 1
            if row+offset == 0:
                isRising = False
    return coordinates

def init(n, l, coordinates):
    dictionary = {}
    for pos in coordinates:
        dictionary[pos] = None
    return dictionary

def fullDictionaryCipher(text, l, coordinates, dictionary):
    for j in range(l):
        dictionary[coordinates[j]] = text[j]

def fullDictionaryDecipher(text, n, l, coordinates, dictionary):
    cursor = 0
    for i in range(n):
        for j in range(l):
            if (i, j) in dictionary:
                dictionary[(i, j)] = text[cursor]
                cursor += 1

def fullDictionary(text, n, l, coordinates, dictionary, cipher):
    if cipher:
        fullDictionaryCipher(text, l, coordinates, dictionary)
    else:
        fullDictionaryDecipher(text, n, l, coordinates, dictionary)

def dictionaryToStringCipher(n, l, coordinates, dictionary):
    text = []
    for i in range(n):
        for j in range(l):
            if (i, j) in dictionary:
                text.append(dictionary[(i, j)])
    return "".join(text)

def dictionaryToStringDecipher(n, l, coordinates, dictionary):
    text = []
    for j in range(l):
        text.append(dictionary[coordinates[j]])
    return "".join(text)

def dictionaryToString(n, l, coordinates, dictionary, cipher):
    if cipher:
        return dictionaryToStringCipher(n, l, coordinates, dictionary)
    else:
        return dictionaryToStringDecipher(n, l, coordinates, dictionary)

def displayDictionary(n, l, coordinates, dictionary):
    for i in range(n):
        for j in range(l):
            if (i, j) in dictionary:
                print(dictionary[(i, j)], end='')
            else:
                print(" ", end='')
        print("")

def algorithm2(text, n, offset, cipher, display):
    if keyOK(n, offset):
        l = len(text)
        coordinates = computeCoordinates(n, l, offset)
        dictionary = init(n, l, coordinates)
        fullDictionary(text, n, l, coordinates, dictionary, cipher)
        if display:
            print("\n[?] Affichage de la vague\n")
            displayDictionary(n, l, coordinates, dictionary)
        if cipher:
            print("\n[?] Message chiffré\n")
        else:
            print("\n[?] Message déchiffré\n")
        print(dictionaryToString(n, l, coordinates, dictionary, cipher))
    else:
        print("Erreur - 'n' et 'offset' sont incompatibles")
    input()

def convert_letter(text): 
    punctuations = string.punctuation
    alphabet = string.ascii_uppercase[:26]
    valid_string = "" 

    text = text.upper()
    normal = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
    end = normal.decode('utf-8')

    for elem in end:
        if elem in alphabet and elem not in punctuations: 
            valid_string += elem
            
    return valid_string

modeChoice = -1
crypChoice = -1
displayChoice = -1
n = -1
offset = -1

while modeChoice < 1 or modeChoice > 2:
    clear()
    print("*** Algorithme 2 ***\n")
    print("Selectionnez un preset: ")
    print("\t1) Mode saisi manuel")
    print("\t2) Exemple question 3.2")
    modeChoice = int(input("\nTapez votre choix: "))

if modeChoice == 1:
    while crypChoice < 1 or crypChoice > 2:
        clear()
        print("*** Algorithme 2 ***\n")
        print("- Preset: manuel\n")
        print("Sélectionnez un mode d'excution: ")
        print("\t1) Chiffrement")
        print("\t2) Déchiffrement")
        crypChoice = int(input("\nTapez votre choix: "))
    
    clear()
    print("*** Algorithme 2 ***\n")
    print("- Preset: manuel")
    if crypChoice == 1:
        print("- Excution: chiffrement\n")
    else:
        print("- Excution: déchiffrement\n")
    text = input("Tapez un texte: ")
    text = convert_letter(text)

    while displayChoice < 1 or displayChoice > 2:
        clear()
        print("*** Algorithme 2 ***\n")
        print("- Preset: manuel")
        if crypChoice == 1:
            print("- Excution: chiffrement\n")
        else:
            print("- Excution: déchiffrement\n")
        print("Sélectionnez un mode d'affichage: ")
        print("\t1) Afficher")
        print("\t2) Masquer")
        displayChoice = int(input("\nTapez votre choix: "))
    
    while not keyOK(n, offset):
        clear()
        print("*** Algorithme 2 ***\n")
        print("- Preset: manuel")
        if crypChoice == 1:
            print("- Excution: chiffrement")
        else:
            print("- Excution: déchiffrement")
        if displayChoice == 1:
            print("- Display: affiché\n")
        else:
            print("- Display: masqué\n")
        n = int(input("n: "))
        offset = int(input("offset: "))
    algorithm2(text, n, offset, crypChoice == 1, displayChoice == 1)

if modeChoice == 2:
    text = "HANHARYMTPTLAYNCIPSITTITNOWRIOEFHOAEALOWIDIIGTNOSATTNSDOATNSSOEGSHLEFTTAMTODAGGITHSGTIDYTGEETSSSTETMOILJINNWGSNIEEISNAISTKNUELIYSYENNAUAAEILGYLTMUGNMUOASOGRNBTENMGNSWFIRBAJIJMEIGHIOTR"
    print("\n[?] Texte à déchiffrer :\n")
    print(text)
    algorithm2(text, 7, 8, False, True)