# Section04-3
# Requests
# requests 사용 스크래핑(3) - Rest API

# Rest API : GET, POST, DELETE, PUT:UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# 과거에는 get과 post 방식으로 게시판에 글을올리거나 했는데, 지금은 PUT으로 요청할 수 있고, replace. fetch. put과 fech를 번갈아가면서 사용하기도 함
# 왜 쓸까? 
# 중요 : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# /movies : 영화를 전부 조회
# url 정보만 보고 이 자원의 상태를 알 수 있는 것.
# 이런 방식으로 개발을 하면 수정도 편하고 협업을 해서 rest api를 정의해놓고 하면 수백명 수십명이 개발을 해도 일관적인 개발 프로세스를 밟을 수 있음
# GET: www.movies.com/movies : 영화를 전부 조회
# GET: www.movies.com/movies/:id : 아이디인 영화를 조회
# POST: www.movies.com/movies/: 영화를 생성
# PUT: www.movies.com/movies/: 영화를 수정
# DELETE: www.movies.com/movies/: 영화를 삭제
# URL 주소는 변화가 없는데, 요청하는 방식에 따라서 서버에서 영화를 조회해서 브라우저로 줄 수 있고.
# 아이디가 몇 번인 영화만 보고 싶으면 겟
# 포스트로 요청하면 등록하는 쪽 
# 풋으로 요청하면 수정하거나. 풋도 생성이 될 수 있음
# 딜리트 하면 오래된 영화를 삭제하고. 
# 스크래핑과 관련은 없지만, 개발, 취미가 아니어도 이 정도 까지 알고 있으면 http 통신을 활용한 데이터의 송수신에 대해서는 어느 정도 지식을 갖췄다고 할 수 있음
# 구글에서 rest api가 무엇인지 시간될 때 확인해볼 것. 

# REST란?
# Represeantational State Transfer의 약자
# 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.

import requests
import pprint

# 세션 활성화
s = requests.session()

# 예제 1
r =s.get('https://api.github.com/events')

# 수신상태 체크 -> 실패하면 예외처리까지 해줌
r.raise_for_status()

# 출력
# print(r.text)

# 예제 2 -> 쿠키정보를 디테일하게 할 때
# 쿠기설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name', 'niceman', domain = "httpbin.org", path='/cookies')

# 요청
# r = s.get('http://httpbin.org/cookies', cookies = jar)

# 출력
# print(r.text)

# 예제3
# r = s.get('https://github.com', timeout=5)

# 출력
# pprint.pprint(r.text)

# 예제4
# r = s.post('http://httpbin.org/post', data={'id':'test7', 'pw': '111'}, cookies=jar)

# print(r.text)
# print(r.headers)


# 예제5

payload1 = {'id':'test7', 'pw': '111'}
payload2 = (('id', 'test7'), ('pw', '111111'))

# r = s.post('http://httpbin.org/post', data=payload2)

# 출력
# print(r.text)


# 예제6(PUT)
# r = s.put('http://httpbin.org/put', data=payload1)

# print(r.text)
r = s.delete('http://httpbin.org/delete', data={'id' : 1})

# 출력
# print(r.text)

# 예제7(Delete)
r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.ok)
print(r.text)
print(r.headers)


s.close()

# rest api url로 자원의 상태 정보를 받는 것
# 딜리트, 풋. 리퀘스트 패키지 정말 편하다. 
# 
