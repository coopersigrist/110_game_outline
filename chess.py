##########################################                                      CHESS                                   ###################################################
#                                                                                                                                                                         #
#       If you are not farmiliar with the rules of chess you can go here: https://en.wikipedia.org/wiki/Rules_of_chess                                                    #
#       If you want to be weird and use unicode symbols for the pieces you can go here: https://altcodeunicode.com/alt-codes-chess-symbols/                               #
#       That'll make it slightly harder to determine which is whose piece but you do you                                                                                  #
#                                                                                                                                                                         #
########################################################################################################################################################################### 

def initialize_board():
    '''
    This function takes no input and returns a board which represents the initial state of a game of chess
    You should use whatever strings you decide for the pieces (and ownership) but you must be consistent!

    I recommend using characters for each piece (Kn = knight, P = Pawn, etc..) and appending that on W or B, for which player it is
    I.e. WKn is a White Knight, WK would be the white king, BP is a black pawn, etc.
    '''

    ## TODO assign the elements of initial_board to represent the initial state of a chess game
    ############################################



    ############################################    


    return initial_board

def print_board(baord):
    '''
    This function will take in a board state and then print it in a human-legible format. Make sure that you use distinguishable characters for each player
    and that the coloumns and rows are displayed correctly

    Parameters:
        board: A 2d (8 rows x 8 coloumns) list (of lists) which represents a certain state of the board,
               using your chosen notation for piece id and ownership
    Returns:
        None
    '''
    
    ## TODO Implement a print of the 2d array with unique characters for each piece
    ############################################



    ############################################


    return None

def any_check(board):
    '''
    This function will check to see if any piece is currently able to move to it's enemies king

    Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
               Each spot should have a string representing which piece is in that spot and which player owns it
    Returns:
        winner: An int representing who is in check if anyone. It should have the value 1 if Player 1 is, -1 for Player 2 is
                And 0 if neither player is in check at the moment 
    '''

    ## TODO Implement check of a check mate
    ############################################



    ############################################

    return winner


def valid_move(board, player, origin=(0,0), destination=(0,2)):
    '''
    Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
        player: An Int representing the player (Player 1 -> 1, Player 2 -> -1)
        origin: a pair of indeces (ints) representing a location on the board (0,0 would represent row 0, col 0 for example). We will try to move the piece that is at this location currently
        desination: another pair of indeces (ints) representing a location on the board. This is the location we will try to move our piece to.
    Returns:
        valid: A boolean representing whether this was a valid move 
    '''
        
        
    ## TODO Implement check of a valid move (This must abide by chess rules particularly check)
    # Some difficulties will be: Pawns being able to move 2 on their first move, Pieces not being able to move through other pieces,
    # needing to block check, Taking enemy pieces but not your own, etc.
    ############################################



    ############################################
    
    return valid

def move(board, player, origin=(0,0), destination=(0,2)):
    '''
    This function should ask the current player which move they'd like to make and then implement it if possible, else
    ask them to give a different move

   Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
        player: An Int representing the player (Player 1 -> 1, Player 2 -> -1)
        origin: a pair of indeces (ints) representing a location on the board (0,0 would represent row 0, col 0 for example). We will try to move the piece that is at this location currently
        desination: another pair of indeces (ints) representing a location on the board. This is the location we will try to move our piece to.
    Returns:
        new_board: A 2d list representing the updated board after making the move
    '''
        
    ## TODO Implement a move (with check)
    ############################################



    ############################################
        
    return new_board


def any_check_mate(board):
    '''
    Parameters:
        board: A 2d (8x8) list (of lists) which represents a certain state of the board
               Each spot should have a string representing which piece is in that spot and which player owns it
    Returns:
        winner: An int representing who won if anyone. It should have the value 1 if Player 1 won, -1 for Player 2
                And 0 if neither player has won yet 
    '''

    ## TODO Implement check of a check mate
    ############################################



    ############################################

    return winner

def play_game():
    '''
    This function has no input or output, but will run through the full game and print out the board after each move
    It should also print out a congrats message to whichever player won

    It should swap between players and make checks each move to see if the game is over, also it should tell a player on their turn when they are in check
    '''

    ## TODO The full game (using all previous functions)
    ############################################

    board = initialize_board()



    ############################################

    return None

play_game()