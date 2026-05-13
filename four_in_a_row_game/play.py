from logic import *
import random

def start_to_play():
    while True:
        choice = get_start_choice()
        if choice == "load":
            board = load_game()
            if board is not None: 
                break 
        elif choice == "new":
            board = create_board()
            break 
        else:
            print("Wrong choice , try again!")
    turn = random.choice("🔴" "🔵")
    game_active = True
    while game_active:
        print_board(board)
        choice, time_of_move = get_user_input()
        if time_of_move > 18:
            print("It's been too long now it's the opponent's turn!")
            if turn == "🔴":
                turn = "🔵"
            else:
                turn = "🔴"
            continue
        if choice.lower() == 's':
            game_active = handle_if_user_quit(board)
        
        elif make_move(board, choice, turn):
            if check_if_win(board, turn):
                print_board(board)
                print("Player", turn, "win!")
                game_active = False
            else:
                if turn == "🔴":
                    turn = "🔵"
                else:
                    turn = "🔴"