import pygame
from pygame.locals import *
from sosAlgorithms import *
import ast
import os
from random import randint

screen = [850, 550]
pygame.init()
mySurface = pygame.display.set_mode((screen[0], screen[1]))
pygame.display.set_caption("SOS Game")
fpsClock = pygame.time.Clock()

#Color
white = (236, 240, 241)
greyF = (60, 68, 76)
greyC = (189, 195, 199)
greenF = (39, 174, 96)
greenC = (46, 204, 113)
redF = (192, 57, 43)
redC = (231, 76, 60)
blue = (41, 128, 185)
playerColor = (redC, blue, greenC, greyF)

#Image
playNormal = pygame.image.load("data/img/bt-menu/play-normal.png")
playHover = pygame.image.load("data/img/bt-menu/play-hover.png")
playActive = pygame.image.load("data/img/bt-menu/play-active.png")
playNormal2 = pygame.image.load("data/img/bt-menu/play-normal.png")
playHover2 = pygame.image.load("data/img/bt-menu/play-hover.png")
playActive2 = pygame.image.load("data/img/bt-menu/play-active.png")
leaveNormal = pygame.image.load("data/img/bt-menu/leave-normal.png")
leaveHover = pygame.image.load("data/img/bt-menu/leave-hover.png")
leaveActive = pygame.image.load("data/img/bt-menu/leave-active.png")
newNormal = pygame.image.load("data/img/bt-mode/new-normal.png")
newHover = pygame.image.load("data/img/bt-mode/new-hover.png")
newActive = pygame.image.load("data/img/bt-mode/new-active.png")
saveNormal = pygame.image.load("data/img/bt-mode/save-normal.png")
saveHover = pygame.image.load("data/img/bt-mode/save-hover.png")
saveActive = pygame.image.load("data/img/bt-mode/save-active.png")
saveNormal2 = pygame.image.load("data/img/bt-mode/save-normal.png")
saveHover2 = pygame.image.load("data/img/bt-mode/save-hover.png")
saveActive2 = pygame.image.load("data/img/bt-mode/save-active.png")
gmBot = pygame.image.load("data/img/bt-config/gm-bot.png")
gmPlayer = pygame.image.load("data/img/bt-config/gm-player.png")
botEasy = pygame.image.load("data/img/bt-config/bot-easy.png")
botHard = pygame.image.load("data/img/bt-config/bot-hard.png")
arrowLNormal = pygame.image.load("data/img/bt-config/arrowL-normal.png")
arrowRNormal = pygame.image.load("data/img/bt-config/arrowR-normal.png")

#Bouton
playButton = [playNormal, playHover, playActive]
playButton2 = [playNormal2, playHover2, playActive2]
playInMenu = [315, 300, 220, 80, False]
playInNew = [315, 450, 220, 80, False]
playInSave = [0, 0, 0, 0, False, 0]
deleteInSave = [0, 0, 0, 0, False, 0]
leaveButton = [leaveNormal, leaveHover, leaveActive]
leaveInMenu = [315, 400, 220, 80, False]
newButton = [newNormal, newHover, newActive]
newInMode = [215, 185 ,180, 224, False]
saveButton = [saveNormal, saveHover, saveActive]
saveButton2 = [saveNormal2, saveHover2, saveActive2]
saveInMode = [455, 185, 180, 224, False]
saveInGame = [0, 0, 80, 90, False]
goBack = [20, 20, 70, 70, False]

#Deux boutons
gmButton = [[300, 125], [250, 90], [gmBot, gmPlayer], False, True]
botButton = [[300, 340], [250, 90], [botHard, botEasy], False, True]

#Selecteur
sizeSelect = [[330, 250], [180, 60], [arrowLNormal, arrowRNormal], ["4 x 4", "6 x 6", "8 x 8"], 0]
playerSelect = [[300, 360], [240, 60], [arrowLNormal, arrowRNormal], ["2 players", "3 players", "4 players"], 0]

#Panel
save = [[0, 120], [screen[0], 60], [greyF, greyC, greenF]]

#Scène affiché à l'écran par défaut
scene = "menu"

