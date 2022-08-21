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
        if board[i].count('X') == 3 or board[i].count('O') == 3:
            if board[i][i] == 'X':
                return X
            else:
                return O

    # Check columns
    columns = []
    for i in range(3):
        columns.append([board[0][i], board[1][i], board[2][i]])
    for i in range(3):
        if columns[i].count('X') == 3 or columns[i].count('O') == 3:
            if columns[i][i] == 'X':
                return X
            else:
                return O

    # Check diagonally
    diagonals = []
    diagonals.append([board[0][0], board[1][1], board[2][2]])
    diagonals.append([board[0][2], board[1][1], board[2][0]])
    for i in range(2):
        if diagonals[i].count('X') == 3 or diagonals[i].count('O') == 3:
            if columns[i][i] == 'X':
                return X
            else:
                return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False

    else:
        return True


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

# My own function
def minValue(board):
    """
    Returns min value for a state
    """
    if terminal(board):
        return utility(board)

    minEval = math.inf
    for action in actions(board):
        if minEval != min(minEval, maxValue(result(board, action))):
            minEval = maxValue(result(board, action))
    return minEval

# My own function!
def maxValue(board):
    """
    Returns min value for a state
    """
    if terminal(board):
        return utility(board)

    maxEval = -math.inf
    for action in actions(board):
        if maxEval != max(maxEval, minValue(result(board, action))):
            maxEval = minValue(result(board, action))

    return maxEval

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        maxVal = -math.inf
        bestAction = tuple()

        for action in actions(board):
            if maxVal < max(maxVal, minValue(result(board, action))):
                maxVal = minValue(result(board, action))
                bestAction = action
        return bestAction

    if current_player == O:
        minVal = math.inf
        bestAction = tuple()

        for action in actions(board):
            if minVal > min(minVal, maxValue(result(board, action))):
                minVal = maxValue(result(board, action))
                bestAction = action
        return bestAction