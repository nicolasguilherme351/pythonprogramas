import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
boardView = ""
lenBoard = 0
game = True
player1Symbol = ""
player2Symbol = ""
player1Number = 1
player2Number = 2
player1Points = 0
player2Points = 0

def showBoard(board, boardView):
    for i in range(0, len(board)):
        for q in board[i]:
            boardView += str(q)
        boardView += "\n"
    print(boardView)

def defineMoves(playerSymbol, board, playerNumber, boardView):
    g = 0
    print("Player", playerNumber)
    print("Digit the position")
    movePlayer = int(input())
    if(movePlayer >= 1 and movePlayer <= 9):
         for i in range(0, len(board)):
            for q in range(0, len(board[i])):
                  if (board[i][q] == movePlayer):
                      board[i][q] = playerSymbol
                  else:
                      g+=1
                  if(g == 9):
                    print("This part is already used")
                    showBoard(board, boardView)
                    defineMoves(playerSymbol, board, playerNumber, boardView)
    else:
        print("digit valid number!")
        defineMoves(playerSymbol, board, playerNumber)

def playerWin(playerNumber, board, game):
            print("Player ", playerNumber, " win")
            decisionForPlayAgain = input("Do you want play again (s or n)? ")
            if (decisionForPlayAgain == 's'):
                # Restart the board for play again 
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            else:
                return False

def verifyBoard(board, playerSymbol, playerPoints, playerNumber, game):
        # Verify diagonals
            if((board[0][0] == playerSymbol and board[1][1] == playerSymbol and board[2][2] == playerSymbol) or (board[0][2] == playerSymbol and board[1][1] == playerSymbol and board[2][0] == playerSymbol)):
                    winner = playerWin(playerNumber, board, game)
                    return winner
        # Verify Lines
            elif ((board[0][0] == playerSymbol and board[0][1] == playerSymbol and board[0][2] == playerSymbol) or (board[1][0] == playerSymbol and board[1][1] == playerSymbol and board[1][2] == playerSymbol) or (board[2][0] == playerSymbol and board[2][1] == playerSymbol and board[2][2] == playerSymbol)):
                    winner = playerWin(playerNumber, board, game)
                    return winner
        # Verify Collumns 
            elif((board[0][0] == playerSymbol and board[1][0] == playerSymbol and board[2][0] == playerSymbol) or (board[0][1] == playerSymbol and board[1][1] == playerSymbol and board[2][1] == playerSymbol) or (board[0][2] == playerSymbol and board[1][2] == playerSymbol and board[2][2] == playerSymbol)):
                    winner = playerWin(playerNumber, board, game)
                    return winner
            return True

decision = input("Player 1: Do you want play with o or x? ")

if (decision == 'x'):
    player1Symbol = 'x'
    player2Symbol = 'o'
else:
    player2Symbol = 'x'
    player1Symbol = 'o'

def executeGame():
    result = True
    while(game == result):
        showBoard(board, boardView)
        if(player1Symbol == 'x'):
            defineMoves(player1Symbol, board, player1Number, boardView)
            showBoard(board, boardView)
            result = verifyBoard(board, player1Symbol, player1Points, player1Number, game)
            if (result == True):
                defineMoves(player2Symbol, board, player2Number, boardView)

        else:
            defineMoves(player2Symbol, board, player2Number, boardView)
            showBoard(board, boardView)
            result = verifyBoard(board, player2Symbol, player2Points, player2Number, game) 
            if (result == True):
                defineMoves(player1Symbol, board, player1Number, boardView)

executeGame()