#Logo du jeu "SOS Game"
font = pygame.font.Font("data/font/helsinki.ttf", 80)
logo = font.render("SOS Game", True, greyF)

def displayButton(btData, btType):
    mouse = pygame.mouse.get_pos()
    #Redimmensionne les images
    for i in range(len(btType)):
        btType[i] = pygame.transform.scale(btType[i], (btData[2], btData[3]))
    #Change l'image en fonction des events
    if btData[4] == False:
        if mouse[0] > btData[0] and mouse[0] < btData[0] + btData[2] and mouse[1] > btData[1] and mouse[1] < btData[1] + btData[3]:
            mySurface.blit(btType[1], (btData[0], btData[1]))
        else:
            mySurface.blit(btType[0], (btData[0], btData[1]))
    else:
        mySurface.blit(btType[2], (btData[0], btData[1]))

def displayTwoButton(bt):
    for i in range(len(bt[2])):
        bt[2][i] = pygame.transform.scale(bt[2][i], (bt[1][0], bt[1][1]))
    if bt[3] == True:
        mySurface.blit(bt[2][0], (bt[0][0], bt[0][1]))
    if bt[4] == True:
        mySurface.blit(bt[2][1], (bt[0][0], bt[0][1]))

def displaySelector(sl):
    #Redimmensionnement des images
    for i in range(len(sl[2])):
        sl[2][i] = pygame.transform.scale(sl[2][i], (sl[1][1], sl[1][1]))
    #Réglage du text (police, taille, couleur, coordonnées)
    fontSelector = pygame.font.Font("data/font/helsinki.ttf", 40)
    textSelector = fontSelector.render(sl[3][sl[4]], True, (236, 240, 241))
    fontSelectorX = sl[0][0] + sl[1][0]/2 - (textSelector.get_rect().width)/2
    fontSelectorY = sl[0][1] + sl[1][1]/2 - (textSelector.get_rect().height)/2
    #Flèche
    mySurface.blit(sl[2][0], (sl[0][0] - sl[1][1], sl[0][1]))
    mySurface.blit(sl[2][1], (sl[0][0] + sl[1][0], sl[0][1]))
    #Text
    mySurface.blit(textSelector,(fontSelectorX, fontSelectorY))

def clickButton(btData):
    if btData[4] == False:
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > btData[0] and event.pos[0] < btData[0] + btData[2] and event.pos[1] > btData[1] and event.pos[1] < btData[1] + btData[3]:
                btData[4] = True

def clickTwoButton(bt):
    if event.type == MOUSEBUTTONDOWN:
        if event.pos[0] > bt[0][0] and event.pos[0] < bt[0][0] + bt[1][0]/2 and event.pos[1] > bt[0][1] and event.pos[1] < bt[0][1] + bt[1][1]:
            bt[3] = False
            bt[4] = True
        if event.pos[0] > bt[0][0] + bt[1][0]/2 and event.pos[0] < bt[0][0] + bt[1][0] and event.pos[1] > bt[0][1] and event.pos[1] < bt[0][1] + bt[1][1]:
            bt[3] = True
            bt[4] = False

def clickSelector(sl):
    if event.type == MOUSEBUTTONDOWN:
        if event.pos[0] > sl[0][0] - sl[1][1] and event.pos[0] < sl[0][0] - sl[1][1] + sl[1][1] and event.pos[1] > sl[0][1] and event.pos[1] < sl[0][1] + sl[1][1]:
            if sl[4] > 0:
                sl[4] -= 1
        if event.pos[0] > sl[0][0] + sl[1][0] and event.pos[0] < sl[0][0] + sl[1][0] + sl[1][1] and event.pos[1] > sl[0][1] and event.pos[1] < sl[0][1] + sl[1][1]:
            if sl[4] < len(sl[3])-1:
                sl[4] += 1

def addTextCenter(x, y, w, h, text, color, fontSize):
    font = pygame.font.Font("data/font/helsinki.ttf", fontSize)
    finalText = font.render(text, True, color)
    textX = x + w/2 - finalText.get_rect().width/2
    textY = y + h/2 - finalText.get_rect().height/2
    mySurface.blit(finalText, (textX, textY))

