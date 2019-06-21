def newBoard(n):
    #Génére un tableau à deux dimensions où chaque case vaut 0
    board = [[0 for i in range(n)] for j in range(n)]
    return board

def possibleSquare(board, n, i, j):
    if i >= 0 and i < n and j >= 0 and j < n:
        return board[j][i] == 0
    return False

def updateScoreS(board, n, i, j, scores, player, lines):
    #Ligne
    if i >= 0 and i < n-(1+1): #Test vers la droite
        if board[j][i+1] == 2 and board[j][i+2] == 1:
            scores[player] += 1
            lines.append([(i,j),(i+2,j), player])
    if i >= 2 and i <= n-1: #Test vers la gauche
        if board[j][i-1] == 2 and board[j][i-2] == 1:
            scores[player] += 1
            lines.append([(i,j),(i-2,j), player])
    #Colonne
    if j >= 0 and j < n-(1+1): #Test vers le bas
        if board[j+1][i] == 2 and board[j+2][i] == 1:
            scores[player] += 1
            lines.append([(i,j),(i,j+2), player])
    if j >= 2 and j <= n-1: #Test vers le haut
        if board[j-1][i] == 2 and board[j-2][i] == 1:
            scores[player] += 1
            lines.append([(i,j),(i,j-2), player])
    #Diagonale
    if i >= 0 and i < n-(1+1) and j >= 2 and j <= n-1: #Test vers haut droite
        if board[j-1][i+1] == 2 and board[j-2][i+2] == 1:
            scores[player] += 1
            lines.append([(i,j),(i+2,j-2), player])
    if i >= 0 and i < n-(1+1) and j >= 0 and j < n-(1+1): #Test vers bas droite
        if board[j+1][i+1] == 2 and board[j+2][i+2] == 1:
            scores[player] += 1
            lines.append([(i,j),(i+2,j+2), player])
    if i >= 2 and i <= n-1 and j >= 0 and j < n-(1+1): #Test vers bas gauche
        if board[j+1][i-1] == 2 and board[j+2][i-2] == 1:
            scores[player] += 1
            lines.append([(i,j),(i-2,j+2), player])
    if i >= 2 and i <= n-1 and j >= 2 and j <= n-1: #Test vers haut gauche
        if board[j-1][i-1] == 2 and board[j-2][i-2] == 1:
            scores[player] += 1
            lines.append([(i,j),(i-2,j-2), player])

def updateScoreO(board,n,i,j,scores,player,lines):
    if i >= 1 and j >= 1 or i >= 1 and j <= n-2 or i >= n-2 and j >= 0 or i <= n-2 and j <= n-2:
        #Ligne
        if j >= 1 and j <= n - 2:
            if board[j-1][i] == 1 and board[j+1][i] == 1:
                scores[player] += 1
                lines.append([(i,j-1), (i,j+1), player])
        #Colonne
        if i >= 1 and i <= n - 2:
            if board[j][i-1] == 1 and board[j][i+1] == 1:
                scores[player] += 1
                lines.append([(i-1,j), (i+1, j), player])
        #Diagonale
        if j >= 1 and i >= 1 and j <= n-2 and i <= n-2 :
            if board[j-1][i-1] == 1 and board[j+1][i+1] == 1: #\
                scores[player] += 1
                lines.append([(i-1, j-1), (i+1, j+1), player])
            if board[j+1][i-1] == 1 and board[j-1][i+1] == 1: #/
                scores[player] += 1
                lines.append([(i-1 ,j+1), (i+1, j-1), player])
def update(board,n,square,scores,player,lines, boardColor):
    board[square[1]][square[0]] = square[2]
    boardColor[square[1]][square[0]] = player+1
    if square[2] == 1:
        updateScoreS(board, n, square[0],square[1], scores, player, lines)
    if square[2] == 2:
        updateScoreO(board, n, square[0],square[1], scores, player, lines)

def endGame(board):
    for j in range(len(board)):
        for i in range(len(board)):
            if board[j][i] == 0:
                return False
    return True