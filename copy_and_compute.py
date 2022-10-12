"""
programe to copy, calculate, and paste
Author: Jordan Hallows
"""
import pyperclip
import pyautogui


def main():
    pyautogui.hotkey('ctrl', 'c')
    try:
        a = eval(pyperclip.paste())
    except:
        a = "Error_unable_to_calculate_input"
    pyperclip.copy(a)
    pyautogui.hotkey('ctrl', 'v')

main()
