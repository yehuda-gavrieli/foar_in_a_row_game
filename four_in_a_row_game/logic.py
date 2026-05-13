import time
import json
from typing import List,Tuple

ROWS = 6
COLS = 7
def create_board()-> List[List[int]]:
    board = []
    for _ in range(ROWS):
        row = [" "] * COLS
        board.append(row)
    return board
board = create_board()


def print_board(board:List[List[int]]): 
    print("---b o a r d---")
    for rows in board:
        print("|" + "!".join(rows) + "|")
    print("_" * 15)

def get_user_input()-> Tuple:
    start_time = time.time()
    user_choice = input("press num between 1-7, or 'S' to save the game and exit: ")
    time_from_start = time.time() - start_time
    return user_choice, time_from_start

def handle_if_user_quit(board:List[List[int]]) -> bool:
    print("Saving the game")
    with open("save_game.json", "w") as file:
        json.dump(board, file)
    return False

def make_move(board:List[List[int]], col_num:str, player_color:str) -> bool:
    if not (col_num.isdigit() or int(col_num) > 7 or int(col_num) < 1):
        print("not valid input!")
        return False
    c = int(col_num) - 1
    for r in range(ROWS - 1, -1, -1):
        if board[r][c] == " ":
            board[r][c] = player_color
            return True
    print("Column full!")
    return False

def check_if_win(board:List[List[int]], player_color:str) -> bool:
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == player_color and board[r][c+1] == player_color and board[r][c+2] == player_color and board[r][c+3] == player_color:
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == player_color and board[r+1][c] == player_color and board[r+2][c] == player_color and board[r+3][c] == player_color:
                return True
    return False
#winner = check_if_win(board, "🔴")