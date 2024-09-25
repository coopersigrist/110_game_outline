##########################################                                 CONNECT 4                                    ###################################################
#                                                                                                                                                                         #
#       If you are not farmiliar with the rules of connect 4 you can go here: https://www.officialgamerules.org/board-games/connect-4                                     #
#       If you want to be weird and use unicode symbols for the pieces you can go here: https://unicode-explorer.com/list/geometric-shapes                                #
#       That'll make it slightly harder to determine which is whose piece but you do you                                                                                  #
#                                                                                                                                                                         #
########################################################################################################################################################################### 

def print_board(baord):
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



    ############################################


    return None

def game_over(board):
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



    ############################################

    return winner


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



    ############################################
    
    return valid

def move(board, player, col):
    '''
    This function should ask the current player which move they'd like to make and then implement it if possible, else
    ask them to give a different move

    Parameters:
        board: A 2d (6x7) list (of lists) which represents a certain state of the board
               values of 1 represent player 1's piecces, a value of -1 represents player 2's and 0 represents empty
        player: An Int representing the player (Player 1 -> 1, Player 2 -> -1)
        col: The coloumn being played in 
    Returns:
        new_board: A 2d list representing the updated board after making the move
    '''
        
    ## TODO Implement a move (with check)
    ############################################



    ############################################
        
    return new_board

def play_game():
    '''
    This function has no input or output, but will run through the full game and print out the board after each move
    It should also print out a congrats message to whichever player won

    It should swap between players and make checks each move to see if the game is over

    '''

    ## TODO The full game (using all previous functions)
    ############################################



    ############################################

    return None

play_game()