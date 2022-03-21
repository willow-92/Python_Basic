import pyautogui as pag
import pywinauto
from time import sleep
import pygetwindow as gw 



pag.keyDown('win')
pag.press('r')
pag.keyUp('win')
pag.typewrite("cmd")
sleep(0.5)
pag.press('enter')

sleep(1.5)
# CMD 창 활성화
i=0
try :
    win = gw.getWindowsWithTitle('명령 프롬프트')[0]
    if win.isActive == False:
        for i in range(3):
            time.sleep(1.0)
            win = gw.getWindowsWithTitle('명령 프롬프트')[0]
            
    if win.isActive == False:
        pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate()
    pag.click(win.left + 662, win.top + 189)
except:
    pag.press('esc')



# pag.press('win')
# pag.typewrite("cmd")
# time.sleep(0.5)
# pag.press('enter')

sleep(1)
pag.typewrite("cd PycharmProjects/pythonProject1/venv/Scripts")
sleep(1)
pag.press('enter')
sleep(1)
pag.typewrite("activate")
sleep(1.5)
pag.press('enter')
sleep(1.5)
pag.typewrite("code")
pag.press('enter')
