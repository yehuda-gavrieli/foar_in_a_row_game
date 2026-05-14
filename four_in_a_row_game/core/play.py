from core.logic import make_move,check_if_win
from core.user_input import get_start_choice,get_user_input
from file_handeling.files import load_game,handle_if_user_quit
from core.board import create_board,print_board
from config import PLAYER1,PLAYER2,KEYBOARD_KEY
import random , msvcrt


def get_choice_load_or_new():
    while True:
        choice = get_start_choice()
        if choice == "load":
            board = load_game()
            if board is not None: 
                return board 
        elif choice == "new":
            board = create_board()
            return board 
        else:
            print("Wrong choice , try again!")

def start_to_play():
    board = get_choice_load_or_new()
    player_turn = random.choice([PLAYER1 ,PLAYER2])
    is_game_active = True
    while is_game_active:
        print_board(board)
        user_choice , _ = get_user_input()
        if user_choice == "timeout":
            print("It's been too long now it's the opponent's player_turn!")
            player_turn = PLAYER2 if player_turn == PLAYER1 else PLAYER1
            continue
        if user_choice == KEYBOARD_KEY:
            is_game_active = handle_if_user_quit(board)
            if not is_game_active:
                break
            continue
        elif make_move(board, user_choice, player_turn):
            if check_if_win(board, player_turn):
                print_board(board)
                print("Player", player_turn, "win!")
                is_game_active = False
            else:
                player_turn = PLAYER2 if player_turn == PLAYER1 else PLAYER1
    while msvcrt.kbhit():
        msvcrt.getch()
