import subprocess
subprocess.call(["D:\\Users\\anseilen\\Downloads\\key_macro (2).exe"])
print('파일 불러오기를 완료했습니다')

import pyautogui
print('라이브러리를 불러왔습니다.')
import pygetwindow as gw 
print('pyget window 라이브러리를 불러왔습니다.')
win = gw.getWindowsWithTitle('키보드')[0] 
win.activate()
pyautogui.press('f11')
print('f11을 눌렀습니다')
pyautogui.press('capslock')
print('capslock을 눌렀습니다')