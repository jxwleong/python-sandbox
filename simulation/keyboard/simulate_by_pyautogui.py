import sys
import pyautogui

def is_in_interactive_mode():
    return sys.stdout.isatty()

def exit_interactive_shell():
    if is_in_interactive_mode():
        pyautogui.write('exit()')
        pyautogui.press('enter')


exit_interactive_shell()
