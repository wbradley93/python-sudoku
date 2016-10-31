"""
Python Sudoku
Author: Wes Bradley
Last Modified: 31 October 2016

Terminal implementation of sudoku game.
Usage: sudoku()

TODO: validate inputs during game, allow user to quit back to main menu, implement
        mid-game board reset, color 3x3 blocks in board, clear and reprint terminal
        with each turn (curses), implement cursor, implement correctness check,
        implement animated solver, implement game timer and leaderboard
maybe TODO: save records of games, allow boards to be loaded and replayed, or 
        previous games to be watched
"""
from board import Board
from backtrack import validMove
    
def startGame(b):
    print(b)
    while b.board != b.getSolution():
        c, r, v = [int(x) for x in input("Enter the value v to put at row r, column c as 'c,r,v': ").split(',')]
        if b.getInitialBoard()[r][c] == 0 and validMove(b.board, r, c, v):
            b.board[r][c] = v
            print(b)
            if b.board == b.getSolution():
                print("Congratulations! You solved it!")
                return
        else:
            print("That was not a valid move. Try again.")

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
        startGame(board)
        sudoku()
    elif mSelect == 'l':
        if 'board' in locals():
            board.resetBoard()
            startGame(board)
            sudoku()
        else:
            print("\nYou haven't yet played a game.")
            sudoku()
    elif mSelect == 'q':
        return
    else:
        print()
        print("That was not a valid selection.")
        sudoku()
