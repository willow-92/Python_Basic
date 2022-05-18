#section 03-1
# 기본 스크래핑 실습
# Get 방식 데이터 통신(1)


import urllib.request
from urllib.parse import urlparse

# 기본 요청 1(encar)
url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

# 여러 정보
print('type : {}'. format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))