def displaySave(reg, save, btData, btType, btData2):
    percent = [0.3, 0.2, 0.2, 0.2, 0.1]
    x = save[0][0]
    h = save[1][1]
    for i in range(len(reg)):
        y = save[0][1]+i*save[1][1]
        w = save[1][0]
        if i%2 == 0:
            pygame.draw.rect(mySurface, save[2][0], (x, y, w, h))
        else:
            pygame.draw.rect(mySurface, save[2][1], (x, y, w, h))
        addTextCenter(x, y, w*percent[0], h, "Party " + str(int(reg[i][0])), save[2][2], 20)
        addTextCenter(x + w*percent[0], y, w*percent[1], h, reg[i][1]+"x"+reg[i][1], save[2][2], 20)
        addTextCenter(x + w*(percent[0]+percent[1]), y, w*percent[2], h, "Player" if reg[i][2] == "p" else "Bot", save[2][2], 20)
        
        #Play button
        btData[0] = int(x + w*(percent[0]+percent[1]+percent[2]))
        btData[1] = int(y-5)
        btData[2] = int(w*percent[3])
        btData[3] = int(h)
        displayButton(btData, btType)
        mouse = pygame.mouse.get_pos()
        if mouse[0] > btData[0] and mouse[0] < btData[0] + btData[2] and mouse[1] > save[0][1] and mouse[1] < save[0][1] + btData[3]*len(reg):
            if mouse[0] > btData[0] and mouse[0] < btData[0] + btData[2] and mouse[1] > btData[1] and mouse[1] < btData[1] + btData[3]:
                btData[5] = i
        else:
            btData[5] = None
        #Delete button
        btData2[0] = int(x + w*(percent[0]+percent[1]+percent[2]+percent[3]))
        btData2[1] = y
        btData2[2] = int(w*percent[4])
        btData2[3] = int(h)
        addTextCenter(btData2[0], btData2[1], btData2[2], btData2[3], "x", redF, 30)
        mouse = pygame.mouse.get_pos()
        if mouse[0] > btData2[0] and mouse[0] < btData2[0] + btData2[2] and mouse[1] > save[0][1] and mouse[1] < save[0][1] + btData2[3]*len(reg):
            if mouse[0] > btData2[0] and mouse[0] < btData2[0] + btData2[2] and mouse[1] > btData2[1] and mouse[1] < btData2[1] + btData2[3]:
                btData2[5] = i
        else:
            btData2[5] = None

def clickButtonSave(btData):
    if event.type == MOUSEBUTTONDOWN and btData[5] != None:
        btData[4] = True

def displayBtCircle(btData, color1, color2, colorText, text):
    mouse = pygame.mouse.get_pos()
    if mouse[0] > btData[0] and mouse[0] < btData[0] + btData[2] and mouse[1] > btData[1] and mouse[1] < btData[1] + btData[2]:
        pygame.draw.circle(mySurface, color2, (int(btData[0]+btData[2]/2), int(btData[1]+btData[2]/2)), int(btData[2]/2))
    else:
        pygame.draw.circle(mySurface, color1, (int(btData[0]+btData[2]/2), int(btData[1]+btData[2]/2)), int(btData[2]/2))
    addTextCenter(btData[0], btData[1], btData[2], btData[2], text, colorText, 20)

#Game panel
def drawBoard(surface, n, x, y, size, cellSize, gap):
    #On dessine le carré qui nous servira de tableau
    pygame.draw.rect(surface, greyC, (x, y, size, size))
    #On trace les délimitation des cases
    for i in range(n):
        pygame.draw.line(surface, white, (x + i * cellSize, y), (x + i * cellSize, y + size), gap)
    for j in range(n):
        pygame.draw.line(surface, white, (x, y + j * cellSize), (x + size, y + j * cellSize), gap)
    #Ajout des lettres S et O dans chaque case
    for j in range(n):
        for i in range(n):
            addTextCenter(x + i * cellSize, y + j * cellSize, cellSize/2, cellSize, "S", white, 20)
            addTextCenter(x + i * cellSize + cellSize/2, y + j * cellSize, cellSize/2, cellSize, "O", white, 20)

