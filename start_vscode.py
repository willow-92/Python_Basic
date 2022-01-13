# 예시 1
# import subprocess 
# subprocess.call(["C:\\temp\\calc.exe"])

# 예시 2
# import os 
# os.system('"C:/Windows/System32/notepad.exe"')

# import subprocess
# print('subprocess를 불러왔습니다.')
# subprocess.call(["C:\\WINDOWS\\system32\\cmd.exe"])
# print('파일 불러오기를 완료했습니다')

# import os
# os.system('"C:/WINDOWS/system32/cmd.exe"')
# print('불러왔는지 확인')

import pyautogui as pag
import time
# print('라이브러리를 불러왔습니다.')
import pygetwindow as gw 
# print('pyget window 라이브러리를 불러왔습니다.')
# win = gw.getWindowsWithTitle('키보드')[0] 
# win.activate()
# win = gw.getWindowsWithTitle('명령 프롬프트')[1] 
# win.activate()

def cd_b():
    pag.typewrite("cd..")
    pag.press('enter')  

def cd():
    pag.typewrite("cd")
    pag.press('enter')  

pag.press('win')
pag.typewrite("cmd")
time.sleep(0.5)
pag.press('enter')
time.sleep(0.5)
cd_b()
cd_b()
pag.typewrite("cd py")
pag.press('tab')
pag.press('enter')
pag.typewrite("cd sc")
pag.press('tab')
time.sleep(0.5)
pag.press('enter')
pag.typewrite("act")
pag.press('tab')
time.sleep(0.5)
pag.press('enter')
time.sleep(0.5)
pag.typewrite("code")
pag.press('enter')
