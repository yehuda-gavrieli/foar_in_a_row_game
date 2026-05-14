from typing import Tuple
import keyboard ,time
from config import KEYBOARD_KEY,TIME,COLS

def get_user_input() -> Tuple:
    start_time = time.time()
    print("press num between 1-7, or ESC to save and exit: ", flush=True)
    while True:
        current_time = time.time() - start_time
        if current_time > TIME:
            return ["timeout", current_time]
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == KEYBOARD_KEY: 
                return [KEYBOARD_KEY, current_time]
            elif event.name in [str(i) for i in range(COLS)]: 
                return [event.name , current_time]
            
def get_start_choice() -> str:
    return input("press 'new' for new game or 'load' to select a saved game: ").lower()