def selectSquare(surface, board, n, x, y, cellSize):
    mouse = pygame.mouse.get_pos()
    for j in range(n):
        for i in range(n):
            if mouse[0] > x + cellSize * i and mouse[0] < x + cellSize * i + cellSize and mouse[1] > y + cellSize * j and mouse[1] < y + cellSize * j + cellSize:
                if possibleSquare(board, n, i, j):
                    if mouse[0] > x + cellSize * i and mouse[0] < x + cellSize * i + cellSize/2 and mouse[1] > y + cellSize * j and mouse[1] < y + cellSize * j + cellSize:
                        return (i, j, 1)
                    else:
                        return (i, j, 2)
    
def displayScore(surface, n, scores, x, y, w, h, percent):
    pygame.draw.rect(surface, white, (x, y, w, h))
    addTextCenter(x, y, w, h*0.2, "Scores", greyF, 20)
    cSize = int((w*percent)/2)
    posY = int(y + h*0.2)
    pygame.draw.circle(surface, playerColor[0], (x + cSize, posY + cSize), cSize)
    addTextCenter(x, posY, cSize*2, cSize*2, str(scores[0]), white, 30)
    pygame.draw.circle(surface, playerColor[1], (x + w - cSize, posY + cSize), cSize)
    addTextCenter(x + w - cSize*2, posY, cSize*2, cSize*2, str(scores[1]), white, 30)   
    if len(scores) > 2:
        pygame.draw.circle(surface, playerColor[2], (x + cSize, y + h - cSize), cSize)
        addTextCenter(x, y + h - cSize*2, cSize*2, cSize*2, str(scores[2]), white, 30)
    if len(scores) > 3:
        pygame.draw.circle(surface, playerColor[3], (x + w - cSize, y + h - cSize), cSize)
        addTextCenter(x + w - cSize*2, y + h - cSize*2, cSize*2, cSize*2, str(scores[3]), white, 30)

def displayPlayer(surface, n, player, x, y, w, h):
    posX = x+w-h
    pygame.draw.rect(surface, white, (x, y, w, h))
    addTextCenter(x, y, w-h, h, "Player", greyF, 20)
    pygame.draw.circle(surface, playerColor[player], (int(posX+h/2), int(y+h/2)), int(h/2))
    addTextCenter(posX, y, h, h, str(player+1), white, 20)

def drawCell(surface, square, player, x, y, cellSize):
    cellX = x + square[0]*cellSize
    cellY = y + square[1]*cellSize
    if square[2] != 0:
        letter = "S" if square[2] == 1 else "O"
        pygame.draw.rect(surface, greyC, (cellX+2, cellY+2, cellSize-2, cellSize-2))
        addTextCenter(cellX, cellY, cellSize, cellSize, letter, playerColor[player], 20)
    
def drawLines(surface, lines, x, y, cellSize):
    if len(lines) >= 1:
        for nbrLine in range(len(lines)):
            pygame.draw.line(surface, playerColor[lines[nbrLine][2]], (x + lines[nbrLine][0][0]*cellSize + cellSize/2, y + lines[nbrLine][0][1]*cellSize + cellSize/2), (x + lines[nbrLine][1][0]*cellSize + cellSize/2,y + lines[nbrLine][1][1]*cellSize + cellSize/2), 3)
        
def changePlayer(p, nbrP):
    p = p + 1 if p < nbrP-1 else 0
    return p

def initValueSl(sl):
    return int(sl[3][sl[4]][0])

def displayStats(x, y, w, h, data, btData):
    sizeTitle = h*0.15
    gap = 20
    pygame.draw.rect(mySurface, greyF, (x, y, w, h))
    pygame.draw.line(mySurface, greyC, (x, y+sizeTitle), (x+w, y+sizeTitle), 3)
    addTextCenter(x, y, w, sizeTitle, "Game", greyC, 25)
    posY = sizeTitle + gap
    sizeText = h*0.12
    for i in range(len(data)):
        addTextCenter(x, y+posY, w, sizeText, data[i], greyC, 20)
        posY += sizeText
    btData[0] = x + w/2 - btData[2]/2
    btData[1] = y + h - gap - btData[3]

