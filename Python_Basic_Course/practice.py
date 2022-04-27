# youtube 영상 다운받기
from pytube import YouTube
from pytube.cli import on_progress
import os


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

    title = yt.title  # 또는, video_streams.title

    special_char = '\/:*?"<>|.'
    for c in special_char:
        if c in title:
            title = title.replace(c, '')
    print(title)  # 폴더명
 
    video_streams.download(filename= title + '.mp4', output_path='./youtube_download')

    print('영상 다운로드 완료!')


yt_url = 'https://www.youtube.com/watch?v=owYz2mHWf8w&t=1s'
youtube_download(yt_url)