import random

def askUserNumber(message):
    nbr = ""
    while not nbr.isdigit(): #Vérifie si c'est bien un nombre et pas un mot
        nbr = str(input(message))
    return int(nbr)

def defineParamGame():
    n = -1
    p = -1
    player = -1
    while not n >= 2: #On boucle jusqu'à obtenir un nombre entier positif
        n = askUserNumber("How many squares (min 2): ") #On interroge l'utilisateur
    while not p >= 1:
        p = askUserNumber("Maximum amount of pawn per box (min 1): ")
    while not player >= 2:
        player = askUserNumber("How many player (min 2): ")
    return n, p, player

def newBoard(n, p):
    #On génére le tableau avec un  nombre de pièces par case compris entre 0 et p
    return [random.randint(0, p) for i in range(n)]

def displayBoard(board, n):
    for i in range(n): #On affiche toutes les pièces composant le tableau
        print(board[i], end=" | ")
    print("\n")
    for i in range(n): #Puis on affiche le numéro correspondant de chaque case
        print(i + 1, end=" | ")
    print("\n")

def possibleSquare(board, n, i):
    #Si la boucle n'a jamais fait un tour, on retourne false, pour l'obliger à tenir
    #compte du choix de l'utilisateur
    if i is None: 
        return False
    #Si i n'est pas compris dans le tableau, on retourne false
    if i > 0 and i < n:
        #On vérifie qu'il y a au moins un pion sur la case
        if board[i] > 0:
            return True 
    return False

def selectSquare(board, n):
    i = None
    while not possibleSquare(board, n, i):
        i = askUserNumber("Choose a square : ") - 1
    return i

def possibleDestination(board, n, i, j):
    if j is None:
        return False
    #On retourne true si j est une case inférieur à celle de i
    return j >= 0 and j < i

def selectDestination(board, n, i):
    j = None
    while not possibleDestination(board, n, i, j):
        j = askUserNumber("Choose a destination : ") - 1
    return j

def move(board, n, i, j):
    board[i] -= 1 #On enlève un pion à la case où on a sélectionné le pion
    board[j] += 1 #On rajoute un pion à la case où on a définit sa nouvelle destination

def lose(board, n):
    #Tant qu'il au moins une case != 0, on continue à jouer
    for i in range(1, n):
        if board[i] != 0:
            return False
    return True

def changePlayer(player, nbrPlayer):
    if player < nbrPlayer:
        player += 1
    else:
        player = 1
    return player

def nimble(n, p, nbrPlayer):
    player = nbrPlayer
    gameBoard = newBoard(n, p)

    #Tant que lose ne renvoie pas true, on continue le jeu
    while not lose(gameBoard, n):
        changePlayer(player, nbrPlayer)
        print("\nPlayer", player, "is playing :\n")
        displayBoard(gameBoard, n)
        squareSelected = selectSquare(gameBoard, n)
        desSelected = selectDestination(gameBoard, n, squareSelected)
        move(gameBoard, n, squareSelected, desSelected)

    #Message de fin indiquant quel est le gagnant
    displayBoard(gameBoard, n)
    print("Winner :", player)
    input("Press enter to close ")

#Début du programme
print("NIMBLE | MARTINEZ Clément | version : 1.0\n")
amountSquare, maxPawn, player = defineParamGame()
nimble(amountSquare, maxPawn, player)