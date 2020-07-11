from IPython.display import clear_output
import random

#welcome message
def welcome():
    print("Welcome to Tic Tac Toe!")


#displaying the board
def display_board(board):

    clear_output()

    print(board[7] + ' | ' +board[8] + ' | ' +board[9])
    print('---------')
    print(board[4] + ' | ' +board[5] + ' | ' +board[6])
    print('---------')
    print(board[1] + ' | ' +board[2] + ' | ' +board[3])


#taking player input
def player_input():
    
    marker = ''

    while (marker != 'x' and marker != 'o'):
        marker = input("Player 1, please pick a marker : 'x' or 'o'").lower()

    player1 = marker

    if (player1 == 'x'):
        return ('x', 'o')
    else:
        return ('o', 'x')

#initializing the board globally
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


#marking places on the board based on user input
def place_marker(board, marker, position):
    board[position] = marker


#checking if won
def win_check(board, mark):
    return(
        #check rows
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        #check columns
        (board[3] == board[7] == board[9] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        #check diagonals
        (board[3] == board[5] == board[7] == mark) or
        (board[1] == board[5] == board[9] == mark)    
     )


#choose which player goes first
def choose_first():
    
    flip = random.randint(0,1)

    if (flip == 0):
        return 'Player 1'
    else:
        return 'Player 2'


#check if a space is available for marking
def space_check(board, position):
   
    return board[position] == ' '


#check if board is full
def full_board_check(board):

    for (i in range(1, 10)):
        if space_check(board, i):
            return False
    #Board is full if we return true
    return true


#ask for player's next choice
def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,] or rnot space_check(board, position):






##Show Welcome Messaage
welcome()

#take player input and initialize player markers by tuple unpacking
player1_marker, player2_marker = player_input()