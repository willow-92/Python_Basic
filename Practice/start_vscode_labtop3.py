import pyautogui as pag
from time import sleep


pag.keyDown('win')
pag.press('r')
pag.keyUp('win')
pag.typewrite("cmd")
sleep(0.5)
pag.press('enter')

path = "cd C://Python_Projects/Scripts"

pag.typewrite(path)
#sleep(1)
pag.press('enter')
#sleep(1)
pag.typewrite("activate")
#sleep(1.5)
pag.press('enter')
# sleep(0.5)
pag.typewrite("code")
pag.press('enter')
