# File:    proj2.py
# Author:  Nick Sica
# Date:    10/30/2018
# Section: 30
# E-mail:  nsica1@umbc.edu
# Description: #   Playing the game connect 4, the user can either play against another play\er or a computer. First one to get 4 in a row on any size board greater than 4x4 wins

#random for computer
from random import randint

#min size of board
MIN_SIZE = 5
#player chips
PLAYER1 = "X"
PLAYER2 = "O"
#4 in a row
WIN = 4
#user input
YES = "y"
NO = "n"
#make the board 
BLANK = "_"



# Creates and returns the game board
# Input: takes in row and column to create the board
# Output: returns the board
def getBoard(row,column):
    gameBoard = []
    #while the length of the gameboard is less than the height
    while len(gameBoard) < row:
        boardRow = []
        while len(boardRow) < column:
            boardRow.append(BLANK)

        gameBoard.append(boardRow)
        
#creates the board 
    return gameBoard

# Will check for a winner after every turn
# Input: The game board, row and column
# Output: Returns the boolean Winner to check if there is a winner 
def getWinnerHorizontally(board,rows,columns):
    winner = False
    #goes through the rows
    for i in range(rows):
        #goes through columns
        for j in range(columns - 3):
            #if "X" or "O" == the 3 around it you get a win
            if board[i][j] != BLANK and board[i][j] == board[i][j + 1] \
               and board[i][j] == board[i][j + 2] \
               and board[i][j] == board[i][j + 3]:
                winner = True
    
    return winner

# gets the winner vertically
# Input: board, row, and columns, all ints 
# Output: Boolean value winner 
def getWinnerVertically(board,rows,columns):
    winner = False
    #iterates through entire board
    for i in range(rows - 3):
        for j in range(columns):
           #if X or O == the 3 around the spot on the board it equals a win
            if board[i][j] != BLANK \
               and board[i][j] == board[i + 1][j] \
               and board[i][j] == board[i + 2][j] \
               and board[i][j] == board[i + 3][j]:
                winner = True

    return winner


# Gets the winner diagonally 
# Input: board, rows and columns of board
# Output: Boolean value winner
def getWinnerDiagonally(board,rows,columns):
    winner = False
    #checks through board
    for i in range(rows - 3):
        for j in range(columns - 3):
           # checks if the index is the same as the ones around it
            if board[i][j] != BLANK \
               and board[i][j] == board[i + 1][j + 1] \
               and board[i][j] == board[i + 2][j + 2] \
               and board[i][j] == board[i + 3][j + 3]:
                winner = True

        #checks through board
    for i in range(3,rows):
        for j in range(columns - 3):
           # while row - 3 <= rows:
            if board[i][j] != BLANK \
               and board[i][j] == board[i - 1][j + 1] \
               and board[i][j] == board[i - 2][j + 2] \
               and board[i][j] == board[i - 3][j + 3]:
                winner = True



    return winner

# Checks for draw in the game
# Input: the gameBoard
# Output: returns the boolean draw
def checkDraw(board):
    #intialize variables 
    draw = False
    myList = []
    row = 0
    #while the row number is less than the length of board
    while row < len(board):
        col = 0
        while col < len(board[row]):
            myList.append(board[row][col])
            col += 1
        row += 1
    #if "_" is in the list, checks if there is a blank in list
    if BLANK not in myList:
        draw = True

    return draw
# Gets the comptuers choice based on random int
# Input: none
# Output: returns the computers choice
def computerChoice(gameBoard,row,column):
    print("It is now the computer's turn")
    #variable that checks if the cpu is playing
    cpu = True
    col = randint(1,column)

    #checks if there is a full column
    full = validCol(gameBoard,row,column,col,cpu)
    while full == True:
        col = randint(1,column)
        full = validCol(gameBoard,row,column,col,cpu)
    #prints the computer statements
    print()
    
    print("The computer has chosen the column " + str(col))
        
    check = 1
    while gameBoard[row - check][col - 1] != BLANK:
        check += 1
    #puts the X in the correct spot
    gameBoard[row - check][col - 1] = PLAYER2

    #displays board
    displayBoard(gameBoard,row,column)

    
    #winner function calls

    winner = getWinnerHorizontally(gameBoard,row,column)
    winner2 = getWinnerVertically(gameBoard,row,column)
    winner3 = getWinnerDiagonally(gameBoard,row,column)

    #draw function call, goes last
    draw = checkDraw(gameBoard)

    #if there is a winner, prints the computer winns
    winList = []
    winList.append(winner)
    winList.append(winner2)
    winList.append(winner3)
    winList.append(draw)

    return winList


    

