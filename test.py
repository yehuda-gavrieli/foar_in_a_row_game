import time
import json
import os

# --- הגדרות ---
ROWS = 6
COLS = 7

# --- 1. פונקציות תשתית (לוח ותצוגה) ---

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def display_board(board):
    print("\n  1 2 3 4 5 6 7")
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * 15)

# --- 2. פונקציות קלט וזמן ---

def get_input_from_user():
    """פונקציה שמקבלת קלט ומודדת זמן"""
    start_time = time.time()
    user_choice = input("Enter 1-7, or 'S' to Save & Exit: ")
    elapsed_time = time.time() - start_time
    return user_choice, elapsed_time

def check_if_quit(choice):
    """בודקת אם המשתמש רוצה להפסיק (הקיש S או ESC)"""
    return choice.upper() == "S" or choice.upper() == "ESC"

# --- 3. פונקציות לוגיקת המהלך (שורה ועמודה) ---

def get_lowest_empty_row(board, col):
    """מוצאת את השורה הפנויה הכי נמוכה בעמודה שנבחרה"""
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == " ":
            return r
    return -1

def drop_piece(board, col, player_char):
    """מבצעת את המהלך בלוח אם הוא תקין"""
    row = get_lowest_empty_row(board, col)
    if row != -1:
        board[row][col] = player_char
        return True
    return False

# --- 4. פונקציות בדיקת מצב המשחק ---

def check_win(board, p):
    """בדיקה בסיסית לניצחון (שורות ועמודות)"""
    # בדיקת שורות
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == p and board[r][c+1] == p and board[r][c+2] == p and board[r][c+3] == p:
                return True
    # בדיקת עמודות
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == p and board[r+1][c] == p and board[r+2][c] == p and board[r+3][c] == p:
                return True
    return False

# --- 5. פונקציות שמירה וניהול תור ---

def save_and_close(board, turn):
    with open("game_data.json", "w") as f:
        json.dump({"board": board, "turn": turn}, f)
    print("Game saved. See you next time!")

def switch_player(current):
    return "O" if current == "X" else "X"

# --- 6. הפונקציה המנהלת (הלולאה הראשית) ---

def run_game():
    board = create_board()
    player = "X"
    
    while True:
        display_board(board)
        print(f"Current Player: {player}")
        
        choice, time_taken = get_input_from_user()
        
        # בדיקת חריגת זמן (סעיף 1)
        if time_taken > 18:
            print("Time out! Switching turns...")
            player = switch_player(player)
            continue
            
        # בדיקה אם המשתמש רוצה לסיים (מה שביקשת)
        if check_if_quit(choice):
            save_and_close(board, player)
            break
            
        # טיפול בבחירת עמודה (מה שביקשת)
        if choice.isdigit():
            col = int(choice) - 1
            if 0 <= col < COLS:
                if drop_piece(board, col, player):
                    if check_win(board, player):
                        display_board(board)
                        print(f"Player {player} Wins!")
                        break
                    player = switch_player(player)
                else:
                    print("Column full!")
            else:
                print("Choose 1-7 only.")
        else:
            print("Invalid input.")

# --- קריאות לדוגמה לכל פונקציה (לבדיקת תקינות) ---
# 1. יצירת לוח: b = create_board()
# 2. החלפת שחקן: p = switch_player("X") -> "O"
# 3. מציאת שורה: row = get_lowest_empty_row(b, 0)
# 4. בדיקת יציאה: exit_now = check_if_quit("S") -> True

if __name__ == "__main__":
    run_game()