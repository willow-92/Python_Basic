#section 03-1
# 기본 스크래핑 실습
# Get 방식 데이터 통신(1)


import urllib.request
from urllib.parse import urlparse
from urllib.parse import urlencode

from numpy import ogrid

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
api = "https://api.ipify.org"
print(api)

# GET 방식 파라미터
values = {
    'format' : 'text' #jsonp, json, text
}
print('before param : {}'.format(values))

params = urlencode(values)
print('after param : {}'.format(params))

# 딕셔너리 형태를 자동으로 인코딩 해서 바꿔줌

# 요청 URL 생성
URL = api + "?" + params
print("요청 URL = {}".format(URL))
# format을 다양한 형태로 바꿔서 출력해보는 연습도 할 것
# txt로 보내면 ip 주소만 리턴함
# 이런 것들은 웹에서 수신하고 발신할 때 데이터의 규약, 데이터의 형식
# 주로 제이슨을 많이 사용함

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이터 디코딩
text = data.decode('UTF-8')
print('response : {}'.format(text))


# chapter1 에서 썻던 urlopen에 대해서 자세하게 배웠음
# 중요한 것은 urlparse 함수를 이용해서 url 형태를 파싱해서 도메인 부분, 프로토콜 부분, 쿼리 부분을 분리하는 것을 파즈가 해줬음
# 실질적으로 서비스를 제공한데 요청했고, 원하는 딕셔너리 형태를 URL 인코딩을 해서 URL을 만들어서 보내고
# 수신 데이터를 디코딩 해서 출력 해줬음
# 스크래핑은 이게 기본적인 흐름
# 요청하고 수신해서 원하는 데이터가 왔는지를 확인하면 됨
# 그 다음에 그 데이터를 DB에 저장하든, 텍스트 파일로 저장해서 원하는 곳에 사용하면 됨. 

# 짧은 예제이지만, 위에서부터 아래로 보면 하나의 큰 흐름으로 볼 수 있음. 
