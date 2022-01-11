#01.10
가상환경 내에서 자동으로 VSCODE 실행하기

- 매번 가상환경에서 vscode를 실행시키기가 귀찮아서 자동으로 실행하는 방법을 찾는 중
- autoenvy라는 것이 있다고 하는데 어떤 방식으로 사용하는 것인지 확인이 어려워 다른 방법을 찾음
- 가장 익숙한 형태인 macro를 사용하여 cmd에서 가상환경 내 vscode를 실행하도록 세팅 해 두었음
- 파이썬에서 macro를 실행하도록 코드를 작성

```
    import subprocess
    subprocess.call(["D:\\Users\\anseilen\\Downloads\\key_macro (2).exe"])
```

이후 pyautogui 라이브러리를 사용하여 방금 만든 macro를 실행시키려고 시도함
그러나 동작하지 않음

```
    import pyautogui
    import pygetwindow as gw 
    win = gw.getWindowsWithTitle('키보드') 
    win.activate()
    pyautogui.press('f11')
    pyautogui.press('capslock')
```

관련 내용은 다른 기회에 확인이 필요함

```
time. sleep(숫자)
```
해당 코드를 통해서 시간 지연을 추가할 수 있음. 타임 라이브러리는 따로 불러와야 함
키보드 입력 방식으로 진행이 어려울 경우 마우스 클릭하는 방법 또한 고려해 볼 필요가 있음

다른 방식을 찾아보다가 성공
리스트 파일 형태로 [0]을 입력해주었어야 했는데 빠져 있어서 발생한 문제
내일은 스케쥴러에 파이썬 스크립트를 실행하도록 넣어주고 추가 테스트 진행해볼 필요가 있음.