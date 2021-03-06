# section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)
# pip install lxml, requests, cssselect

from os import link
from re import T
import requests
from lxml.html import fromstring, tostring
import pprint
# fromstring =  웹에서 스윙된 데이터를 스트링으로 바꿔주는 것
# tostring = 중간에 제대로 되었는지 확인할 때 

import os


# 세션을 바꾸는 코드
# 세션이란?
# 웹은 한 번 요청을 하고 응답이 오면 연결이 끊김
# 세션을 이용해서 이 사람이 로그인을 했는지를 판단함. 쿠기 정보를 활용하지만,
# 브라우저를 껏다가 다시 켜도 구글의 경우 로그인이 연결되어 있고,
# 한 번 로그인 한 상태로 껏다가 다시 켜도 로그인이 되어 있는 경우가 세션을 사용한 것
# 세션을 사용하지 않으면 로그인을 하고 다른 사이트에 갔을 때 로그인 정보를 활용할 수 없기 떄문에
# 서버에서 일정한 플로우를 가지고 정보를 가지고 있는 것
# 지금은 로그인이나 이런게 필요 없이 눈에 보이는 정보를 가져오지만
# 세션 정보를 이용해야 하는 경우가 있음




def main():
    '''
    네이버 메인 뉴스 스탠드 스크래핑 메인 함수
    '''

    # 세션 사용
    session = requests.Session()
    
    # 스크래핑 대상 URL
    response = session.get("https://www.naver.com/") 
    
    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)
    pprint.pprint(urls)
    with open('./Python_Basic/Crawling_Basic./scrap.txt', 'w') as f:
        f.writelines(urls)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력
    # for url in urls:
    #     print(url)

def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    news_name = []
    news_link = []



    print("=============================================")
    print("신문사 이름 포함 엑스패스 가져오기")
    print("=============================================")
    print('')
# 신문사 이름 추출
    for a in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]/a[@class="thumb"]'):
        
        # a 구조 확인
        # print(a)
        
        # a 문자열 출력

        # print(tostring(a, pretty_print=True))
        
        name = extract_contents(a)
        news_name.append(name)
        
        
        # 딕셔너리 삽입
    

    print("=============================================")
    print("신문사 링크 포함 엑스패스 가져오기")
    print("=============================================")
    print('')

    for b in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]/div[@class="popup_wrap"]/a[@class="btn_popup"]'):
        # print(tostring(b, pretty_print=True))

        link = extract_link(b)
        news_link.append(link)
 
    for i in range(len(news_name)):
        urls[news_name[i]] = news_link[i]

    return urls
    

def extract_contents(dom):
    name = dom.xpath('./img')[0].get('alt')
    return(name)


def extract_link(dom):
    link = dom.get("href")
    return(link)
    # print(link)


# 스크래핑 시작
if __name__ == "__main__":
    main()


# 이번 작업에서는 세션의 개념이 나왔음
# 단방향, 일회성 통신. 요청하고 끊기고. 응답하고 끊기고.
# 불특정 다수가 요청하기 때문에.
# 서버에서 이 사람이 누구인지 확인하기 위해서 세션을 연결해놓고 쿠키 정보 등을 활용해서 사용자를 구분한다는 것.

# 가장 중요한 것은 xpath로 바꿨다는 것
