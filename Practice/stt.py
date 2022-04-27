from pytube import YouTube
from pytube.cli import on_progress
import os
import ffmpeg
import webbrowser
import pyautogui as pag
import pygetwindow as gw 
import time



# cd C:\\Users\\anseilen\\Desktop\\
# ffmpeg -i videoplayback (1).mp4 -acodec copy audio.mp3
# start = ffmpeg -i C:\\Users\\anseilen\\Desktop\\videoplayback.mp4 C:\\Users\\anseilen\\Desktop\\video.mp3

tp_x = [3409, 3409, 3409, 3576, 3576, 3576]
tp_y = [605, 635, 665, 605, 635, 665]


def stt ():
    # mp3 변환
    base_dir = 'C:/Users/kyung.song/PycharmProjects/youtube_download/'
    mp4_file = base_dir + "videoplayback.mp4"
    mp3_file = base_dir + "audio.mp3"
    cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
    os.system(cmd)




stt()
