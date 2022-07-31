"""
Tic Tac Toe Player
"""
import copy
import math

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
    """
    Returns player who has the next turn on a board.
    """
    sumX = 0
    sumO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                sumX += 1
            if board[i][j] == O:
                sumO += 1
    if sumX > sumO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    i = action[0]
    j = action[1]
    currentPlayer = player(newBoard)

    if newBoard[i][j] != EMPTY:
        raise Exception

    else:
        newBoard[i][j] = currentPlayer

    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for i in range(3):
        if board[i].count(X) or board[i].count(O) == 3:
            return board[i][i]

    # Check columns
    columns = []
    for i in range(3):
        columns.append([board[i][0], board[i][1], board[i][2]])
    for i in range(3):
        if columns[i].count(X) or columns[i].count(O) == 3:
            return columns[i][i]

    # Check diagonally
    diagonals = []
    diagonals.append([board[0][0], board[1][1], board[2][2]])
    diagonals.append([board[0][2], board[1][1], board[2][0]])
    for i in range(2):
        if diagonals.count(X) or diagonals.count(O) == 3:
            return diagonals[i][i]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    elif EMPTY not in board:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

