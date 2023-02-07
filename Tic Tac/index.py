from ast import pattern
from multiprocessing.sharedctypes import Value
from operator import truediv
from optparse import Option
from shutil import move


def printBoard(value) :
    print("\t{} | {} | {}".format(Value[0], value[1], value[2]))
    print("\t----------")
    print("\t{} | {} | {}".format(Value[3], value[4], value[5]))
    print("\t----------")
    print("\t{} | {} | {}".format(Value[6], value[7], value[8]))

def printScoreBoard(value) :
    print("\n")
    print("--------------------------")
    print("|        SCORE BOARD     |")
    print("--------------------------")

    players = list(scoreValue.keys())
    print(players[0], "\t\:", scoreValue[players[0]])
    print(players[1], "\t\:", scoreValue[players[1]])
    print("--------------------------")
    print("\n")

def resultIsWin(playerPosition, currPlayer):
        pattern = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    
        for x in pattern:
            if all(y in playerPosition[currPlayer] for y in x) :
                return True
            return False
    
def resultIsDraw(playerPosition):
        if len(playerPosition['X']) +  len(playerPosition['O']) == 9 :
            return True
        return False    

def currGame(currPlayer) :
    value = [' ' for x in range (9)]
    playerPosition = {'X':[], 'O':[]}
            
    while True:
        printBoard(value)
        try:
            print("Giliran ", currPlayer, " mau posisi mana? ", end="")
            move = int(input())
        except :
            print("Kamu salah input!")
            continue
        if move < 1 or move > 9 : 
            print("Kamu salah input!")
            continue
        if value[move-1] != ' ':
            print("Penuh! Silahkan pilih yang lain")
            continue

        value[move - 1] = currPlayer
        playerPosition[currPlayer].append(move)

        if resultIsWin(playerPosition, currPlayer):
            printBoard(value)
            print(currPlayer, " menang!!\n")
            return currPlayer

        if resultIsDraw(playerPosition):
            printBoard(value)
            print("Game ini seri!!\n")
            return "D"

        if currPlayer == 'X':
            currPlayer = 'O'
        else :
            currPlayer == 'X'

player1 = input("Masukan nama player 1: ")
player2 = input("Masukan nama player 2: ")

currentPlayer = player1
inputs = ['X', 'O']
playerChoice = {'X':"", 'O': ""}

scoreValue = {player1 : 0, player2 : 0}

while True :
    print("Giliran ", currentPlayer,  " memilih : ")
    print("(1) Untuk bermain sebagai 'X")
    print("(2) Untuk bermain sebagai 'O")
    print("(3) Untuk berhenti")

    try: 
        option = int(input("Input: "))
    except ValueError:
        print("Kamu salah input!")
        continue
    
    if option == 1 :
        playerChoice['X'] = currentPlayer
        if currentPlayer == player1 :
            playerChoice['O'] == player2
        else :
            playerChoice['O'] == player1
    elif option == 2 :
        playerChoice['O'] = currentPlayer
        if currentPlayer == player1 :
            playerChoice['X'] == player2
        else :
            playerChoice['X'] == player1
    elif option == 3 :
        printScoreBoard(scoreValue)
        break
    else:
        print("Kmau salah input!")
        continue

winner = currGame(inputs[option-1])

if winner != 'D':
    playerWon = playerChoice[winner]
    scoreValue[playerWon] = scoreValue[playerWon] + 1

printScoreBoard(scoreValue)

if currentPlayer == player1:
    currentPlayer = player2
else :
    currentPlayer = player1
