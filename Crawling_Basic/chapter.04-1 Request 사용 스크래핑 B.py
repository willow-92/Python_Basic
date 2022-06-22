# section 04-2
# Requests
# requests 사용 스크래핑(2) - JSON

# Json 데이터 방식을 파이썬으로 수싱해서 파싱후 원하는 값을 추출해서 데이터를 표시
# Json? 구글 검색해서 확인해볼 것.
# Json은 데이터 교환 형식. 경량.
# xml을 대체하고 있음
# 자바스크립트에서 개체를 만들 때 사용하는 표현 식
# json은 특정 언어에 종속되지 않음. 언어와 상관 없이 json 포맷에서 핸들링 할 수 있는 라이브러리를 제공
# 확장자가 json 형식으로 이뤄진 파일이나 형식을 이용해서 웹으로 보내고 받고. 대부분 웹에서 유튜브나 인스타그램과 같은 API에서도 json 형식으로 데이터를 내려주고 있음

import json
import requests

# httpsbin.org에서 json 받아서 진행해보기

s = requests.session()

# 100개 JSON 데이터 요청
r = s.get('https://httpbin.org/stream/100', stream = True)
# 궁금하면 stream 옵션 검색해볼 것

# 수신 확인
# print(r.text)


# Encoding 확인
# print('Encoding : {}'.format(r.encoding))
  
# 최대한 에러를 최소화하고 중간에 일어날 수 있는 예외를 예측해서 코딩하는게 중요함. 
if r.encoding is None:
    r.encoding = 'UTF-8'

# print('Encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode = True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    #JSON(Dict) 변화 후 타입 확인
    b = json.loads(line)
    # print(b)
    # print(type(b))

    # 정보 내용 출력
    # for k, v in b.items():
    #     print("key : {}, Values : {}".format(k,v))
    # print()
    # print()

    s.close()

r = s.get('https://jsonplaceholder.typicode.com/todos/1')
# print(r.headers)

# 본문 정보
# print(r.text)

# json 변환
# print(r.json())

# key 반환
# print(r.json().keys())
# 
# 값 반환
# print(r.json().values())

# 인코딩 반환
# print(r.encoding)

# 바이너리 정보
# print(r.content)

s.close()

# 제이슨 데이터를 인코딩하고 제이슨으로 전체 로드해서 문자열을 딕셔너리로 바꿔서 파이썬 코드로 출력함
# 두 번째 제이슨 플레이스 홀더에서는 제이슨 데이터로 내려주기 때문에 인코딩이 다 되어 있음
# 단일 레코드일 경우 위와 같이 호출하는 메소드가 존재
# 리퀘스트와 제이슨은 한 쌍으로 같이 많이 사용됨
# 쉽지만 반드시 실습 해야 하는 예제
# 
# 
# 수업 후 100개의 포스트를 받아서 for 문으로 출력해보는 예제를 해볼 것. 
 
r = s.get('https://jsonplaceholder.typicode.com/posts')

# print(r.headers)
print(r.content)