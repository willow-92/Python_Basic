# chapter02-2 urlopen 함수 기초
# urlretrieve로 웹에서 원하는 정보를 다운로드 받는 작업을 진행함
# urlopen 함수는 꼭 알아둬야 하는 함수
# 지난 시간에는 다운로드까지 자기가 했지만, urlopen은 다운로드를 하지 않음.
# 다운은 하지 않지만, 다른 함수에서 urlopen로 웹에서 수신된 데이터를 가지고 있고, 
# 이 자체를 다른 함수에서 매개변수로 받는 패턴을 많이 사용하기 때문에 반드시 알아야 함

# urlib.request 예외처리
# 기존 소스코드 변경
# 예외처리
# 기타 리팩토링

# 지난 시간과 같은 기능을 하지만 urlopen으로 기능하도록 함수를 재구성

import urllib.request as req
from urllib.error import URLError, HTTPError
# 인터넷 접속시 에러가 났을 경우를 대비하기 위한 것. 
# 에러처리가 프로그래밍 할 때 중요함
# 예외처리를 하지 않으면 어떤 오류인지 알기도 어렵고.
# 예외처리를 하면 빈번하게 발생하는 에러를 확인하고 수정할 수 있음. 


# 다운로드 경로 및 파일명
path_list = ["C:/Users/kyung.song/PycharmProjects/Python_Basic/Crawling_Basic/practice_files/test1.jpg", "C:/Users/kyung.song/PycharmProjects/Python_Basic/Crawling_Basic/practice_files/index.html"]

# 다운로드 리소스 url
target_url = ["https://dimg.donga.com/ugc/CDB/SHINDONGA/Article/5f/9a/4c/f6/5f9a4cf615cfd2738de6.jpg", "https://google.com"]
for i, url in enumerate(target_url):
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("----------------------")

        # 상태 정보 중간 출력
        print('Header info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print("----------------------")
        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download failed")
        print("URL error Reason : ", e.reason)
        

    # 성공
    else:
        print()
        print("Download Succeed.")

# 골격을 완성한 상태
# 타겟 URL을 순회를 하면서 2번 요청을 해서 한 번이라도 에러가 나면 잡고 중단이 되지만, 
# 설정해 놓은 에러로 코드를 보고 어디가 문제인지 알 수 있고.
# 정상적으로 진행되었을 경우 else문이 돌면서 통과


# 02-1보다는 좀 더 pythonic한 코드를 짰음.
# 순회를 하면서 동시에 순차대로 2번을 요청했고. 요청하고 싶은 url을 여러개 넣을 수도 있음
# 나중에 코드를 좀 더 보기 좋게, 가독성 있게 만들수 있음.
# 지금 수준에서는 이 정도로 작성
# 순서대로 urlopen으로 가져온 데이터를 담아서 컨텐츠를 썼음(write)
# With로 사용하면 쓰기가 끝나고 자동으로 닫히기 때문에, 자주 사용함
# 모두 성공하면 else 구문이 찍히고
# 에러가 발생하면 except 부분에서 에러를 잡고. 
# 코드 자체의 흐름을 이해할 수 있으면 실력이 부쩍 늘어난다.
# 나중에 어느 순간 자연스럽게 이해가 되는 순간이 반드시 온다. 
# 조급해 하지 말고 실행이 완벽하게 되는 것을 목표로 코드를 작성하는 것을 연습할 것. 

# urlopen 함수는 수신된 데이터를 담을 수 있다는 것.
# 이 자체가 함수 클래스 객체이기 때문에 인포에서 이런 것들을 출력하는 것. 
# 코드를 시간을 아끼면서 생산성있게 제공하는 메소드를 활용하는 것이 중요함. 

