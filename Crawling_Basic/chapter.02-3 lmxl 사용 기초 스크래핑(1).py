# section 02-3 lxml 사용 기초 (1)

# 파싱 - 구조에 맞게 원하는 데이터를 가져오는 방법
# 특수문자를 제거하거나, 한글로 된 부분만 가져오거나 하는 것.
# 그 중에 많이 사용하는 lxml
# pip install lxml

# 네이버 뉴스 스탠드 스크래핑
# 신문사 정보 리스트 출력
# CSS 선택자 활용
import requests
import lxml.html

# def main():
#     '''
#     네이버 메인 뉴스 스탠드 스크래핑 메인 함수
#     '''


#     # 스크래핑 대상 URL
#     response = requests.get("https://news.naver.com/") # Get 방식과 Post 방식이 있음


#     # 신문사 링크 리스트 획득
#     # 직접 함수를 제작.
#     # 만약 URL retrive를 썻다면 다운로드하고 데이터가 끝나는데, 
#     # 데이터를 중간에 담아서 어떤 함수에 넘길 때 많이 사용함
#     # requests.get이 아니라 urlopen 함수로 읽어와서 아래 함수로 넘겨도 괜찮음. 
#     urls = scrape_news_list_page(response)

#     # 개발자 도구에서 네이버 헤더에 요청하는 처음 방식은 GET 방식으로 요청함
#     # 이럴 때는 url 주소상의 쿼리 조건을 네이버 서버에 넘겨서 사용자가 뭘 클릭했고, 페이지가 어디에 있고. 
#     # 이런 것들은 거의 get 방식. 로그인이 필요하지 않음. 
#     # 보안이 엄격한 은행권이나, 로그인할 때는 주로 숨겨져 있는, 데이터 헤더 정보나 바디정보가 숨겨져 있음. 
#     # 이럴때는 POST 방식을 사용함
#     # 당연히 POST 메소드도 있음.
#     # 
#     # 결과 출력
#     for url in urls:
#         # url 출력
#         print(url)
#         # 파일 쓰기
#         # 생략
#         # 

# def scrape_news_list_page(response):
#     # URL 리스트 선언
#     urls = []

#     # 태그 정보 문자열 저장
#     root = lxml.html.fromstring(response.content)
#     # print(root)
#     # print(response.content)

#     # css selector install 할 것(pip install cssselect)
#     # 네이버 뉴스를 메인에서 가져오는 것에 실패하여 뉴스 페이지 내에 있는 URL을 가져 오는 것으로 변경하여 시도
#     for a in root.cssselect('.cjs_channel_card .cjs_ctitle._item_title a.cjs_ctitle_a'):
#     #     # 링크
#         url = a.get('href')
#         urls.append(url)
#     return urls

# CSS 선택자에 대해서 검색을 해보고 포스팅 해 놓은 자료들을 살펴보고 읽어볼 것. 
# CSS 온라인 셀렉터에서 여러 데이터들을 클릭해보고, 특정 값을 가져오기 위해서는 어떤 아이디를 가져올 수 있는지 확인을 해보는 작업을 해볼 것. 



# 강의 내에 존재했던 네이버 메인 페이지에서 긁어오는 방법을 새롭게 시도하기 위해 
# 주석 없이 코드를 다시 복사하여 작성해보기

def main():
    response = requests.get("https://news.naver.com/") 
    urls = scrape_news_list_page(response)

    for url in urls:
        print(url)

def scrape_news_list_page(response):
    urls = []
    root = lxml.html.fromstring(response.content)

# 실패. 추후 다시 확인 필요
    for a in root.cssselect('.thumb_area .thumb_box._NM_NEWSSTAND_THUMB._NM_NEWSSTAND_THUMB_press_valid .popup_wrap > a.btn_popup'):
        url = a.get('href')
        urls.append(url)
    return urls


# 스크래핑 시작
if __name__ == "__main__":
    main()



