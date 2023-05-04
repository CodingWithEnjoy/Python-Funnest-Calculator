import pyperclip
import keyboard
import pyautogui
import time
import re

def onHighlighted():
    keyboard.wait('ctrl+v')
    text = pyperclip.paste()

    if re.search(r'[+\-*/^=0-9\s]', text):
        result = str(eval(text.replace('^', '**')))
