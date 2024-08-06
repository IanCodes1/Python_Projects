# File: Project2.py
# Student: Ian Salinas
# UT EID: ibs325
# Course: CS303E
# 
# Date: 11/07/2022
# Description of Progr9,2am: Program simulates a game of Tic-Tac-Toe and allows the user to play the game against a bot.


import random

# Some global constants:

HUMAN   = 0
MACHINE = 1

WELCOME = "Welcome to our Tic-Tac-Toe game! \nPlease begin playing."
YOU_WON  = "Congratulations! You won!\n"
YOU_LOST = "Sorry!  You lost!\n"
YOU_TIED = "Looks like a tie.  Better luck next time!\n"

def initialBoard():
    return  [ [" ", " ", " "], \
              [" ", " ", " "], \
              [" ", " ", " "] ]

class TicTacToe:
    def __init__(self):
        # Initialize the game with the board and current player
        self.__player = 0
        self.__board = initialBoard()

    def __str__(self):
        # Return a string representation of the board.
        return self.__board[0][0]+"|" + self.__board[0][1]+"|" + self.__board[0][2]+ "\n-----\n" + self.__board[1][0] + "|" + \
            self.__board[1][1] + "|" + self.__board[1][2] + "\n-----\n" + self.__board[2][0] + "|" + \
            self.__board[2][1] + "|" + self.__board[2][2]
    def getPlayer( self ):
        # Return the current player.
        return self.__player

    def isWin( self ):
        # See if the board represents a win for the current
        # player. A win is three of the current player's tokens
        # in a single row, column, or either diagonal.
        for i in range(0,3):
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] != " ":
                return YOU_WON
            elif self.__board[0][i] == self.__board[1][i] == self.__board[2][i] != " ":
                return True
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != " " \
            or self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != " ":
            return True

    def swapPlayers( self ):
        # Change the current player from HUMAN to MACHINE or
        # vice versa.
        if self.__player == 0:
            self.__player = 1
        else: self.__player = 0
        return

    def humanMove( self ):
        # Ask the HUMAN to specify a move.  Check that it's 
        # valid (syntactically, in range, and the space is 
        # not occupied).  Update the board appropriately.
        print()
        print("Your turn:")

        while True:
            atStart = input("  Specify a move r, c: ")
            print()
            if not "," in atStart:
                print("Response should be r, c. Try again!")
                
            else:
                r , c = atStart.split(",")
                r = int(r)
                c = int(c.lstrip())
                if ( r < 0 or r > 2 or c > 2 or c < 0):
                    print("Illegal move specified.  Try again!")
                    continue
                if ( 0 <= r <= 2 )and ( 0 <= c <= 2 ):
                    if self.__board[r][c] == " ":
                        self.__board[r][c] = "X"
                        return
                    else:
                        print("Illegal move specified.  Try again!")

    def machineMove( self ):
            # This is the MACHINE's move.  It picks squares randomly
            # until it finds an empty one. Update the board appropriately.
            # Note: this is a really dumb way to play tic-tac-toe.  
            print()
            print("Machine's turn:")
            while True:
                r = random.randint(0, 2)
                c = random.randint(0, 2)
                if self.__board[r][c] == " ":
                    print("  Machine chooses: ", r, ", ", c, sep="")
                    print()
                    self.__board[r][c] = "O"
                    return

def driver( ):
        """ This plays tic-tac-toe in a pretty simple-minded
        fashion.  The human player goes first with token "X" and
        alternates with the machine using token "O".  We print
        the board before the first move and after each move. """

        # Print the welcome message
        print( WELCOME )

        # Initialize the board and current player
        ttt = TicTacToe()
        print( ttt )

        # There are up to 9 moves in tic-tac-toe.
        for move in range(9):
            # The current player may be HUMAN
            # or MACHINE
            if ttt.getPlayer() == HUMAN:
                # If HUMAN, take a move, print the board,
                # and see if it's a win.
                ttt.humanMove()
                print( ttt )
                if ttt.isWin():
                    print()
                    print( YOU_WON )
                    return

            else:
                # Else MACHINE takes a move.  Print the
                # board and see if the machine won.
                ttt.machineMove()
                print( ttt )
                if ttt.isWin():
                    print()
                    print( YOU_LOST )
                    return

            # Swap players.
            ttt.swapPlayers()

        # After nine moves with no winner, it's a tie.
        print( YOU_TIED )
        
driver()