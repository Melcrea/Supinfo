def askUserNumber(message):
    nbr = ""
    #On vérifie que la valeur entrée par l'utilisateur est bien un nombre
    while not nbr.isdigit():
        nbr = str(input(message))
    return int(nbr)

def newBoard(n):
    #Génère un tableau en deux dimensions composant essentiellement de points
    board = [[0 for j in range(n)] for i in range(n)]
    for i in range(n): #Creer les croix verticales
        board[i][0] = 1
    for j in range(n - 1): #Creer les croix horizontales
        board[n - 1][j] = 1 
    for j in range(1, n): #Creer les ronds horizontaux
        board[0][j] = 2
    for i in range(n): #Creer les ronds verticaux
        board[i][n - 1] = 2
    return board

def display(board, n):
    #On parcourt le tableau en entier
    for i in range(n):
        for j in range(n):
            #On met des points pour les cases vides, celles qui sont égales à 0
            if board[i][j] == 0:
                print(".", end="  ")
            #On met des croix pour le premier joueur
            elif board[i][j] == 1:
                print("x", end="  ")
            #On met des ronds pour le deuxième joueur
            else:
                print("o", end="  ")
        print("\n")

def possiblePawn(board, n, player, i, j):
    if i is None:
        return False
    #S'il n'est pas sur le terrain
    if i > n - 1 or j > n - 1:
        return False
    #Si ce n'est pas son pion
    if board[i][j] == 0 or board[i][j] != player:
        return False
    #S'il ne peut pas être bougé
    if i != 0:
        if board[i - 1][j] == 0: #La case au dessus
            return True
    if i != n - 1:
        if board[i + 1][j] == 0: # La case en dessous
            return True
    if j != 0:
        if board[i][j - 1] == 0: # La case à gauche
            return True
    if j != n - 1:
        if board[i][j + 1] == 0: # La case à droite
            return True
    return False

def selectPawn(board, n, player):
    i, j = None, None
    while not possiblePawn(board, n, player, i, j):
        #On demande à l'utilisateur la pion à déplacer et on enlève -1 car le tableau commence à 0
        i = askUserNumber("Select a pawn,  row: ") - 1
        j = askUserNumber("Select a pawn, column: ") - 1
    return i, j

def possibleDestination(board, n, i, j, k, l):
    if k is None:
        return False
    #Si c'est toujours la même case
    if i == k and j == l:
        return False
    #S'ils sont sur la même ligne
    if i == k:
        for x in range(j + 1, l + 1):
            if board[i][x] != 0:
                return False
    #S'ils sont sur la même colonne
    elif j == l: 
        for x in range(i + 1, k + 1):
            if board[x][j] != 0:
                return False
    else:
        return False
    return True

def selectDestination(board, n, i, j):
    k, l = None, None
    while not possibleDestination(board, n, i, j, k, l):
        #On demande à l'utilisateur la case souhaitée et on enlève -1 car le tableau commence à 0
        k = askUserNumber("Select a destination,  row: ") - 1
        l = askUserNumber("Select a destination, column: ") - 1
    return k, l

def move(board, n, player, i, j, k, l):
    board[i][j] = 0 #On assigne 0 à l'ancienne case pour la vider
    board[k][l] = 1 if player == 1 else 2 #Et on place le bon pion en fonction du joueur qui joue

def testHorizontal(board, k, borneInf, borneSup):
    #On teste pour voir s'il y a des cases vides entre les deux bornes
    for j in range(borneInf, borneSup):
        if board[k][j] == 0:
            return False
    return True

def testVertical(board, l, borneInf, borneSup):
    #On teste pour voir s'il y a des cases vides entre les deux bornes
    for i in range(borneInf, borneSup):
        if board[i][l] == 0:
            return False
    return True

def capture(board, k, l):
    #On teste pour le joueur n°1 et le joueur n°2
    for typePlayer in range(1, 3):
        #On cherche tous les pions du même joueur sur la ligne où le nouveau pion vient d'être déplacé
        #On stocke les coordonnées dans la liste borne
        borne = []
        for j in range(len(board[k])):
            if board[k][j] == typePlayer:
                borne.append(j)
        #print("Horizontal : ", typePlayer, borne)
        #S'il y a des pions stockés dans la liste...
        if len(borne) > 0:
            for x in range(len(borne) - 1):
                #S'ils ne sont pas collés...
                if borne[x + 1] - borne[x] > 1:
                    #On teste s'il y a des espaces entre deux bornes
                    if testHorizontal(board, k, borne[x] ,borne[x + 1]):
                        #Et si c'est bon on transforme toute la ligne
                        for j in range(borne[x], borne[x + 1]):
                            board[k][j] = typePlayer
        borne = [] #On vide la liste
        #On cherche tous les pions du même joueur sur la colonne où le nouveau pion vient d'être déplacé
        #On stocke les coordonnées dans la liste borne
        for i in range(len(board)):
            if board[i][l] == typePlayer:
                borne.append(i)
        #print("Vertical : ", typePlayer, borne)
        #S'il y a des pions stockés dans la liste...
        if len(borne) > 0:
            for x in range(len(borne) - 1):
                #S'ils ne sont pas collés...
                if borne[x + 1] - borne[x] > 1:
                    #On teste s'il y a des espaces entre deux bornes
                    if testVertical(board, l, borne[x] ,borne[x + 1]):
                        #Et si c'est bon on transforme toute la ligne
                        for i in range(borne[x], borne[x + 1]):
                            board[i][l] = typePlayer
    
                
            
def lose(board, n, player):
    #On cherche les pions du joueur suivant
    player = 1 if player == 2 else 2
    #On parcours le tableau...
    for i in range(n):
        for j in range(n):
            #... et s'il est le pion de ce joueur ...
            if board[i][j] == player:
                #... on teste s'il est positionnable ailleurs
                if possiblePawn(board, n, player, i, j):
                    return False            
    #On teste s'il reste des pions au joeur en question
    if player in board:
        return False
    return True    

def changePlayer(player):
    #On change de joueur
    return 2 if player == 1 else 1

def mingMang(n):
    player = 2
    gameLevel = newBoard(n)
    
    #Tant que lose ne renvoie pas true, on continue le jeu
    while not lose(gameLevel, n, player):
        player = changePlayer(player)
        display(gameLevel, n)
        print("\nPlayer", player, "is playing :\n")
        i, j = selectPawn(gameLevel, n, player)
        k, l = selectDestination(gameLevel, n, i, j)
        move(gameLevel, n, player, i, j, k, l)
        capture(gameLevel, k, l)
    
    #Message de fin indiquant quel est le gagnant
    display(gameLevel, n)
    print("Winner :", player)
    input("Press enter to close ")

#Début du programme
print("MINGMANG | MARTINEZ Clément | version : 1.0\n")
#On demande de saisir un taille de terrain >3
size = -1
while size < 3:
    size = askUserNumber("Game size (min 3): ")
mingMang(size)