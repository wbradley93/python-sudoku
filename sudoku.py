"""
Python Sudoku
Author: Wes Bradley
Last Modified: 31 October 2016

Generates standard sudoku boards according to method outlined in generator.pdf
"""
from random import randrange
from backtrack import solve
from time import sleep

def randomVal():
    return randrange(1, 10)

def randomPlace():
    return (randrange(9) for _ in range(2))

def validMove(b, r, c, v):
    return not (v in b[r] or v in (i[c] for i in b) or \
        any(v in k for k in [j[3 * (c//3):3 * (c//3) + 3] for j in b[3 * (r//3):3 * (r//3) + 3]]))

def generateBoard():
    board = [[0 for _ in range(9)] for _ in range(9)]

    for _ in range(11):
        while True:
            row, col = randomPlace()
            val = randomVal()
            if validMove(board, row, col, val):
                break
        board[row][col] = val

    solve(board, 0)
    print(digHoles(board))
    return board

def printBoard(b):
    hLine = "-" * 37
    print(hLine)
    for i in range(9):
        line = "|"
        for j in range(9):
            line += " " + str(b[i][j]) + " |"
        print(line)
        print(hLine)


def digHoles(b):
    pBoard = [[True for _ in range(9)] for _ in range(9)]
    pRange = [i for i in range(81)]
    n = pRange.pop(randrange(len(pRange)))
    r = n//9
    c = n%9

    return pBoard, pRange, n, r, c

def sudoku():
    print("\nWelcome to sudoku. Enter one of the following options:")
    print("To play a new game, enter 'n'.")
    print("To replay the last board, enter 'l'.")
    print("To quit, enter 'q'.")
    mSelect = input("Make your selection: ")

    if mSelect == 'n':
        board = generateBoard()
        printBoard(board)
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
