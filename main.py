import time
import json

def create_board():
    rows = 6
    cols = 7
    board = []
    for _ in range(rows):
        rows = [" "] * cols
        board.append(rows)
    return board

def print_board(board): 
    print("---b o a r d---")
    for rows in board:
        print(rows)
        print("|" + "!".join(rows) + "|")
    print("_" * 15)

#print_board(create_board())


def get_choice_from_user():
    try:
        choice = input("enter your choice: press on the booton esc to exit, p to play for example(p 1 2)").lower().split()
        print(choice)
        res = choice[0]
        action = choice[0].upper()
        r, c = int(choice[1]), int(choice[2])
        if res == "esc":
            print("yes")
    except:
        print("somting wrong")
#get_choice_from_user()

def get_user_input():
    start_time = time.time()
    user_choice = input("press 1-7, or 'S' to Save & Exit: ")
    time_from_start = time.time() - start_time
    return [user_choice, time_from_start]


def check_if_user_whan_to_quit(choice):
    return choice[0].lower() == "s" or choice[0].lower() == "esc"
print(check_if_user_whan_to_quit(get_user_input()))