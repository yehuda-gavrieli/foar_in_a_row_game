from file_handeling.files import get_game_number
from typing import List
from config import ROWS,COLS


def create_board()-> List[List[str]]:
    num_of_games = get_game_number()
    print("your game is number" , num_of_games)
    board = []
    for _ in range(ROWS):
        row = [" "] * COLS
        board.append(row)
    return board

def print_board(board:List[List[str]]): 
    print("  ---b o a r d---")
    print("   1 2 3 4 5 6 7 ")
    print("  ---------------")
    for i, rows in enumerate(board):
        print(i + 1,"| " + "  |  ".join(rows) + " |")
    print("  ---------------")