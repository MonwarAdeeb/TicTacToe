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
        marker = input("Player 1, please pick a marker : 'x' or 'o' :   ").lower()

    player1 = marker

    if (player1 == 'x'):
        return ('x', 'o')
    else:
        return ('o', 'x')
        


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

    for i in range(1, 10):
        if space_check(board, i):
            return False
    #Board is full if we return true
    return True


#ask for player's next choice
def player_choice(board):

    position = 0
    #checking if input is a number first, then checking the space on board
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position : (1-9) : '))

    return position


#print new line for easy viewing
def new_line():
    print('\n')



#check in players want to play again
def replay():

    choice = input("\nPlay again? Enter Yes or No : ").lower()

    return choice == 'yes'


################################################################
#         Beginning calling functions to ply the game!         #
################################################################



##Show Welcome Messaage
welcome()
new_line()

#Beginning of Gameplay
while True:

    #Setting up the board
    the_board = [' ']*10

    #Setting up player markers by tuple unpacking
    player1_marker, player2_marker = player_input()

    #Settting up turn
    turn = choose_first()
    new_line()
    print(turn + ' will go first!')

    #Taking input if the game should begin
    play_game = input('Ready to play? y or n : ').lower()
    new_line()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    while game_on:

        #Player one turn
        if turn == 'Player 1':

            #Showthe board
            display_board(the_board)
            #Choosing a position
            new_line()
            print('Player 1, ')
            position = player_choice(the_board)
            #Place the marker on position
            place_marker(the_board,player1_marker, position)

            #Check if player 1 has won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                new_line()
                print('Player 1 has won!')
                game_on = False
            
            else:
                #if not won, Check if the game is tied
                if full_board_check(the_board):
                    display_board(the_board)
                    new_line()
                    print("Game tied!")
                    break
                #As not won or tied, Give turn to Player 2
                else:
                    turn = 'Player 2'


        #Player two turn
        else:

            #Showthe board
            display_board(the_board)
            #Choosing a position
            new_line()
            print('Player 2, ')
            position = player_choice(the_board)
            #Place the marker on position
            place_marker(the_board,player2_marker, position)

            #Check if player 2 has won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                new_line()
                print('Player 2 has won!')
                game_on = False
            
            else:
                #if not won, Check if the game is tied
                if full_board_check(the_board):
                    display_board(the_board)
                    new_line()
                    print("Game tied!")
                    break
                #As not won or tied, Give turn to Player 1
                else:
                    turn = 'Player 1'
    
    #break out of the loop on replay
    if not replay():
        break
