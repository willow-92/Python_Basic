# Import Modules from collections
print("importing modules")
from asyncio.base_subprocess import BaseSubprocessTransport
from collections import Counter
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import jpype
from konlpy.tag import Komoran
from konlpy.tag import Okt
from konlpy.utils import pprint
import nltk
print("import finished")

print("requests url")
url = "https://www.linkedin.com/jobs/search?keywords=UI%2FUX&location=%EC%84%9C%EC%9A%B8%20%EC%9D%B8%EC%B2%9C%20%EC%A7%80%EC%97%AD&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
page = requests.get(url)
html = page.text
print(html)

print("start parsing")
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1').string
company = soup.find('a', class_='job-card-container__link job-card-container__company-name ember-view')
body_string = ''
print(soup)

print("done")

# 이어서 작업할 것
# 참조 :https://mokeya.tistory.com/106
# 어떤 사이트를 긁어와야 하는지 부터 확인할 것
# 대기


