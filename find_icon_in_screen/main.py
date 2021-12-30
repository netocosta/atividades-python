import pyautogui
from pywinauto.keyboard import send_keys
import time

count = 0
repeticoes = 999999999

while (True):
    if (count <= repeticoes):
        z=0;
        while (z<=7):
            icon_pos = pyautogui.locateOnScreen('arrow.png')
            if icon_pos:
                print(icon_pos)
                x = icon_pos.left+5
                y = icon_pos.top+5
                pyautogui.click(x, y)
                time.sleep(0.5)
            z = z + 1
        else:
            send_keys("{PGDN}")
            send_keys("{UP}")
            send_keys("{UP}")
    else:
        exit()
          
    count = count + 1
