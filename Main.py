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
        
        if result[-2:] == '.0':
            result = result[:-2]

        for char in text:
            time.sleep(0.1)
            keyboard.press('backspace')

        for char in result:
            time.sleep(0.1)
            pyautogui.typewrite(char)
            
while True:
    onHighlighted()