def drawAllCells(board, boardColor, n):
    for j in range(n):
        for i in range(n):
            drawCell(mySurface, (i, j, board[j][i]), boardColor[j][i]-1, boardX, boardY, cellSize)

def readRegister(registerFile):
    reg = []
    f = open(registerFile, "r")
    amountLine = int(f.readline())
    for line in range(1, amountLine+1):
        currentLine = f.readline()
        index = currentLine[0]+currentLine[1]
        size = currentLine[2]
        gameMode = currentLine[3]
        reg.append((index, size, gameMode))
    f.close()
    return reg

def readAllDataGame(path, filename):
    f = open(path + filename + ".txt", "r")
    currentLine = f.readline()
    boardSave = ast.literal_eval(currentLine)
    currentLine = f.readline()
    boardColorSave = ast.literal_eval(currentLine)
    currentLine = f.readline()
    linesSave = ast.literal_eval(currentLine)
    currentLine = f.readline()
    scoresSave = ast.literal_eval(currentLine)
    currentPlayer = f.readline()
    return boardSave, boardColorSave, linesSave, scoresSave, int(currentPlayer)

def addSaveRegister(path, filename, register, n, mode):
    #Modifie le fichier des registres
    f = open(path + filename + ".txt", "w")
    f.write(str(len(register)+1) + "\n")
    biggerIndex = 0
    for i in range(len(register)):
        if int(register[i][0]+register[i][1]) > biggerIndex:
            biggerIndex = int(register[i][0])+1
    for i in range(len(register)):
        f.write(str(register[i][0]) + str(register[i][1]) + str(register[i][2]) + "\n")
    f.write(str("0" + str(biggerIndex) if len(str(biggerIndex)) == 1 else biggerIndex) + str(n) + str("p" if mode == "player" else "b") + "\n")
    f.close()

def removeSave(path, filename, register, index):
    print(index)
    f = open(path + filename + ".txt", "w")
    f.write(str(len(register)-1) + "\n")
    indexG = int(register[index][0])
    print(register)
    del register[index]
    print(register)
    for i in range(len(register)):
        f.write(str(register[i][0]) + str(register[i][1]) + str(register[i][2]) + "\n")
    f.close()
    print(f)
    os.remove(path + str(indexG) + ".txt")

def saveGame(path, index, board, boardColor, lines, scores, player):
    f = open(path + str(index) + ".txt", "w")
    f.write(str(board) + "\n")
    f.write(str(boardColor) + "\n")
    f.write(str(lines) + "\n")
    f.write(str(scores) + "\n")
    f.write(str(player) + "\n")
    f.close()

def displayWinner(scores):
    highScore = max(scores)
    nbrWinner = scores.count(highScore)
    allWinners = []
    if highScore == 0 or nbrWinner == len(scores):
        addTextCenter(710, 400, 50, 40, "No winner", greenF, 20)
    if nbrWinner != 1 and highScore != 0 and nbrWinner != len(scores):
        for i in range(len(scores)):
            if scores[i] == highScore:
                allWinners.append(i)
        addTextCenter(710, 400, 50, 40, "The winners are :", greenF, 20)
        addTextCenter(710, 440, 50, 40, "the player " + str(allWinners[0]+1), greenF, 20)
        if len(allWinners) >= 2:
            addTextCenter(710, 480, 50, 40, "the player " + str(allWinners[1]+1), greenF, 20)
        if len(allWinners) >= 3:
            addTextCenter(710, 520, 50, 40, "the player " + str(allWinners[2]+1), greenF, 20)
    if nbrWinner == 1 and highScore != 0:
        player = scores.index(highScore)+1
        addTextCenter(710, 400, 50, 40, "The winner is", greenF, 20)
        addTextCenter(710, 440, 50, 40, "the player " + str(player), greenF, 20)

