from typing import List
from config import ROWS,COLS


def make_move(board:List[List[str]], col_num:str, player_color:str) -> bool:
    if not col_num.isdigit() or int(col_num) > 7 or int(col_num) < 1:
        print("not valid input , try again!")
        return False
    col = int(col_num) - 1
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player_color
            return True
    print("Column full!")
    return False

def check_if_win(board:List[List[str]], player_color:str) -> bool:
    def check_row():
        for row in range(ROWS):
            for col in range(COLS - 3):
                if board[row][col] == player_color and board[row][col + 1] == player_color and board[row][col + 2] == player_color and board[row][col + 3] == player_color:
                    return True
    def check_col():
        for row in range(ROWS - 3):
            for col in range(COLS):
                if board[row][col] == player_color and board[row + 1][col] == player_color and board[row + 2][col] == player_color and board[row + 3][col] == player_color:
                    return True
    def check_diagonal_left_to_right():
        for row in range(ROWS - 3):
            for col in range(COLS - 3): 
                if board[row][col] == player_color and board[row + 1][col + 1] == player_color and board[row + 2][col + 2] == player_color and board[row + 3][col + 3] == player_color:
                    return True
    def check_diagonal_right_to_left():
        for row in range(3 , ROWS):
            for col in range(0, COLS - 3):
                if board[row][col] == player_color and board[row - 1][col + 1] == player_color and board[row - 2][col + 2] == player_color and board[row - 3][col + 3] == player_color:
                    return True
    return False

