import ffmpeg
import os
import webbrowser
import pyautogui as pag
import pygetwindow as gw 
import time



# cd C:\\Users\\anseilen\\Desktop\\
# ffmpeg -i videoplayback (1).mp4 -acodec copy audio.mp3
# start = ffmpeg -i C:\\Users\\anseilen\\Desktop\\videoplayback.mp4 C:\\Users\\anseilen\\Desktop\\video.mp3

tp_x = [3409, 3409, 3409, 3576, 3576, 3576]
tp_y = [605, 635, 665, 605, 635, 665]



def stt (type : int, num : int):
    # mp3 변환
    base_dir = '/Users/anseilen/Desktop/'
    mp4_file = base_dir + "videoplayback.mp4"
    mp3_file = base_dir + "audio.mp3"
    os.remove('/Users/anseilen/Desktop/audio.mp3')
    cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
    os.system(cmd)


    # STT 변환
    url = "https://clovanote.naver.com/home/note"
    webbrowser.open(url)
    time.sleep(2)
    pag.moveTo(3662, 764, 0.2)
    pag.click()
    pag.moveTo(2902, 578, 0.2)
    pag.click()
    time.sleep(0.2)
    pag.typewrite("audio.mp3")
    time.sleep(0.2)
    pag.press('enter')  

    x = tp_x[type]
    y = tp_y[type]
    pag.moveTo(x, y, 0.2)
    pag.click()
    pag.moveTo(3678, 745, 0.2)
    pag.click()

    x = tp_x[num]
    y = tp_y[num]
    pag.moveTo(x, y, 0.2)
    pag.click()
    pag.moveTo(3678, 745, 0.2)
    # pag.click()



# type :  대화형태
# 0 = 일반대화
# 1 = 회의
# 2 = 인터뷰, 상담
# 3 = 개인메모
# 4 = 강연
# 5 = 전화통화

# num : 참여자 수
# 0 = 선택하지 않음
# 1 = 1명
# 2 = 2명
# 3 = 3명
# 4 = 4명
# 5 = 5명 이상


stt(4, 1)