 # VENV가 만들어지지 않는 현상 발견
 # 한참 시도 했으나 생성 불가. 추후 관련 내용 리서치 하여 다시 도전하기
 # 기존 가상환경 사용도 무방하므로 계속 진행


import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fimage.nmv.naver.net%2Fblog_2022_04_06_2025%2F34c9b456-b5a8-11ec-8c89-505dacfba98a_05.jpg&type=sc960_832'
html_url = 'http://google.com'

# 다운 받을 경로
save_path1 = 'C:/Users/kyung.song/PycharmProjects/Python_Basic/Crawling_Basic/practice_files/test1.jpg'
save_path2 = 'C:/Users/kyung.song/PycharmProjects/Python_Basic/Crawling_Basic/practice_files/index.html'

# 예외 처리

# urlretrieve 함수는 2개를 리턴함
# 첫 번쨰로, 다운로드 받아올 파일과 수신정보. 
# 항상 통신을 할 때는 헤더로 왔다갔다 하는데, 무슨 의미냐, 헤더 정보로 수신을 하고 정보를 한다는 것
# 헤더 값고 수신 정보 값을 가져올 수 있음


try: 
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else: 
    # Header 정보 출력
    print('Header1')
    print(header1)

    print('Header2')
    print(header2)


