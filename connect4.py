##########################################                                 CONNECT 4                                    ###################################################
#                                                                                                                                                                         #
#       If you are not farmiliar with the rules of connect 4 you can go here: https://www.officialgamerules.org/board-games/connect-4                                     #
#       If you want to be weird and use unicode symbols for the pieces you can go here: https://unicode-explorer.com/list/geometric-shapes                                #
#       That'll make it slightly harder to determine which is whose piece but you do you                                                                                  #
#                                                                                                                                                                         #
########################################################################################################################################################################### 

def print_board(board):
    '''
    This function will take in a board state and then print it in a human-legible format. Make sure that you use distinguishable characters for each player
    and that the coloumns and rows are displayed correctly

    Parameters:
        board: A 2d (6 rows x 7 coloumns) list (of lists) which represents a certain state of the board
               values of 1 represent player 1's piecces, a value of -1 represents player 2's and 0 represents empty
    Returns:
        None
    '''
    
    ## TODO Implement a print of the 2d array with unique characters for each player 
    ############################################

    for row in board:
        print_row(row)

    print("---------------------")
    print(" 1  2  3  4  5  6  7  ")


    ############################################

    return None

def print_row(row):
    str = ""
    for elem in row:
        if elem == 1:
            str += "[X]"
        elif elem == -1:
            str += "[O]"
        elif elem == 0:
            str += "[ ]"
    print(str)

def n_in_a_row(board, row, col, dir=(0,1), n=4):

    end_loc = (row+(n*dir[0]), col+(n*dir[1]))

    if end_loc[0] > 6 or end_loc[0] < 0 or end_loc[1] > 6 or end_loc[1] < 0:
        return False

    if n <= 1:
        return True

    match_next = board[row][col] == board[row+dir[0]][col+(dir[1])]

    if n <= 2:
        return match_next
    
    else:
        return match_next and n_in_a_row(board, row+dir[0], col+(dir[1]), dir=dir, n=n-1)

def game_over(board, row, col):
    '''
    Parameters:
        board: A 2d (6x7) list (of lists) which represents a certain state of the board
               values of 1 represent player 1's piecces, a value of -1 represents player 2's and 0 represents empty
    Returns:
        winner: An int representing who won if anyone. It should have the value 1 if Player 1 won, -1 for Player 2
                And 0 if neither player has won yet 
    '''

    ## TODO Implement check of a 4 in a row
    ############################################

    for x in [-1, 0, 1]:
        for y in [-1,0,1]:
            if not (x == 0 and y == 0):
                if n_in_a_row(board, row, col, (x,y), n=4):
                    return board[row][col]


    ############################################

    return False


def valid_move(board, col):
    '''
    Parameters:
        board: A 2d (6x7) list (of lists) which represents a certain state of the board
               values of 1 represent player 1's piecces, a value of -1 represents player 2's and 0 represents empty
        col: The coloumn being played in 
    Returns:
        valid: A boolean representing whether this was a valid move 
    '''
        
        
    ## TODO Implement check of a full coloumn
    ############################################

    if board[0][col] != 0:
        return False
    else:
        return True


    ############################################

def move(board, player):
    '''
    This function should ask the current player which move they'd like to make and then implement it if possible, else
    ask them to give a different move

    Parameters:
        board: A 2d (6x7) list (of lists) which represents a certain state of the board
               values of 1 represent player 1's piecces, a value of -1 represents player 2's and 0 represents empty
        player: An Int representing the player (Player 1 -> 1, Player 2 -> -1)
    Returns:
        new_board: A 2d list representing the updated board after making the move
    '''
        
    ## TODO Implement a move (with check)
    ############################################
    col_choice = int(input("which col would you like to play in?")) - 1
    while not valid_move(board, col_choice):
        col_choice = input("Not a valid move, which col would you like to play in?")
    
    for i in range(6):
        if i == 5 or board[i+1][col_choice] != 0 :
            board[i][col_choice] = player
            break

    ############################################
        
    return board, (i, col_choice)

def play_game():
    '''
    This function has no input or output, but will run through the full game and print out the board after each move
    It should also print out a congrats message to whichever player won

    It should swap between players and make checks each move to see if the game is over

    '''

    ## TODO The full game (using all previous functions)
    ############################################

    player = 1

    board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    while True:
        print_board(board)
        print("Player", (player+3)%3, "("+("X" if player==1 else "O")+")", "your turn" )
        board, (row, col) = move(board, player)
        winner = game_over(board, row, col)
        if winner != 0:
            print_board(board)
            print("CONGRATS PLAYER", int((winner+3)%3), "! YOU WIN BECAUSE PLAYER", int(((winner*-1)+3)%3), "SUCKS!")
            return winner
        player *= -1
        
        

    ############################################

play_game()