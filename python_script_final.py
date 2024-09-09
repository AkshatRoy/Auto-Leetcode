import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

def show_error(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)

def ask_ready():
    root = tk.Tk()
    root.withdraw()
    return messagebox.askyesno("Ready Check", "Are you ready for the text to be typed in?")

def type_text(text, interval=0.02):
    lines = text.split('\n')
    for line in lines:
        pyautogui.press('home')
        pyautogui.typewrite(line, interval=interval)
        pyautogui.press('enter')
        time.sleep(interval)

# Main script
question_file_path = Path("question.txt")

if question_file_path.exists():
    with question_file_path.open() as question_file:
        file_name = question_file.readline().strip()
else:
    show_error(f"File {question_file_path} does not exist.")
    exit()

solution_file_path = Path(f"solutions/{file_name}.txt")

if solution_file_path.exists():
    with solution_file_path.open() as solution_file:
        solution_text = solution_file.read()
else:
    show_error(f"File {solution_file_path} does not exist.")
    exit()

time.sleep(7)
if ask_ready():
    x, y = 950, 250
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    time.sleep(5)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

    type_text(solution_text, interval=0.05)

   

    # # Hold ctrl + delete for 5 seconds after typing the last line
    # # pyautogui.keyDown('ctrl')
    # pyautogui.keyDown('delete')
    # time.sleep(5)
    # pyautogui.keyUp('delete')
    # # pyautogui.keyUp('ctrl')
else:
    show_error("Operation cancelled by the user.")
