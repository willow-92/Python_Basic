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
# 첫 번쨰로, 다운로드 받아올 파일이름과 수신정보 (수신 헤더값). 
# 항상 통신을 할 때는 헤더로 왔다갔다 하는데, 무슨 의미냐, 헤더 정보로 수신을 하고 정보를 한다는 것
# 헤더 값과 수신 정보 값을 가져올 수 있음
# 매우 편한 함수. 


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

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    print('Download Succeed')


# http는 1회성 연결. 요청을 하고 응답을 주고 연결이 끊어짐. 
# 그렇기 때문에 채팅과 같이 실시간 성으로 수발신을 하기 위해서는 소켓통신을 활용하기도 함
# http 통신은 1번 요청과 수신을 하면 연결이 끊긴다. 
# 그렇기 때문에 쿠키값을 이용해서 세션을 유지시키는 기능을 해야 함

# 폴더에 가보면 파일들이 다운되어 있음.
# 타겟 URL을 요청해서 그 URL에 있는 모든 정보를 내 컴퓨터로 가져오는 것이 시작
# 이 안에서 정보를 찾는 것을 파싱이라고 하는데, 이런 것들을 위해 파이썬에 많은 도구가 있음.

# 네이버 이미지를 다운로드 받았고. 
# 구글 HTML 정보를 다운 받았고
# header정보 확인했고
# 다운로드 정보 파일 저장함


# 가장 중요한 것은 Header로 송수신을 한다는 것. 
# status 코드가 200번이 나와야 정상처리가 된것
# urlib.request 함수를 이용함



