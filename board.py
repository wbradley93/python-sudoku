"""
Sudoku Board Class
Author: Wes Bradley
Last Modified: 3 December 2016

Defines sudoku board class and related methods
"""

from copy import deepcopy
from backtrack import solve
from digger import digHoles
import helpers as h

def generateSolvedBoard(dif):
    board = [[0 for _ in range(9)] for _ in range(9)]

    for _ in range(11):
        while True:
            row, col = h.randomPlace()
            val = h.randomVal()
            if h.validMove(board, row, col, val):
                break
        board[row][col] = val

    solve(board, 0)
    return board

class Board(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.solvedState = generateSolvedBoard(self.difficulty)
        self.initialState = digHoles(deepcopy(self.solvedState), self.difficulty)
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
        return self.initialState[r][c] == 0 and h.validMove(self.state, r, c, v)

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