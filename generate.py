"""
Sudoku Board Generator
Author: Wes Bradley
Last Modified: 31 October 2016

Generates solved sudoku boards according to method outlined in generator.pdf
"""

from random import randrange
from backtrack import validMove, solve
from digger import digHoles
from copy import deepcopy

def randomVal():
    return randrange(1, 10)

def randomPlace():
    return (randrange(9) for _ in range(2))

def generateBoard(dif):
    board = [[0 for _ in range(9)] for _ in range(9)]

    for _ in range(11):
        while True:
            row, col = randomPlace()
            val = randomVal()
            if validMove(board, row, col, val):
                break
        board[row][col] = val

    solve(board, 0)
    solution = deepcopy(board)
    digHoles(board, dif)
    return solution, board