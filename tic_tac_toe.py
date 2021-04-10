import random


# This function must be completed
def space_value(board, index):
    """
    Get the value for a space in the board.

    Returns the value in the board at the given index, if not a string that
    contains a space. Otherwise, it returns the index as a string.

    Arguments: board: An array of nine strings | index: The value in the board to
    interrogate
    """
    if board[index] != " ":
        return board[index]
    else:
        return f'{index}'


def draw_board(board):
    """This function prints out the board that it was passed."""
    # print("   |   |")
    print("----------------------")
    print(f" {space_value(board, 7)} | {space_value(board, 8)} | {space_value(board, 9)}")
    # print("   |   |")
    print("----------------------")
    # print("   |   |")
    print(f" {space_value(board, 4)} | {space_value(board, 5)} | {space_value(board, 6)}")
    # print("   |   |")
    print("----------------------")
    # print("   |   |")
    print(f" {space_value(board, 1)} | {space_value(board, 2)} | {space_value(board, 3)}")
    # print("   |   |")
    print("----------------------")


def get_player_and_computer_letters():
    """
    Lets the player type which letter they want to be.

    Returns a list with the player's letter as the first item and the computer's
    letter as the second item.
    """
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


# This function must be completed
def play_again():
    """
    Determines if the player wants to play again.

    It should ask the player if they want to play again, then read input from the
    player to determine if they typed some value that begins with the letter
    "y". If the value does begin with "y", then return True. Otherwise, return
    False.
    """
    response = input('Would you like to play again? \n')
    
    if response.startswith('y'):
        return True
    return False


def make_move(board, letter, move):
    """Set the board at index move to the provided letter"""
    board[move] = letter


# This function must be completed
def is_winner(board, letter):
    """
    Determines if the specified letter is a winner.

    Given the board and the player's letter, this function returns True if that
    player has won.
    """
    possible_wins = [
        #horizontal
        [1, 2, 3],
        [4, 5, 6], 
        [7, 8, 9],
        #vertical
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        #diagonal
        [1, 5, 9],
        [3, 5, 7],
    ]

    ## loop over all win sets
    for win_set in possible_wins:
        ## for a given win set, loop over the space numbers provided in the win_set
        ## filter whether the value stored at the given space matches the players letter
        ## if all 3 match, the returned list will have a length of 3, indicating a win
        win_boolean = len([ space for space in win_set if board[space] == letter]) == 3
        if win_boolean:
            return True
    
    return False
        



def is_space_free(board, move):
    """Return True if the value in board at move is " "."""
    return board[move] == " "


# This function must be completed
def get_player_move(board):
    """
    Prompt the player for their move and return their value as an integer.

    This function insures that the board space in which the player wants to play
    is empty. If the player indicates a square that already has a value in it,
    then the function tells the player that is an invalid move and prompts the
    player, again, for a value.
    """
    intake = input('Please type the integer of the square for which you would like to move: ')
    try: 
        move = int(intake)
    except: 
        print(f'Hmmm... I do not believe that was an integer. Please try again...')
        return get_player_move(board)
    
    if is_space_free(board, move):
        return move
    else:
        print(f'Sorry, that square is already taken. Lets try again...')
        return get_player_move(board)

    


# This function must be completed
def get_random_move(board):
    """
    Returns a valid random move for the computer from an empty space in the
    board.

    To get nice random moves, consider using the random.shuffle method, here.
    """
    nums = [i for i in range(1, 10)]    # return range of nums from 1 - 9
    random.shuffle(nums)                # shuffle nums range
    comp_move = nums[0]                 # take 1st of newly shuffled range

    if is_space_free(board, comp_move): # if available...
        return comp_move                # proceed with move
    else: 
        return get_random_move(board)   # else, try again
    

# This function must be completed
def is_board_full(board):
    """
    Return True if every space on the board has been taken. Otherwise return
    False.
    """
    board[0] = "0"  ## board initialize with 10 " " spaces, but only 9 on the board; fill board[0] by default
    for index, value in enumerate(board):
        if is_space_free(board, index):
            return False
    return True


print("Welcome to Tic Tac Toe!")

while True:
    board = [" "] * 10
    player, computer = get_player_and_computer_letters()
    if player == "X":
        turn = "player"
    else:
        turn = "computer"
    game_in_progress = True

    while game_in_progress:
        if turn == "player":
            draw_board(board)
            move = get_player_move(board)
            make_move(board, player, move)

            if is_winner(board, player):
                draw_board(board)
                print("Hooray! You have won the game!")
                game_in_progress = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            move = get_random_move(board)
            make_move(board, computer, move)

            if is_winner(board, computer):
                draw_board(board)
                print("The computer has beaten you! You lose.")
                game_in_progress = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"
    if not play_again():
        break