# prints the game board
# Input: The gameboard 
# Output: Nothing, just prints the board
def displayBoard(board,rows,columns):
    #just displays the entire board
    for i in range(rows):
        for j in range(columns):
            print(board[i][j], end = " ")
        print()


# Validates the user input
# Input: takes in the rows of the board and the move int 
# Output: returns the move int which correspons with an index
def getValidMove(column,move):
#checks if the move is greater than the row number 
    while move > column:
        print("That is invalid!")
        move = int(input("Enter a column to place your piece in (1-" + str(column) + "): "))

    return move

# Validates that the column is full or not 
# Input: the game board, the amount of rows and the specific column
# Output: a boolean (full), which shows if the column is full or not
def validCol(board,row,column,user,cpu):
    myList = []
    full = False
    check = 1
    #decreases the row number to check if a column is full
    for i in range(row,0,-1):
        myList.append(board[row - check][user - 1])
        check += 1
    #print statement if column is full
    if len(myList) == row and BLANK not in myList:
        if cpu == False:
            print("That column is full")
            full = True
        elif cpu == True:
            full = True
        else:    
            full = False

    return full

# decides whether the user wants to play another game or not
# Input: nothing 
# Output: boolean endgame 
def playAgain():
    #decides whether to end the game or not 
    endGame = False
    #user input on if they want to play again
    play_Again = input("Do you want to play again? (y/n): ")

    #while loop to validate input 
    while play_Again != YES and play_Again != NO:
        print("That is an invalid input")
        play_Again = input("Do you want to play again? (y/n): ")

    #if the user picks no 
    if play_Again == NO:
        endGame = True

    return endGame

