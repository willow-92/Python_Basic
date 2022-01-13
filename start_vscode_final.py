import pyautogui as pag
import time
import pygetwindow as gw 

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
