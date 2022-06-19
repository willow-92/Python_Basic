# section 04-1
# Requests
# Requests 사용 스크래핑(1) - Session

# 쿠키 -> 정보를 담아 놨다가 활용
# 식별되지 않은 방대한 클라이언트들을 어떻게 구분할까?
# 이런 것들을 식별하기 위해 쿠키 정보를 저장해놨다가 활용

# 쿠키는 많이 사용되기 때문에, 직접 쿠기 정보를 서버에 전송할 수 있어야 함.
# 네이버 개발자도구에서 어플리케이션탭의 쿠키를 보면 이런 쿠기 정보를 활용한다고 알 수 있음
# 딕셔너리 형태로 핸들링 할 수 있고
# 방문을 할 때 마다 쿠기 정보가 쌓이는 것을 볼 수 있고. 딜리트 키로 지울 수도 있음

from urllib.request import HTTPBasicAuthHandler
import requests

# 세션 활성화
# s = requests.session()
# 세션을 열었다는 것은 닫는 메소드도 존재한다는 것. 그래야 불필요한 리소스 낭비를 막을 수 있음. 

# r = s.get('https://www.naver.com')

# 수신 데이터
# print(r.text)

# 수신 상태 코드
# print('Status Code : {}'.format(r.status_code))

# 확인 
# print('Ok? : {}'.format(r.ok))
# true 가 나왔다는 것은 정확하게 수신이 되었다는 의미. 
# 조건문에서 주로 활용함


# 세션 비활성화
# s.close()    


# HTTPbin.org

# s = requests.session()

# 쿠키 Return
# r1 = s.get('https://httpbin.org/cookies', cookies = {'name' : 'kim1'})
# print(r1.text)

# 쿠키 Set
# r2 = s.get('https://httpbin.org/cookies/set', cookies = {'name' : 'kim2'})
# print(r2.text)

# User-Agent
# url = 'https://httpbin.org'
# headers = {'user-agent': 'nice-man_1.0.0_win10_ram16_home_chrome'}
# Header 정보 전송
# r3 = s.get(url, headers=headers)
# print(r3.text)


# 세션 비활성화
# s.close()

# 클라이언트(요청한는 쪽)에서는 서버 측에서 이 클라이언트가 정상적으로 접근을 해서 나의 데이터, 내가 주는 정보를 수신해 가는지 확인하기 위해서 쿠키와 같은 헤더정보를 확인함. 
# 헤더 정보에 파이썬과 같은 정보가 온다면 정보 크롤링을 허가하지 않음. 물론 robot txt에서 권고안을 주기는 하지만, 헤더정보로 클라이언트에 허가되지 않은 행동을 구분함. 
# 가장 중요한 것은 get 방식으로 요청할 때 쿠키와 헤더정보를 실어서 우리가 이 만들어놓은 코드가 정상적으로 요청을 하는구나, 클라이언트가 요구하는 대로 정보를 페이로드, 실어서 요청할 수 있또록
# 만들어주는 그런 리퀘스트 모듈의 강력한 기능. 

# 실무에서 with 문을 권장함. -> 파일 관련, DB 관련, HTTP 통신관련. 
# 외부 리소스를 요청함. 코드도 간결해지고. 다른 사람이 코드를 볼 때 외부 관련 작업을 한다는 것을 알 수 있음
# with 문이 끝날 때 사용한 리소스 반환 작업이 자동으로 이루어짐.

with requests.Session() as s: 
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)

# 세션을 활성화 비활성화
# 쿠키를 헤더 정보로 만들어서 요청 했다는 것
# 수신 상태 확인하는 방법
# 
