import random

def display_board(board):  # This will display the game board
    print("\n" * 45)
    print("    |   |   ")
    print(" {}  | {} | {}  ".format(board[7], board[8], board[9]))
    print("    |   |   ")
    print("-------------")
    print("    |   |   ")
    print(" {}  | {} | {}  ".format(board[4], board[5], board[6]))
    print("    |   |   ")
    print("-------------")
    print("    |   |   ")
    print(" {}  | {} | {}  ".format(board[1], board[2], board[3]))
    print("    |   |   ")


def who_goes_first():  # this will decide who goes first player 1 or player 2
    random_ = random.randint(1, 2)
    if random_ == 1:

        return 1
    else:
        return 2


def space_check(board, position):  # this checks if the position you are entering X or O is available or not ?
    return board[position] == ' '


def choose_position(board):  # this asks player input for number in-between (1-9)
    position = int(input('Choose a number between (1-9): '))
    if position in range(1,10) and space_check(board, position) == True:
        return position
    else:
        return False


def x_or_o():
    while True:
        marker = input('Player1: Do you want to be X or O ?: ').upper()
        if marker == 'X' or marker == 'O':

            if marker == 'X':
                return ('X','O')
                break
            else:
                return ('O', 'X')
                break


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    if board[1] == board[2] == board[3] == marker or \
       board[4] == board[5] == board[6] == marker or \
       board[7] == board[8] == board[9] == marker or \
       board[1] == board[4] == board[7] == marker or \
       board[2] == board[5] == board[8] == marker or \
       board[3] == board[6] == board[9] == marker or \
       board[1] == board[5] == board[9] == marker or \
       board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


def full_board_check(board):
    for x in range(1,10):
        if board[x] == ' ':
            return True
    else:
        return False


def replay():
    yes_or_no = input('Do you want to play again? yes or no : ').lower()
    if yes_or_no == 'yes':
        return True
    else:
        return False

def play_game():
    print('Welcome to Tic Tac Toe game!')
    while True:
        game_board = [' ']*10
        player1_marker, player2_marker = x_or_o()
        who_is_first = who_goes_first()
        print(f'Player{who_is_first} will go first.')
        play_or_no = input('Are you ready to play? y or n ?: ').lower()
        game_on = False
        if play_or_no == 'y':
            game_on = True
        else:
            game_on= False

        while game_on:
            if who_is_first == 1:
                display_board(game_board)
                print(f'Player 1 turn ({player1_marker})')
                place_marker(game_board, player1_marker, choose_position(game_board))
                if win_check(game_board,player1_marker):
                    display_board(game_board)
                    print('Player 1 Wins!!!')
                    break
                else:
                    if full_board_check(game_board) == False:
                        display_board(game_board)
                        print("It's a Tie game!!")
                        break
                    else:
                        who_is_first = 2
            else:
                display_board(game_board)
                print(f'Player 2 turn ({player2_marker})')
                place_marker(game_board, player2_marker, choose_position(game_board))
                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print('Player 2 Wins!!!')
                    break
                else:
                    if full_board_check(game_board) == False:
                        display_board(game_board)
                        print("It's a Tie game!!")
                        break
                    else:
                        who_is_first = 1
        if not replay():
            print('Thank you for playing!!!! ')
            break


play_game()
