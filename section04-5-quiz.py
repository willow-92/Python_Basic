# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print('1. ', len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('2. ', 'apple', 'orange', 'banana', 'lemon')

# 3. 화면에 * 기호 100개를 표시하세요.
print('3. ', '*' * 100)
# 문자열도 연산이 가능함.

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
a = "30"
print('4. ', type(a))

b = int(a)
print('4. ', b, type(b))

c = float(a)
print('4. ', b, type(c))

d = complex(a)
print('4. ', d,type(d))

e = str(a)
print('4. ', e, type(e))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
a = 'Niceman'
print('5. ', a[-3:])

a_idx = a.index("man")
# 인덱스는 내가 찾고자하는 문자의 첫 부분의 자리값을 리턴해줌
print('5. ', a[a_idx:a_idx+3])


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
a = 'Strawberry'
print('6. ', a[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
num = "010-7777-9999"
print(num[0:3] + num[4:8] + num[9:13])


print('7. ', num.replace("-",""))

# 정규표현식
# 따로 공부해야 하는 부분
import re #regular
print("7. ", re.sub('[^0-9]','', num))
# ^ 는 아니다 라는 의미
# 숫자가 아닌 것을 제외하겠다

# 정규표현식은 여러 언어에서도 공통적임.

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
url = 'http://daum.net'
print('8. ', url.replace('http://',''))
print('8. ', url[7:])
url_index = url.index('daum')
print('8 ', url[url_index:])
import re 
print('8, ', re.sub('^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$', '',url))
# 다양한 방식으로 표현이 가능함. 


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
a = 'NiceMan'
print('9. ', a.upper())
print('9. ', a.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
a = 'abcdefghijklmn'
print('10. ', a[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
a = ["Banana", "Apple", "Orange"]
a.remove('Apple')
print('11. ', a)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
a = (1, 2, 3, 4)
b = list(a)
print('12. ', b)

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
a = {'성인': 100000, '청소년': 70000, '아동': 30000}
print('11. ', a)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
a['소아'] = 0
print('11. ', a)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print('15. ', a.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print('16. ', a.values())

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
