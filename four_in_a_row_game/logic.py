import time
import json
import os
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
    print(" 1 2 3 4 5 6 7")
    for rows in board:
        print("|" + "!".join(rows) + "|")
    print("_" * 15)

def get_user_input()-> Tuple:
    start_time = time.time()
    user_choice = input("press num between 1-7, or 'S' to save the game and stop: ")
    time_from_start = time.time() - start_time
    return user_choice, time_from_start

def make_move(board:List[List[int]], col_num:str, player_color:str) -> bool:
    if not col_num.isdigit() or int(col_num) > 7 or int(col_num) < 1:
        print("not valid input , try again!")
        return False
    c = int(col_num) - 1
    for r in range(ROWS - 1, -1, -1):
        if board[r][c] == " ":
            board[r][c] = player_color
            return True
    print("Column full!")
    return False

def check_if_win(board:List[List[int]], player_color:str) -> bool:
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player_color and board[row][col + 1] == player_color and board[row][col + 2] == player_color and board[row][col + 3] == player_color:
                return True
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == player_color and board[row + 1][col] == player_color and board[row + 2][col] == player_color and board[row + 3][col] == player_color:
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == player_color and board[row + 1][col + 1] == player_color and board[row + 2][col + 2] == player_color and board[row + 3][col + 3] == player_color:
                return True
    for row in range(3 , ROWS):
        for col in range(0, COLS - 3):
            if board[row][col] == player_color and board[row - 1][col + 1] == player_color and board[row - 2][col + 2] == player_color and board[row - 3][col + 3] == player_color:
                return True
    return False
#winner = check_if_win(board, "🔴")

def load_game() -> List[List[str]]:
    if not os.path.exists("all_games") or not os.listdir("all_games"):
        print("No saved games!")
        return None

    print("--- list of games---")
    files = os.listdir("all_games")
    for file in files:
        print("   game:", file)
    choice = input("\nEnter the game number: ")
    filepath = "all_games/" + choice + ".json"
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            board = json.load(file)
            print("game load successfully!")
            return board
    else:
        print("game number does not exist.")
        return None
    
def get_start_choice():
    return input("press 'new' for new game or 'load' to select a saved game: ").lower()

def save_game(board):
    if not os.path.exists("all_games"):
        os.makedirs("all_games")
    num = len(os.listdir("all_games")) + 1
    filepath = os.path.join("all_games", f"{num}.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(board, file, ensure_ascii=False)     
    print("game saved")

def handle_if_user_quit(board):
    save_game(board) 
    return False 