import pyautogui as pag
import pywinauto
import time
import pygetwindow as gw 

# 자주 입력하는 값 함수화
def cd_b():
    pag.typewrite("cd..")
    pag.press('enter')  

def cd():
    pag.typewrite("cd")
    pag.press('enter')  


pag.keyDown('win')
pag.press('r')
pag.keyUp('win')
pag.typewrite("cmd")
time.sleep(0.5)
pag.press('enter')

time.sleep(1.5)
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
time.sleep(1.5)
pag.typewrite("code")
pag.press('enter')
