from IPython.display import clear_output

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
        player2 = 'o'
    else:
        player2 = 'x'

    return (player1, player2)


board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']





##Show Welcome Messaage
welcome()

#take player input and initialize player markers
player1_marker, player2_marker = player_input()
