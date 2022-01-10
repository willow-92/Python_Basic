# 01.10
가상환경 내에서 자동으로 VSCODE 실행하기

- 매번 가상환경에서 vscode를 실행시키기가 귀찮아서 자동으로 실행하는 방법을 찾는 중
- autoenvy라는 것이 있다고 하는데 어떤 방식으로 사용하는 것인지 확인이 어려워 다른 방법을 찾음
- 가장 익숙한 형태인 macro를 사용하여 cmd에서 가상환경 내 vscode를 실행하도록 세팅 해 두었음
- 파이썬에서 macro를 실행하도록 코드를 작성



``` python
import subprocess
subprocess.call(["D:\\Users\\anseilen\\Downloads\\key_macro (2).exe"])
```


이후 pyautogui 라이브러리를 사용하여 방금 만든 macro를 실행시키려고 시도함
그러나 동작하지 않음



``` python
import pyautogui
import pygetwindow as gw 
win = gw.getWindowsWithTitle('키보드') 
win.activate()
pyautogui.press('f11')
pyautogui.press('capslock')
```



관련 내용은 다른 기회에 확인이 필요함
