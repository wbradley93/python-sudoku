"""
Python Sudoku
Author: Wes Bradley
Last Modified: 3 December 2016

Terminal implementation of sudoku game.
Usage: sudoku()

TODO: color 3x3 blocks in board, clear and reprint terminal
        with each turn (curses), implement cursor, implement correctness check,
        implement animated solver, implement game timer and leaderboard
maybe TODO: save logs of games, allow boards to be loaded and replayed, or 
        previous games to be watched
"""
from board import Board

def getInput(d):
    while True:
        prompt = "To make a move, enter the value v to put at row r, column c as 'c r v'\n"
        if d:
            prompt += "To reset the board, enter 'reset'\n"
        prompt += "To return to the main menu, enter 'main'\n"
        prompt += "Make your selection: "
        inParams = input(prompt)
        if inParams == 'main' or (inParams == 'reset' and d): 
            return inParams
        else:
            inParams = inParams.split(' ')
            if len(inParams) == 3 and all((i.isnumeric() and int(i) in range(1,10)) for i in inParams):
                for i in range(3):
                    inParams[i] = int(inParams[i])
                    if i != 2:
                        inParams[i] -= 1
                return inParams
            else:
                print("That input was not valid. Try again.")
    
def startGame(b):
    print(b)
    while b.getCurrentState() != b.getSolvedState():
        diff = b.getCurrentState() != b.getInitialState()
        i = getInput(diff)
        if i == 'main':
            return
        elif i == 'reset':
            b.resetState()
            print(b)
        else:
            if b.isValidMove(*i):
                b.setValue(*i)
                print(b)
            else:
                print("That was not a valid move. Try again.")
    print("Congratulations! You solved it!")

def sudoku():
    while True:
        print("\nWelcome to sudoku. Enter one of the following options:")
        print("To play a new game, enter 'new'.")
        if 'board' in locals():
            print("To continue your current game, enter 'continue'.")
            if board.getCurrentState() != board.getInitialState():
                print("To restart the last board, enter 'restart'.")
        print("To quit, enter 'quit'.\n")
        mSelect = input("Make your selection: ")
    
        if mSelect == 'new':
            dif = input("Choose a difficulty level from 0 (extremely easy) to 4 (evil): ")
            while not dif.isnumeric() or int(dif) not in range(5):
                dif = input("That was not a valid difficulty level. Try again: ")
            board = Board(int(dif))
            startGame(board)
        elif mSelect == 'continue':
            if 'board' in locals():
                startGame(board)
            else:
                print("\nYou don't have an active game.")
        elif mSelect == 'restart':
            if 'board' in locals():
                board.resetState()
                startGame(board)
            else:
                print("\nYou haven't yet played a game.")
        elif mSelect == 'quit':
            break
        else:
            print()
            print("That was not a valid selection.")
