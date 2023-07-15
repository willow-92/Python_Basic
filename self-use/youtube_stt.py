from pytube import YouTube
from pytube.cli import on_progress
import os
import ffmpeg
import webbrowser
import pyautogui as pag
import pygetwindow as gw 
import time
import requests

# thumnail url 다운받기
def youtube_thum(file_url):
    save_path = 'D:/kyung/fintech/tistory/clipinfo/thum_nail.jpg'
    url = YouTube(file_url).thumbnail_url
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image downloaded successfully and saved as '{save_path}'")
    else:
        print("Failed to download image")       
    # webbrowser.open(YouTube(file_url).thumbnail_url)

# youtube 영상 다운받기
def youtube_download(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)  # YouTube 객체 생성

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

def mp3to4 ():
    # mp3 변환
    base_dir = '/Python_Basic/youtube_download/'
    mp4_file = base_dir + "videoplayback.mp4"
    mp3_file = base_dir + "audio.mp3"
    os.remove('/Python_Basic/youtube_download/audio.mp3')
    cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
    os.system(cmd)
    print("mp3 -> mp4 변환 완료")

def set_file_location(file_location, file_name):
    pag.moveTo(3360, 42, 0.5)
    pag.click()
    time.sleep(0.5)
    pag.typewrite(file_location)
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.5)
    pag.moveTo(2902, 531, 0.5)
    pag.click()
    time.sleep(0.5)
    pag.typewrite(file_name)
    time.sleep(0.5)
    pag.press('enter')  
    time.sleep(3)

def stt():
    # STT 변환
    webbrowser.open("https://clovanote.naver.com/home/note")
    time.sleep(2)
    pag.moveTo(3662, 764, 0.5)
    pag.click()
    pag.sleep(1)
    set_file_location("C:\Python_Basic\youtube_download", "audio.mp3" )
    pag.sleep(4)
    pag.moveTo(3705, 742, 0.5)
    pag.click()
    # pag.moveTo(3360, 42, 0.5)
    # pag.click()
    # time.sleep(0.5)
    # pag.typewrite("C:\Python_Basic\youtube_download")
    # time.sleep(0.5)
    # pag.press('enter')
    # time.sleep(0.5)
    # pag.moveTo(2902, 578, 0.5)
    # pag.click()
    # time.sleep(0.5)
    # pag.typewrite("audio.mp3")
    # time.sleep(0.5)
    # pag.press('enter')  
    # time.sleep(3)

    # x = tp_x[type]
    # y = tp_y[type]
    # pag.moveTo(x, y, 0.2)
    # pag.click()
    # pag.moveTo(3678, 745, 0.2)
    # pag.click()

    # x = tp_x[num]
    # y = tp_y[num]
    # pag.moveTo(x, y, 0.2)
    # pag.click()
    # pag.moveTo(3678, 745, 0.2)
    # pag.click()

def download_stt(option):
    # 클로바 노트 페이지로 이동
    webbrowser.open("https://clovanote.naver.com/home")
    time.sleep(2)

    # 다운로드 팝업창 닫기
    pag.moveTo(4530, 1126, 0.5)
    pag.click()

    # 최근 변환 노트 클릭
    pag.moveTo(3312, 270, 0.5)
    pag.click()

    #다운로드 팝업창 닫기
    pag.moveTo(3780, 794, 0.5)
    pag.click()

    # 더보기 버튼 클릭
    pag.moveTo(4511, 157, 0.5)
    pag.click()

    # 음성 기록 다운로드 버튼 클릭
    pag.moveTo(4425, 201, 0.5)
    pag.click()
    time.sleep(2)

    # 시간기록 포함 체크박스 해제
    pag.moveTo(3393, 718, 0.5)
    pag.click()

    # 음성 형태에 따라 참석자 포함 체크 여부 결정
    if option == 0:
        pag.moveTo(3533, 718, 0.5)
        pag.click()
    
    # "다운로드" 버튼 클릭
    pag.moveTo(3688, 810, 0.5)
    pag.click()

    # 파일 다운로드 경로 입력창 클릭
    pag.moveTo(3333, 50, 0.5)
    pag.click()

    # 파일 다운로드 경로 입력
    pag.typewrite('D:/kyung/fintech/tistory/clipinfo')
    time.sleep(0.5)
    pag.press('enter')  

    pag.moveTo(3559, 492, 0.5)
    pag.click()
    pag.typewrite('stt.txt')

    pag.moveTo(3490, 572, 0.5)
    pag.click() 

    pag.moveTo(3605, 594, 0.5)
    pag.click() 
    pag.moveTo(4527, 1122, 0.5)
    pag.click()


# 블로그 시작
def set_blog():
    webbrowser.open("https://blog.naver.com/david383")
    pag.sleep(5)
    pag.moveTo(3067, 641, 5)
    pag.click()
    pag.sleep(3)
    pag.moveTo(4495, 180, 0.5)
    pag.click()
    pag.sleep(0.5)
    pag.moveTo(4441, 310, 0.5)
    pag.click()
    pag.sleep(0.5)
    pag.moveTo(4351, 499, 0.5)
    pag.click()
    pag.sleep(0.5)

