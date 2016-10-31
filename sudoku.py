"""
Python Sudoku
Author: Wes Bradley
Last Modified: 31 October 2016

Terminal implementation of sudoku game.
Usage: sudoku()
"""
from board import Board
    
def sudoku():
    print("\nWelcome to sudoku. Enter one of the following options:")
    print("To play a new game, enter 'n'.")
    print("To replay the last board, enter 'l'.")
    print("To quit, enter 'q'.\n")
    mSelect = input("Make your selection: ")

    if mSelect == 'n':
        dif = input("Choose a difficulty level from 0 (extremely easy) to 4 (evil): ")
        while not dif.isnumeric() or int(dif) not in range(5):
            dif = input("That was not a valid difficulty level. Try again: ")
        board = Board(int(dif))
        print(board)
    elif mSelect == 'l':
        if 'board' not in locals():
            print("\nYou haven't yet played a game.")
            sudoku()
    elif mSelect == 'q':
        return
    else:
        print()
        print("That was not a valid selection.")
        sudoku()
