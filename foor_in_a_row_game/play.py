from logic import *

def start_to_play():
    board = create_board()
    turn = "X"
    game_active = True
    while game_active:
        print_board(board)
        choice, time_of_move = get_user_input()
        if time_of_move > 18:
            print("It's been too long now it's the opponent's turn!")
            if turn == "X":
                turn = "O"
            else:
                "X"
            continue
        if choice.lower() == 's':
            game_active = handle_if_user_quit(board)
        
        elif make_move(board, choice, turn):
            if check_if_win(board, turn):
                print_board(board)
                print("Player", turn, "win!")
                game_active = False
            else:
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"