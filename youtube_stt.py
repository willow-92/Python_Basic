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


def setup_template(file_loc, blog_loc):
    pag.hotkey('win', 'r')
    pag.typewrite('file_loc')
    pag.press('enter')  
    time.sleep(0.5)
    pag.hotkey('ctrl', 'a')
    pag.hotkey('ctrl', 'c')
    webbrowser.open("blog_loc")
    time.sleep(2)
    pag.moveTo(4012, 139, 0.5)
    pag.click()
    pag.moveTo(4012, 223, 0.5)
    pag.click()
    time.sleep(2)
    pag.moveTo(3730, 186, 0.5)
    pag.click()
    pag.moveTo(3834, 135, 0.5)
    pag.click()
    pag.moveTo(3834, 228, 0.5)
    pag.click()
    pag.moveTo(2694, 337, 0.5)
    pag.click()
    time.sleep(0.5)
    pag.hotkey('ctrl', 'v')
    pag.moveTo(3783, 136, 0.5)
    pag.click()
    pag.moveTo(3783, 183, 0.5)
    pag.click()
    
    def download_stt(option):
    webbrowser.open("https://clovanote.naver.com/home")
    time.sleep(2)
    pag.moveTo(3312, 270, 0.5)
    pag.click()
    pag.moveTo(4511, 157, 0.5)
    pag.click()
    pag.moveTo(4425, 201, 0.5)
    pag.click()
    time.sleep(2)
    pag.moveTo(3391, 671, 0.5)
    pag.click()
    if option == 0:
        pag.moveTo(3533, 666, 0.5)
        pag.click()
    pag.moveTo(3684, 715, 0.5)
    pag.click()
    pag.moveTo(3157, 50, 0.5)
    pag.click()
    pag.typewrite('D:/')
    pag.press('enter')  
    pag.moveTo(3487, 531, 0.5)
    pag.click()
    pag.typewrite('stt.txt')
    pag.moveTo(3519, 609, 0.5)
    pag.click() 
    pag.moveTo(3605, 594, 0.5)
    pag.click() 
    pag.moveTo(4527, 1122, 0.5)
    
    def download_clip_info(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress)  # YouTube 객체 생성
    video_streams = yt.streams
    upload = str(f'{yt.publish_date}')[0:10].replace('_','.')
    
    # 블로그 템플릿 생성
    with open('file_path', 'w') as f:

        f.write(f'''<h2 data-ke-size="size26"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR'; font-size: 1.62em;">{yt.title} - {yt.author}[&#x1F440;제목]</span></h2>\n''')
        f.write('''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';" 설명문 </span></p>\n''')
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
        f.write('''<p data-ke-size="size18"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">[내용 전문]</span></p>\n''')
        f.write('''<div data-ke-type="moreLess" data-text-more="더보기" data-text-less="닫기"><a class="btn-toggle-moreless">더보기</a>\n''')
        f.write('''<div class="moreless-content">\n''')
        with open ('file_path', 'r', encoding='utf8') as data:
            lines = data.readlines()
            for i in lines:
                print(i)
                f.write(f'''<p data-ke-size="size16">{i}</p>''')

    print(f'채널명: {yt.author}')
    print(f'제목: {yt.title}')
    print(f'업로드일:', upload)
    print(f'영상 길이: {str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)}')
    print(f'원본 영상: {yt.watch_url}')
    print(f'영상 정보 저장 완료')


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

yt_url = ''
youtube_download(yt_url)
stt(4, 1)
