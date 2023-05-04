import pyperclip
import keyboard
import pyautogui
import time
import re

def onHighlighted():
    keyboard.wait('ctrl+v')
    text = pyperclip.paste()