def iaeasy(Surface, player, boardX, boardY, cellSize,n,board, boardColor):
    if  player == 1:
        possibleCases = []
        for j in range(n):
            for i in range(n):
                if board[j][i] == 0:
                    possibleCases.append((i, j))
        if len(possibleCases) != 0:
            i = randint(0, len(possibleCases)-1)
            k = randint(1, 2)
            square=(possibleCases[i][0], possibleCases[i][1],k)
            drawCell(Surface, square, player, boardX, boardY,  cellSize)
            update(board, n, square, scores, player, lines, boardColor)
            drawLines(Surface, lines, boardX, boardY, cellSize)

inProgress = True
while inProgress:
    if scene == "menu": #Menu home
        #Background
        mySurface.fill(white)
        #Logo
        addTextCenter(0, 0, screen[0], 300, "SOS Game", greyF, 80)
        displayButton(playInMenu, playButton)
        displayButton(leaveInMenu, leaveButton)
        addTextCenter(0, 510, 470, 40, "Made by Jonathan CLAVEL & Clément MARTINEZ", greyF, 18)
        if playInMenu[4] == True:
            playInMenu[4] = False
            scene = "mode"
        if leaveInMenu[4] == True:
            inProgress = False

        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            clickButton(playInMenu)
            clickButton(leaveInMenu)
    elif scene == "mode": #Menu de sélection du mode de jeu
        #Background
        mySurface.fill(greenC)
        #Logo
        addTextCenter(0, 0, screen[0], 130, "SOS Game", greyF, 80)
        displayButton(newInMode, newButton)
        displayButton(saveInMode, saveButton)
        displayBtCircle(goBack, white, greyC, greyF, "Back")
        if newInMode[4] == True:
            scene = "new"
            newInMode[4] = False
            register = readRegister("data/save/register.txt")
        if saveInMode[4] == True:
            scene = "save"
            saveInMode[4] = False
            register = readRegister("data/save/register.txt")
        if goBack[4] == True:
            scene = "menu"
            goBack[4] = False
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            clickButton(newInMode)
            clickButton(saveInMode)
            clickButton(goBack)
    elif scene == "new":
        #Background
        mySurface.fill(greenC)
        #Logo
        addTextCenter(0, 0, screen[0], 130, "SOS Game", greyF, 80)
        displayTwoButton(gmButton)
        displaySelector(sizeSelect)
        displayButton(playInNew, playButton)
        displayBtCircle(goBack, white, greyC, greyF, "Back")
        if gmButton[3] == True:
            displayTwoButton(botButton)
        if gmButton[4] == True:
            displaySelector(playerSelect)
        if playInNew[4] == True:
            playInNew[4] = False
            scene = "game"
            #Variables
            n = initValueSl(sizeSelect)
            name = None
            mode = "player" if gmButton[3] == False else "bot"
            player = 0
            nbrPlayer = initValueSl(playerSelect) if gmButton[3] == False else 2
            lines = []
            scores = [0 for i in range(nbrPlayer)]
            boardSize = 400
            cellSize = boardSize/n
            boardX = int(screen[0]/2 - boardSize/2)
            boardY = int(screen[1]/2 - boardSize/2)
            board = newBoard(n)
            boardColor = newBoard(n)
            #Display
            mySurface.fill(white)
            drawBoard(mySurface, n, boardX, boardY, boardSize, cellSize, 2)
            displayPlayer(mySurface, n, player, 650, 10, 150, 50)
            displayScore(mySurface, n, scores, 650, 150, 170, 200, 0.45)
        if goBack[4] == True:
            scene = "mode"
            goBack[4] = False
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            clickTwoButton(gmButton)
            clickTwoButton(botButton)
            clickSelector(sizeSelect)
            clickSelector(playerSelect)
            clickButton(playInNew)
            clickButton(goBack)
    elif scene == "save":
        #Background
        mySurface.fill(white)
        #Logo
        addTextCenter(0, 0, screen[0], 130, "SOS Game", greyF, 80)
        if len(register) != 0:
            displaySave(register, save, playInSave, playButton2, deleteInSave)
        else:
            addTextCenter(0, 0, screen[0], screen[1], "No backup  :I", greyF, 40)
        displayBtCircle(goBack, white, greyC, greyF, "Back")
        if playInSave[4] == True and len(register) != 0:
            board, boardColor, lines, scores, player = readAllDataGame("data/save/", str(int(register[int(playInSave[5])][0])))
            playInSave[4] = False
            scene = "game"
            #Variables
            n = int(register[playInSave[5]][1])
            name = "Party " + str(int(register[playInSave[5]][0]))
            mode = "player" if register[playInSave[5]][2] == "p" else "bot"
            nbrPlayer = len(scores)
            boardSize = 400
            cellSize = boardSize/n
            boardX = int(screen[0]/2 - boardSize/2)
            boardY = int(screen[1]/2 - boardSize/2)
            #Display
            mySurface.fill(white)
            drawBoard(mySurface, n, boardX, boardY, boardSize, cellSize, 2)
            displayPlayer(mySurface, n, player, 650, 10, 150, 50)
            displayScore(mySurface, n, scores, 650, 150, 170, 200, 0.45)
            drawAllCells(board, boardColor, n)
            drawLines(mySurface, lines, boardX, boardY, cellSize)
        if goBack[4] == True:
            scene = "mode"
            goBack[4] = False
        if deleteInSave[4] == True:
            if len(register) != 0:
                removeSave("data/save/", "register", register, deleteInSave[5]) 
                register = readRegister("data/save/register.txt")
            deleteInSave[4] = False
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            clickButtonSave(playInSave)
            clickButtonSave(deleteInSave)
            clickButton(goBack)
    elif scene == "game":
        displayBtCircle(goBack, white, greyC, greyF, "Back")
        addTextCenter(0, 0, screen[0], 85, "SOS Game", greyF, 50)
        displayStats(40, 120, 150, 300, ("unknown" if name == None else name, str(n)+"x"+str(n), mode), saveInGame)
        displayButton(saveInGame, saveButton2)
        if goBack[4] == True:
            scene = "mode"
            goBack[4] = False
        if saveInGame[4] == True:
            saveInGame[4] = False
            if len(register) < 7:
                if name == None:
                    addSaveRegister("data/save/", "register", register, n, mode)
                    register = readRegister("data/save/register.txt")
                    saveGame("data/save/", int(register[len(register)-1][0]), board, boardColor, lines, scores, player)   
                    name = "Party " + str(int(register[len(register)-1][0]))
                else:
                    saveGame("data/save/", int(register[playInSave[5]][0]), board, boardColor, lines, scores, player)      
            else:
                addTextCenter(0, 510, screen[0], 40, "The maximum number of backups allowed is 7", redC, 20)
        if endGame(board) == True:
            displayWinner(scores)
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            clickButton(goBack)
            clickButton(saveInGame)
            if event.type == MOUSEBUTTONDOWN and endGame(board) == False:
                if event.pos[0] > boardX and event.pos[0] < boardX + boardSize and event.pos[1] > boardY and event.pos[1] < boardY + boardSize:
                    squareSelected = selectSquare(mySurface, board, n, boardX, boardY, cellSize)
                    if squareSelected != None:
                        scoresSave = scores.copy()
                        drawCell(mySurface, squareSelected, player, boardX, boardY, cellSize)
                        update(board, n, squareSelected, scores, player, lines, boardColor)
                        drawLines(mySurface, lines, boardX, boardY, cellSize)
                        if scores == scoresSave:
                            player = changePlayer(player, nbrPlayer)
                        displayPlayer(mySurface, n, player, 650, 10, 150, 50)
                        displayScore(mySurface, n, scores, 650, 150, 170, 200, 0.45)
                        
                        if mode == "bot":
                            if player == 1:
                                scoresSave = scores.copy()
                                iaeasy(mySurface, player, boardX, boardY, cellSize,n,board, boardColor)
                                while scores != scoresSave:
                                    scoresSave = scores.copy()
                                    iaeasy(mySurface, player, boardX, boardY, cellSize,n,board, boardColor)
                                player = changePlayer(player,nbrPlayer)
                                displayPlayer(mySurface, n, player, 650, 10, 150, 50)
                                displayScore(mySurface, n, scores, 650, 150, 170, 200, 0.45)
    pygame.display.update()
    fpsClock.tick(30)
pygame.quit()