import pyautogui
from pywinauto.keyboard import send_keys
import time
count = 0
repeticoes = 20

while (True):
    if (count <= repeticoes):
        icon_pos = pyautogui.locateOnScreen('arrow.png')
        if icon_pos:
            print(icon_pos)
            x = icon_pos.left+3
            y = icon_pos.top+3
            pyautogui.click(x, y)
            send_keys("{DOWN}")
            send_keys("{DOWN}")
            send_keys("{DOWN}")
            send_keys("{DOWN}")
        else:
            send_keys("{DOWN}")
            send_keys("{DOWN}")
            send_keys("{DOWN}")
            send_keys("{DOWN}")
    else:
        exit()    
        
    count = count + 1
