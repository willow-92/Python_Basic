# Section05-1
#Beautifulsoup 사용 스크래핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
    <title> The Dormouse's story</title>
    </head>
    <body>
    <h1>this is h1 area</h1>
    <h2>this is h2 area</h2>
    <p class="title"><b>The Dormous's story</b></p>
    <p class="story">Once upon a time there were three little sisters.
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
    </p>
    <p class="stroy">
        story...
    </p>

    </body>

</html>
"""


# 예재1(Beautifulsoup 기초)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))
# print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

#p 태그 접근
# body 안에 p 태그가 3개 있지만, 아래 방식으로 접근하면 첫 번째 자식인 p 태그를 가지고 옴
p1 = soup.html.body.p
print('p1', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling
print('p2', p2)