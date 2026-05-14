from typing import List
import json,os
from config import PATH


def get_game_number() -> int:
    if not os.path.exists(PATH):
        return 1
    return len(os.listdir(PATH)) + 1

def save_game(board:List[List[str]]):
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    num_file = len(os.listdir(PATH)) + 1
    filepath = os.path.join(PATH, f"{num_file}.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(board, file, ensure_ascii=False)     
    print("game saved to",filepath)


def load_game() -> List[List[str]]:
    if not os.path.exists(PATH) or not os.listdir(PATH):
        print("not saved games!")
        return None
    files = os.listdir(PATH)
    print(f"choose a game between(0-{len(files)})")
    choice = input("\nEnter the game number: ")
    filepath = os.path.join(PATH, f"{choice}.json")
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            board = json.load(file)
            print("game load successfully!")
            return board
    else:
        print("game number does not exist.")
        return None


def handle_if_user_quit(board:List[List[str]]) -> bool:
    save_game(board) 
    return False 