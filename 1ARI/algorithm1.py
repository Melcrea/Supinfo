from random import randint

def convertLetters(text):
    for letter in text:
        if not letter.isalpha():
            text = text.replace(letter, "")
    text = text.upper()
    return text

def generateKey():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = []
    for i in range(len(alphabet)):
        randLetter = alphabet[randint(0, len(alphabet)-1)]
        key.append(randLetter)
        alphabet.remove(randLetter)
    return "".join(key)

def keyOK(key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterFound = []
    for item in key:
        if item.isalpha() and not item in letterFound:
            letterFound.append(item)
        else:
            return False
    return True
        
def shiftLeft(keyLeft, i):
    listKey = list(keyLeft)
    #print(listKey)
    letter = listKey[i]
    listKey.remove(letter)
    #print(listKey)
    listKey.insert(13, letter)
    #print(listKey)

def shiftRight(keyRight, i):
    listKey = list(keyRight)
    #print(listKey)
    letter = listKey[i]
    listKey.remove(letter)
    #print(listKey)
    listKey.insert(13, letter)
    #print(listKey)

def algorithm1(text, keyLeft, keyRight, cipher):
    if keyOK(keyLeft) and keyOK(keyRight):
        codedText = []
        for letter in text:
            indexLetter = keyRight.find(letter)
            codedText.append(keyLeft[indexLetter])
            shiftRight(keyRight, indexLetter)
            shiftLeft(keyLeft, indexLetter)
        print(codedText)

algorithm1(convertLetters("SWAY"), "OAJTFYLQXCMPEDNVSBRUKHGWIZ", "EWKFTYIQXUHPMABCNJRLDZSGVO", 1)
