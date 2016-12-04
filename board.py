"""
Sudoku Board Class
Author: Wes Bradley
Last Modified: 5 December 2016

Defines sudoku board class and related methods
"""

from copy import deepcopy
from backtrack import solve
from digger import randomDig
from random import randrange
from helpers import validMove

def generateSolvedBoard():
    # 9x9 matrix of 0's
    board = [[0 for _ in range(9)] for _ in range(9)]

    # pick 11 random places, places random valid numbers there
    for _ in range(11):
        while True:
            row, col = (randrange(9) for _ in range(2))
            val = randrange(1, 10)
            if validMove(board, row, col, val):
                break
        board[row][col] = val

    # solve the rest of the board
    solve(board)
    return board

class Board(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.solvedState = generateSolvedBoard()
        self.initialState = randomDig(deepcopy(self.solvedState), self.difficulty)
        self.state = deepcopy(self.initialState)
        
    def setState(self, state):
        self.state = deepcopy(state)
        
    def resetState(self):
        self.setState(self.initialState)
        
    def getDifficulty(self):
        return self.difficulty
        
    def getInitialState(self):
        return self.initialState
        
    def getCurrentState(self):
        return self.state
        
    def getSolvedState(self):
        return self.solvedState
        
    def setValue(self, c, r, v):
        self.state[r][c] = v
        
    def isValidMove(self, c, r, v):
        # if space isn't given and number doesn't break rule
        return self.initialState[r][c] == 0 and validMove(self.state, r, c, v)

    def __str__(self):
        hLine = "  " + "-" * 37 + "\n"
        out = hLine 
        for i in range(9):
            line = str(i+1) + " |"
            for j in range(9):
                line += " " + (" " if self.state[i][j] is 0 else str(self.state[i][j])) + " |"
            out += line + "\n"
            out += hLine
        out += "    1   2   3   4   5   6   7   8   9"
        return out