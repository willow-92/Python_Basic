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



def stt (type : int, num : int):
    # mp3 변환
    base_dir = '/Python_Basic/youtube_download/'
    mp4_file = base_dir + "videoplayback.mp4"
    mp3_file = base_dir + "audio.mp3"
    os.remove('/Python_Basic/youtube_download/audio.mp3')
    cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
    os.system(cmd)



    # STT 변환
    webbrowser.open("https://clovanote.naver.com/home/note")
    time.sleep(2)
    pag.moveTo(3662, 764, 0.2)
    pag.click()
    pag.moveTo(3360, 42, 0.2)
    pag.click()
    time.sleep(0.2)
    pag.typewrite("C:\Python_Basic\youtube_download")
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.2)
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



# youtube 영상 다운받기
def youtube_download(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress)  # YouTube 객체 생성

    video_streams = yt.streams
    print(video_streams)  # streams 처리 전체 정보

    print(f'영상제목: {yt.title}')
    print(f'영상 조회수: {yt.views}')
    print(f'영상 길이: {yt.length} sec. [{str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)}]')
    print(f'영상 설명: {yt.description}')
    print(f'영상 평점: {yt.rating}')
    print(f'영상 썸네일 링크: {yt.thumbnail_url}')
    print(f'영상 나이 제한: {yt.age_restricted}')
    print(f'영상 제작자: {yt.author}')
    print(f'영상 아이디: {yt.video_id}')
    print(f'영상 채널 URL: {yt.channel_url}')
    print(f'영상 링크: {yt.keywords}')
    print(f'영상 URL: {yt.watch_url}')
    
    ## filter()를 활용하여 파일 확장자 타입 등을 포함한 streams 처리
    video_streams = yt.streams.filter(file_extension='mp4').get_by_itag(22)
    print(video_streams)
    ## <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
    
    # 저장 폴더 만들기
    if not os.path.exists('youtube_download'):
        os.mkdir('youtube_download')
    else:
        pass

    title = 'videoplayback'

    special_char = '\/:*?"<>|.'
    for c in special_char:
        if c in title:
            title = title.replace(c, '')
    print(title)  # 폴더명
 
    video_streams.download(filename= title + '.mp4', output_path='./youtube_download')

    print('영상 다운로드 완료!')






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

yt_url = 'https://youtu.be/-oeBNUXUQv0'
youtube_download(yt_url)
stt(4, 1)