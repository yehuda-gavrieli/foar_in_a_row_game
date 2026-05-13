from logic import *

def start_to_play():
    while True:
        choice = get_start_choice()
        if choice == "L":
            board = load_game()
            break 
        elif choice == "N":
            board = create_board()
            break # יוצא מהלולאה וממשיך למשחק
        else:
            print("Wrong choice! Please press 'N' for New or 'L' for Load.")
    turn = "🔴"
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
                save_game(board)
                game_active = False
            else:
                if turn == "🔴":
                    turn = "🔵"
                else:
                    turn = "🔴"