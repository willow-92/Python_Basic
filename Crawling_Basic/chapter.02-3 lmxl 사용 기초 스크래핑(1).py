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

def main():
    '''
    네이버 메인 뉴스 스탠드 스크래핑 메인 함수
    '''


    # 스크래핑 대상 URL
    response = requests.get("https://www.naver.com") # Get 방식과 Post 방식이 있음

    # 신문사 링크 리스트 획득
    # 직접 함수를 제작.
    # 만약 URL retrive를 썻다면 다운로드하고 데이터가 끝나는데, 
    # 데이터를 중간에 담아서 어떤 함수에 넘길 때 많이 사용함
    # requests.get이 아니라 urlopen 함수로 읽어와서 아래 함수로 넘겨도 괜찮음. 
    urls = scrape_news_list_page(response)

    # 개발자 도구에서 네이버 헤더에 요청하는 처음 방식은 GET 방식으로 요청함
    # 이럴 때는 url 주소상의 쿼리 조건을 네이버 서버에 넘겨서 사용자가 뭘 클릭했고, 페이지가 어디에 있고. 
    # 이런 것들은 거의 get 방식. 로그인이 필요하지 않음. 
    # 보안이 엄격한 은행권이나, 로그인할 때는 주로 숨겨져 있는, 데이터 헤더 정보나 바디정보가 숨겨져 있음. 
    # 이럴때는 POST 방식을 사용함
    # 당연히 POST 메소드도 있음.
    # 
    # 결과 출력
    for url in urls:
        # url 출력
        print(url)
        # 파일 쓰기
        # 생략
        # 

def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect(''):
        
        pass


# 스크래핑 시작
if __name__ == "__main__":
    main()
