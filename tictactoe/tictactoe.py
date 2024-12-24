"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    if terminal(board):
        return False
    countx = 0
    counto = 0
    for i in board:
        countx+=i.count(X)
        counto+=i.count(O)
    
    if countx <= counto:
        return X
    elif countx > counto:
        return O
    
def actions(board):
    act = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                act.add((i,j))
    return act


def result(board , action):
    
    if action not in actions(board):
        raise Exception
    temp = copy.deepcopy(board)
    temp[action[0]][action[1]] = player(board)
    
    return temp

def winner(board):
    if (board[0][0], board[1][1], board[2][2]) == (X,X,X) or (board[2][0], board[1][1], board[0][2]) == (X,X,X):
        return X
    if (board[0][0], board[1][1], board[2][2]) == (O,O,O) or (board[2][0], board[1][1], board[0][2]) == (O,O,O):
        return O
    for i in range(len(board)):
        if board[i] == [X,X,X]:
            return X
        elif board[i] == [O,O,O]:
            return O
    for i in range(len(board)):
        if [board[0][i] , board[1][i] , board[2][i]] == [X,X,X]:
            return X
        if [board[0][i] , board[1][i] , board[2][i]] == [O,O,O]:
            return O
            
        
    return None

def terminal(board):
    if winner(board):
        return True
    else: # Check if all blocks filled or nah
        count = 0
        for i in board:
            if i.count(EMPTY) != 0:
                return False
        return True

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -999
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v
        
def min_value(board):
    if terminal(board):
        return utility(board)

    v = 9999
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v
        
def minimax(board):
    if terminal(board):
        return None
    
    act = None
    
    if player(board) == X:
        v = -999
        for i in actions(board):
            var = max_value(result(board,i))
            if v < var:
                v = var
                act = i
    
    else:
        v = 999
        for i in actions(board):
            var = min_value(result(board,i))
            if v > var:
                v = var
                act = i
    return act
    
