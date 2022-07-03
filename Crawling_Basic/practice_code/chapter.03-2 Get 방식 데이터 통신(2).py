#section 03-2
# 기본 스크래핑 실습
# Get 방식 데이터 통신(2) - RSS

# 정부기관에서 제공하는 RSS 데이터를 수신해서 콘솔에 출력하는 실습


# 지난 시간에는 가장 중요한 get 방식.
# 웹에서 Http 방식으로 서버와 통신을 할 때, get 방식과 post방식 중에 get방식은 url 주소 창에 서버에서 필요로 하는 어떤 쿼리를 스트림 형태로 페이로드,
# 주소 창에 실어서 서버에 요청을 해서 응답을 받을 수 있따.
# 수신된 데이터를 디코딩 하고
# 요청 url 생성하는 작업까지 해봤음. 

# 행안부 사이트에서 RSS를 제공하는데,
# RSS는 그 사이트를 맨날 방문하는 사이트가 있으면, 사이트를 방문하지 않고도 새로운 글이나 소식이 업데이트 되었는지, 다양한 형태 주로 xml 형태로 읽을 거리를 제공해줌
# 메일로 새로운 글이 등록되었다는 피드가 오면 새로운 글로 가는
# 사이트에서 보내주는 소식지. 
# 연속으로 4번을 요청해서 출력
# 요청 url 정보를 분석하고
# 행안부에서 정보를 잘 가져왔는지 xml 데이터까지 확인해보기


import urllib.request
import urllib.parse
import pprint

# 행정 안전부 : https://www.mois.go.kr
# 행정 안전부 RSS API URL
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간 확인
# print(params)

# 연속해서 4회 요청

for c in params:
    # 파라미터 출력
    # print(c)
    # URL 인코딩
    param = urllib.parse.urlencode(c)
    
    # URL 완성
    url = API + "?" + param

    # URL 출력
    print("url :", url)

    # 요청
    res_data = urllib.request.urlopen(url).read()
    # pprint.pprint(res_data) # 디코딩이 안 된 상태. 알아볼 수 없음.

    # 수신 후 디코딩
    contents = res_data.decode("utf-8")

    # 출력
    print("")
    print("="*150)
    print("")
    print(contents)

# 데이터를 가져왔으면 이 컨텐츠를 가지고 파일에 써도 되고. 
# 나중에 뷰티풀스프로 파싱을 해서 제목만 가져다가 디비에 넣어도 되고.
# 엑셀 저장을 해도 되고. 
# 가져 오면 일단 반은 성공하는 것. 
# 가져와서 내 컴퓨터에 있기 때문에.

