import ffmpeg
import os

def stt ():
    # mp3 변환
    base_dir = 'C:/Users/kyung.song/Downloads/'
    mp4_file = base_dir + "videoplayback3.mp4"
    mp3_file = base_dir + "audio2.mp3"
    print('start conversion')
    # os.remove('/Python_Basic/youtube_download/audio.mp3')
    cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
    os.system(cmd)

stt()