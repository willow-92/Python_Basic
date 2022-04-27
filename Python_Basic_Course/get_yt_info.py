import pytube.cli import Youtube

# 영상 정보 저장하기
def download_clip_info(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress)  # YouTube 객체 생성
    video_streams = yt.streams
    upload = str(f'{yt.publish_date}')[0:10].replace('_','.')
    print(f'채널명: {yt.author}')
    print(f'제목: {yt.title}')
    print(f'업로드일:', upload)
    print(f'영상 길이: {str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)}')
    print(f'원본 영상: {yt.watch_url}')
    print(f'영상 정보 저장 완료')