def main():
    #loop that determines if the user plays again
    endGame = False

    while endGame == False:
        #variable that helps check for winners
        winner = False
        winner2 = False
        winner3 = False
        draw = False
        cpu = False
        
        print("Welcome to Connect 4!")

    #user inputs height and width
        row = int(input("Enter a height: "))
        column = int(input("Enter a width: "))
        check1 = 1
        check2 = 1

        #checks if the board is the correct size
        while row < MIN_SIZE or column < MIN_SIZE:
            print("The game board must be larger than 4x4")
            row = int(input("Enter a height: "))
            column = int(input("Enter a width: "))

        #asks if user wants to face another player or computer
        user_Choice = input("Play against the computer? (y/n): ")

        #if input is invalid 
        while user_Choice != YES and user_Choice != NO:
            print("That is an invalid input")
            user_Choice = input("Play against the computer? (y/n): ")

        #creates gameboard 
        gameBoard = getBoard(row,column)
        #displays board 
        displayBoard(gameBoard,row,column)


        if user_Choice == YES:
            
            #while the winner boolean is false otherwise there is a winner and game ends
            while winner == False and winner2 == False and winner3 == False \
                  and draw == False:

                cpu = False
                print("Player 1 what is your choice?")

                #gets user choices and checks if it is a valid move
                user_Move = int(input("Enter a column to place your piece in (1-" + \
                            str(column) + "): "))

                user_Move = getValidMove(column,user_Move)

                #checks if user input is in a valid colum
                full = validCol(gameBoard,row,column,user_Move,cpu)

                #if valid column is true then asks user to reinput
                while full == True:
                    user_Move = int(input("Enter a column to place your piece in (1-" + \
                                str(column) + "): "))
                    user_Move = getValidMove(column,user_Move)
                    full = validCol(gameBoard,row,column,user_Move,cpu)

                #check1 is used to determine if there is a chip in the column \
                #if there is, check increases
                check1 = 1
                while gameBoard[row - check1][user_Move - 1] != BLANK:
                    check1 += 1
                #puts the X in the correct spot
                gameBoard[row - check1][user_Move - 1] = PLAYER1

                #displays board
                displayBoard(gameBoard,row,column)
                #winner function calls

                winner = getWinnerHorizontally(gameBoard,row,column)
                winner2 = getWinnerVertically(gameBoard,row,column)
                winner3 = getWinnerDiagonally(gameBoard,row,column)

                #draw function call, goes last
                draw = checkDraw(gameBoard)

                #checks if there is a winner and if the user wants to play again
                if winner == True or winner2 == True or winner3 == True:
                    print("Player 1 wins!! WINNER WINNER CHICKEN DINNER!!")
                    endChoice = playAgain()
                    if endChoice == True:
                        endGame = True

                #checks if there is a draw         
                elif winner == False and winner2 == False \
                     and winner3 == False and draw == True:
                    print("There is a draw, no one wins")
                    endChoice = playAgain()

                    if endChoice == True:
                        endGame = True
                        
                else:
                    cpu = True
                    
                    winList = computerChoice(gameBoard,row,column)
                    #if there is a winner, prints the computer wins
                    #assigns the win list (computer) to the win variables 
                    winner = winList[0]
                    winner2 = winList[1]
                    winner3 = winList[2]
                    draw = winList[3]
                    if winner == True or winner2 == True or winner3 == True:
                        print("The Computer Wins!! WINNER WINNER CHICKEN DINNER!!")
                        #asks if user wants to play again
                        endChoice = playAgain()

                        if endChoice == True:
                            print("hello")
                            endGame = True

                    #if there is a draw, then it asks if user wants to play again        
                    elif winner == False and winner2 == False \
                         and winner3 == False and draw  == True:
                        print("There is a draw, no one wins")
                        endChoice = playAgain()

                        if endChoice == True:
                            endGame = True

                   
            
        #if the user chose to play against another player
        elif user_Choice == NO:

            #while the winner boolean is false otherwise there is a winner and game ends
            while winner == False and winner2 == False and winner3 == False and draw == False :
                print("Player 1 what is your choice?")

                #gets user choices and checks if it is a valid move
                user_Move = int(input("Enter a column to place your piece in (1-" + \
                            str(column) + "): "))
            
                user_Move = getValidMove(column,user_Move)
                #checks if user input is in a valid colum
                full = validCol(gameBoard,row,column,user_Move,cpu)
                #if valid column is true then asks user to reinput 
                while full == True:
                    user_Move = int(input("Enter a column to place your piece in (1-" + \
                                str(column) + "): "))
                    user_Move = getValidMove(column,user_Move)
                    full = validCol(gameBoard,row,column,user_Move,cpu)
                #check1 is used to determine if there is a chip in the column \
                #if there is, check increases 
                check1 = 1
                while gameBoard[row - check1][user_Move - 1] != BLANK:
                    check1 += 1
                #puts the X in the correct spot
                gameBoard[row - check1][user_Move - 1] = PLAYER1

                #displays board 
                displayBoard(gameBoard,row,column)
                #winner function calls

                winner = getWinnerHorizontally(gameBoard,row,column)
                winner2 = getWinnerVertically(gameBoard,row,column)
                winner3 = getWinnerDiagonally(gameBoard,row,column)

                #draw function call, goes last
                draw = checkDraw(gameBoard)

                #win statements, if there is a winner
                #and asks the user if they want to play again
                if winner == True or winner2 == True or winner3 == True:
                    print("Player 1 wins!! WINNER WINNER CHICKEN DINNER!!")
                    endChoice = playAgain()
                    if endChoice == True:
                        endGame = True

                #if there is a draw then prints
                #asks user if they want to play again
                elif winner == False and winner2 == False \
                     and winner3 == False and draw == True:
                    print("There is a draw, no one wins")
                    endChoice = playAgain()
                    if endChoice == True:
                        endGame = True
                    
                else:
                #player 2 turn 
                    print("Player 2 what is your choice?")
                #user input
                    user_Move = int(input("Enter a column to place your piece in (1-" + \
                                str(column) + "): "))
                #validates the move
                    user_Move = getValidMove(column,user_Move)
                #validates the column
                    full = validCol(gameBoard,row,column,user_Move,cpu)
                #if the column is full then it asks user to re input

                    while full == True:
                        user_Move = int(input("Enter a column to place your piece in (1-" +\
                                    str(column) + "): "))
                        user_Move = getValidMove(column,user_Move)
                        full = validCol(gameBoard,row,column,user_Move,cpu)
                #check 2 is used to determine if the spot is open in the correct column
                    check2 = 1

                    while gameBoard[row - check2][user_Move - 1] != BLANK:
                        check2 += 1
                #puts O in the correct spot
                    gameBoard[row - check2][user_Move - 1] = PLAYER2
                #updates the game board 
                    displayBoard(gameBoard,row,column)

                    #win functions
                    winner = getWinnerHorizontally(gameBoard,row,column)
                    winner2 = getWinnerVertically(gameBoard,row,column)
                    winner3 = getWinnerDiagonally(gameBoard,row,column)
                    
                    draw = checkDraw(gameBoard)
                    
               #if there is a winner prints the statement
                    if winner == True or winner2 == True or winner3 == True:
                        print("Player 2 wins!! WINNER WINNER CHICKEN DINNER!!")
                        endChoice = playAgain()
                        if endChoice == True:
                            endGame = True

                    #if there is a draw, then asks the user if they want to play again
                    elif winner == False and winner2 == False \
                         and winner3 == False and draw == True:
                        print("There is a draw, no one wins")
                        endChoice = playAgain()
                        if endChoice == True:
                            endGame = True

        #if endGame is true then print this 
        if endGame == True:
            print()
            print("Thanks for playing")
            
        
        
        

main()
