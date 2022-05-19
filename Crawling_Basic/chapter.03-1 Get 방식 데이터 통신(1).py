#section 03-1
# 기본 스크래핑 실습
# Get 방식 데이터 통신(1)


import urllib.request
from urllib.parse import urlparse

# 기본 요청 1(encar)
url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

# 여러 정보
# print('type : {}'. format(type(mem)))
# print('geturl : {}'.format(mem.geturl()))
# print('status : {}'.format(mem.status))
# print('headers : {}'.format(mem.headers))
# print('headers : {}'.format(mem.getheaders()))
# print('getcode : {}'.format(mem.getcode()))
# print('read: {}'.format(mem.read(123).decode('utf-8')))
print('parse : {}'.format(urlparse('https://www.encar.co.kr?test=test').query))
# 서버로 요청하는 값 중에 get 방식에서 데이터 파라미터, 키는 테스트, 값은 테스트로 보내는데, 그 부분만 쿼리를 입력해주면 그 부분만 출력을 해줌. 
# 전체 정보를 보고싶다고 하면 지우고 URL 정보를 파싱을 해서 분리해줌. 
print('parse : {}'.format(urlparse('https://www.encar.co.kr?test=test')))
# 말도 안되지만, 만약에 이게 아이디와 비밀번호라고 가정하면, id=test&pw=1111 이렇게 되면 서버는 이 정보를 받아서 아이디가 테스트고 비밀번호가 1111인 사람이 로그인을 하는구나, 정보를 줬구나 하는 것을 파악
# 이게 바로 get 방식. 중요 정보가 url에 노출이 되기 때문에 원데이터를 보안 때문에 게시판 형태의 공개적인 서비스 사이트에서 주로 get 방식을 활용한다. 
# 로그인을 활용하거나 중요한 원문 데이터, 긴 데이터는 포스트 방식을 사용한다. 

# 수신 받아보는 예제
# 기본 요청2(ipify)