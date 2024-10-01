def initialize():
    # sets up the initial chess board
    initial = [
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'], 
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
    ]
    return initial

def printBoard(board):
    # prints out the chess board
    columns = ['  a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h ']
    print("   " + " ".join(columns)) 
    for i, row in enumerate(board):
        row_str = " ".join(f"{piece:>3}" for piece in row)
        print(f"{8 - i}  {row_str}  {8 - i}") 
    print("   " + " ".join(columns))

def cPawnMove(board, origin, dest):
    # checks if pawn move is valid
    rOrig, cOrig = origin
    rDest, cDest = dest
    piece = board[rOrig][cOrig]

    if piece[0] == 'W':  # white pawn
        if (rDest == rOrig - 1) and (cDest == cOrig):
            return board[rDest][cDest] == '--'
        if (rOrig == 6) and (rDest == 4) and (cDest == cOrig):
            return board[5][cOrig] == '--' and board[rDest][cDest] == '--'
        if (rDest == rOrig - 1) and (abs(cDest - cOrig) == 1):
            return board[rDest][cDest][0] == 'B'
    elif piece[0] == 'B':  # black pawn
        if (rDest == rOrig + 1) and (cDest == cOrig):
            return board[rDest][cDest] == '--'
        if (rOrig == 1) and (rDest == 3) and (cDest == cOrig):
            return board[2][cOrig] == '--' and board[rDest][cDest] == '--'
        if (rDest == rOrig + 1) and (abs(cDest - cOrig) == 1):
            return board[rDest][cDest][0] == 'W'
        
    return False

def cKnightMove(board, origin, dest):
    # checks if knight move is valid
    if (abs(origin[0] - dest[0]) == 2 and abs(origin[1] - dest[1]) == 1) or \
       (abs(origin[0] - dest[0]) == 1 and abs(origin[1] - dest[1]) == 2):
        return True
    return False

def cBishopMove(board, origin, dest):
    # checks if bishop move is valid
    if abs(origin[0] - dest[0]) == abs(origin[1] - dest[1]):
        rStep = 1 if dest[0] > origin[0] else -1
        cStep = 1 if dest[1] > origin[1] else -1

        row, col = origin[0] + rStep, origin[1] + cStep
        while (row, col) != dest:
            if board[row][col] != '--':
                return False  # another piece currently blocking spot
            row += rStep
            col += cStep
        return True
    return False

def cRookMove(board, origin, dest):
    # checks if rook move is valid
    if origin[0] == dest[0] or origin[1] == dest[1]:
        rStep = 0 if origin[0] == dest[0] else (1 if dest[0] > origin[0] else -1)
        cStep = 0 if origin[1] == dest[1] else (1 if dest[1] > origin[1] else -1)

        row, col = origin[0] + rStep, origin[1] + cStep
        while (row, col) != dest:
            if board[row][col] != '--':
                return False  # another piece currently blocking spot
            row += rStep
            col += cStep
        return True
    return False

def cQueenMove(board, origin, dest):
    # checks if queen move is valid
    return cRookMove(board, origin, dest) or cBishopMove(board, origin, dest)

def cKingMove(origin, dest):
    # checks if king move is valid
    return max(abs(origin[0] - dest[0]), abs(origin[1] - dest[1])) == 1

def valid(board, player, origin, dest):
    # checks if indices are valid
    if not (0 <= origin[0] < 8 and 0 <= origin[1] < 8 and 0 <= dest[0] < 8 and 0 <= dest[1] < 8):
        return False

    piece = board[origin[0]][origin[1]]
    if piece == '--' or (player == 1 and piece[0] == 'B') or (player == -1 and piece[0] == 'W'):
        return False

    # checks specific piece move validity 
    if piece[1] == 'P':  # pawn
        return cPawnMove(board, origin, dest)
    elif piece[1] == 'K':  # king
        return cKingMove(origin, dest)
    elif piece[1] == 'Q':  # queen
        return cQueenMove(board, origin, dest)
    elif piece[1] == 'R':  # rook
        return cRookMove(board, origin, dest)
    elif piece[1] == 'B':  # bishop
        return cBishopMove(board, origin, dest)
    elif piece[1] == 'N':  # knight
        return cKnightMove(board, origin, dest)

    return False

def move(board, player, origin, dest):
    # moves piece if valid
    if valid(board, player, origin, dest):
        board[dest[0]][dest[1]] = board[origin[0]][origin[1]]  # moves the piece
        board[origin[0]][origin[1]] = '--'  # clears the original piece position 
    else:
        raise ValueError("invalid move")
    
    return board

def inDanger(board, kingPos, player):
    # checks if king is under attack
    opponent = -player
    for r in range(8):
        for c in range(8):
            if board[r][c][0] == ('W' if opponent == 1 else 'B') and valid(board, opponent, (r, c), kingPos):
                return True
    return False

def inCheck(board):
    # checks if player is currently in check
    kingsPos = [(0, 4), (7, 4)]  # positions of the kings
    for i, pos in enumerate(kingsPos):
        if inDanger(board, pos, -1 if i == 0 else 1):
            return 1 if i == 0 else -1  # returns 1 if player 1 is in check, -1 if player 2 is in check
    return 0  # no player currently in check

def check(board):
    # checks checkmate status
    checkStatus = inCheck(board)
    if checkStatus == 0:
        return 0  # no one is currently in check

    pColor = 'W' if checkStatus == 1 else 'B'
    pMove = -1 if checkStatus == 1 else 1

    for r in range(8):
        for c in range(8):
            if board[r][c][0] == pColor:
                for newR in range(8):
                    for newC in range(8):
                        if valid(board, pMove, (r, c), (newR, newC)):
                            return 0  # player can move
    return checkStatus  # returns 1 if player 1 checkmate, -1 if player 2 checkmate

def play():
    board = initialize()
    printBoard(board)
    player = 1  # player 1 is white
    
    while True:
        try:
            if check(board) != 0:
                winner = "player 1" if check(board) == -1 else "player 2"
                print(f"checkmate! {winner} wins!")
                break

            move_input = input(f"PLAYER {1 if player == 1 else 2} enter your move (ex. 'e2 e4'): ")
            origin_str, dest_str = move_input.split()
            origin = (8 - int(origin_str[1]), ord(origin_str[0]) - ord('a'))  # converts to (row, col)
            dest = (8 - int(dest_str[1]), ord(dest_str[0]) - ord('a'))  # converts to (row, col)

            move(board, player, origin, dest)
            printBoard(board)

            # switch player
            player = -player

        except ValueError as e:
            print(e)
        except IndexError:
            print("invalid move")

play()