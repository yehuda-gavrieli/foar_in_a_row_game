

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
        print("|" + "!".join(rows) + "|")
    print("_" * 15)

print_board(create_board())