# 영상 정보 저장 및 티스토리 템플릿 생성하기
def download_clip_info(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)  # YouTube 객체 생성
    video_streams = yt.streams
    upload = str(f'{yt.publish_date}')[0:10].replace('_','.')
    
    # 블로그 템플릿 생성
    with open('D:/kyung/fintech/tistory/clipinfo/clip_info.txt', 'w') as f:

        f.write(f'''<h2 data-ke-size="size26"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR'; font-size: 1.62em;">{yt.title} - {yt.author}[&#x1F440;눈튜브 : 눈으로 읽는 유튜브]</span></h2>\n''')
        f.write('''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">유튜브 영상을 글로 편하게 보고 다시 공부하기 위해 정리한 글입니다.</span></p>\n''')
        f.write('''<p data-ke-size="size18">&nbsp;</p>\n''')
        f.write(f'<p data-ke-size=\"size18\"><span style=\"font-family: \'Noto Sans Demilight\', \'Noto Sans KR\';\">채널명 : {yt.author}</span></p>\n')
        f.write(f'''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">제목 : {yt.title}</span></p>\n''')
        f.write(f'''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">업로드일: {upload}</span></p>\n''')
        f.write(f'''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">영상 길이: {str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)}</span></p>\n''')
        f.write(f'''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">원본영상: <a href="{yt.watch_url}">{yt.watch_url}</a>&nbsp;</span></p>\n''')
        f.write(f'''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">[요약]</span></p>\n''')
        f.write('''<ul style="list-style-type: disc;" data-ke-list-type="disc">\n''')
        f.write('''<li>&nbsp;</li>\n''')
        f.write('''<li>&nbsp;</li>\n''')
        f.write('''<li>&nbsp;</li>\n''')
        f.write('''</ul>\n''')
        f.write('''<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />\n''')
        f.write('''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">[내용 전문]</span></p>\n''')
        f.write('''<div data-ke-type="moreLess" data-text-more="더보기" data-text-less="닫기"><a class="btn-toggle-moreless">더보기</a>\n''')
        f.write('''<div class="moreless-content">\n''')
        with open ('D:/kyung/fintech/tistory/clipinfo/stt.txt', 'r', encoding='utf-8-sig') as data:
            lines = data.readlines()
            for i in lines:
                print(i)
                

    print(f'채널명: {yt.author}')
    print(f'제목: {yt.title}')
    print(f'업로드일:', upload)
    print(f'영상 길이: {str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)}')
    print(f'원본 영상: {yt.watch_url}')
    print(f'영상 정보 저장 완료')

def setup_template():
    pag.hotkey('win', 'r')
    time.sleep(0.5)
    pag.typewrite('D:/kyung/fintech/tistory/clipinfo/clip_info.txt')
    pag.press('enter')  
    time.sleep(0.5)
    pag.hotkey('ctrl', 'a')
    pag.hotkey('ctrl', 'c')
    webbrowser.open("https://steady-learning.tistory.com/")
    time.sleep(2)
    
    # 마이페이지 클릭
    pag.moveTo(4070, 139, 0.5)
    pag.click()

    # 글쓰기 버튼 클릭
    pag.moveTo(4070, 223, 0.5)
    pag.click()
    time.sleep(2)

    # 이전 저장 무시를 위한 버튼 클릭
    pag.moveTo(3730, 186, 0.5)
    pag.click()

    # 모드 선택 버튼 클릭
    pag.moveTo(3864, 135, 0.5)
    pag.click()

    # HTML 버튼 클릭
    pag.moveTo(3864, 251, 0.5)
    pag.click()

    # 본문 내역 클릭
    pag.moveTo(2694, 337, 0.5)
    pag.click()
    time.sleep(0.5)

    # 붙여넣기
    pag.hotkey('ctrl', 'v')

    # 모드 선택 버튼
    pag.moveTo(3812, 136, 0.5)
    pag.click()

    # 기본 모드로 변경
    pag.moveTo(3812, 183, 0.5)
    pag.click()

    # 제목 복사
    pag.moveTo(3380, 408, 0.5)
    pag.click()
    pag.click()
    pag.click()
    pag.hotkey('ctrl', 'c')

    # 제목 붙여넣기
    pag.moveTo(3153, 292, 0.5)
    pag.click()
    pag.hotkey('ctrl', 'v')
    pag.press('left')
    for i in range(13):
        pag.press('backspace')






# stt(인자 설명)
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

#
print(pag.position())

# 북마크바 켜져 있는지 확인 (켜져 있어야 함)
# 다운로드 파일이 있어서 화면 하단에 다운로드 팝업이 있는지 확인 (팝업이 없어야 함)
# 화면 배율 100%

yt_url = '''
https://www.youtube.com/watch?v=wIyl9wpl8rY
'''
# youtube_download(yt_url)

# mp3to4()
# stt()
# time.sleep(600)
# download_stt(0)
# set_blog() #네이버 블로그
# 티스토리용
# time.sleep(5)
# download_clip_info(yt_url)
youtube_thum(yt_url)
# time.sleep(5)
# setup_template()