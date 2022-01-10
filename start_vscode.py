import subprocess
subprocess.call(["D:\\Users\\anseilen\\Downloads\\key_macro (2).exe"])

import pyautogui
import pygetwindow as gw 
win = gw.getWindowsWithTitle('키보드') 
win.activate()
pyautogui.press('f11')
pyautogui.press('capslock')