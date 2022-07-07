# Import Modules from collections
print("importing modules")
from asyncio.base_subprocess import BaseSubprocessTransport
from collections import Counter
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import jpype
from konlpy.tag import Komoran
from konlpy.tag import Okt
from konlpy.utils import pprint
import nltk
print("import finished")

ua = UserAgent()

headers = {
    'User-agent' : ua.random,
    'refferer' : 'https://www.linkedin.com/jobs/view'
}

print("requests url")
url = "https://www.linkedin.com/jobs/view/3150157200"
page = requests.get(url, headers=headers)
html = page.text


# print(html)


print("start parsing")
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1').string
company = soup.find('span', class_='jobs-unified-top-card__company-name')
content = soup.find('div', class_='jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch')
body_string = ''
print(title)
print(company)
print(content)

# print("done")

# 이어서 작업할 것
# 참조 :https://mokeya.tistory.com/106
# 어떤 사이트를 긁어와야 하는지 부터 확인할 것
# 대기

# 동적인 자료는 셀레늄 활용이 필요하다는 글을 발견
# 다시 확인해볼 것

# 우선 requests를 통해서 받아오는 html 안에 똑같은 태그 이름을 가진 텍스트가 존재하지 않음.
# 개발자 도구에서는 보이는데 requests로 가져오는 html에는 왜 보이지 않는지 확인할 필요가 있음.