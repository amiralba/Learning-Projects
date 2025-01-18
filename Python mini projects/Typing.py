import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test")
    stdscr.addstr("\nPress any key to begin!!!")
    stdscr.refresh()
    stdscr.getkey()
    
def display(stdscr, target, current, wpm=0):
    stdscr.clear()
    
    height, width = stdscr.getmaxyx()
    
    def split_text(text, width):
        return [text[i:i + width] for i in range(0, len(text), width)]
    
    target_lines = split_text(target, width)
    current_lines = split_text("".join(current), width)
    
    for i, line in enumerate(target_lines):
        if i >= height - 1:  
            break
        stdscr.addstr(i, 0, line)

    for i, line in enumerate(current_lines):
        if i >= height - 1:  
            break
        for j, char in enumerate(line):
            target_char = target_lines[i][j]
            color = curses.color_pair(1) if char == target_char else curses.color_pair(2)
            stdscr.addstr(i, j, char, color)
    
    stdscr.addstr(height - 1, 0, f"WPM: {wpm}")
        
def load_text():
    try:
        with open("typing_text.txt", "r") as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        return "Error: Could not find the typing text file."


def test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        
        stdscr.clear()
        display(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)  
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) 
    
    start_screen(stdscr)
    
    while True:
        test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to see your score.")
        stdscr.getkey()
        stdscr.addstr(4, 0, "Press ESC to exit or any other key to play again.")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break


wrapper(main)