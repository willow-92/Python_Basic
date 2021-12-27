# # 060
# # 다음 리스트의 평균을 출력하라.

# nums = [1, 2, 3, 4, 5]
# # 실행 예:
# # 3.0

# # 방법 1
# a = sum(nums)
# b = len(nums)
# c = a/b
# print(c)

# # 방법2
# import numpy as np
# a = np.array(nums)
# print(np.mean(a))

# # 059
# # 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# # 리스트에 저장된 항목이 전부 몇개인지 확인하기 위해서 len()함수를 사용할 수 있다. 

# # 058
# # 다음 리스트의 합을 출력하라.

# nums = [1, 2, 3, 4, 5]
# # 실행 예:
# # 15

# print(sum(nums))

# # 057
# # 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)

# nums = [1, 2, 3, 4, 5, 6, 7]
# # 실행 예:
# # max:  7
# # min:  1#

# print("max: ", max(nums))
# print("min: ", min(nums))

# # 056
# # lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]

# # 실행 예:
# # >> langs
# # ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

# lang3 = lang1 + lang2
# print(lang3)

# # 055
# # movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2:]
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# print(movie_rank)
# del movie_rank[2]
# print(movie_rank)
# # del을 이용하여 리스트에서 원소를 삭제할 수 있음. 리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱 되므로 여러 값을 삭제할 때는 어떤 값이
# # 먼저 삭제된 후 남은 원소들의 순서를 새로 고려한 후 삭제해야 함. 


# 리무브 매서드는 한 번에 하나의 값 밖에 삭제할 수 없음. 
# movie_rank = ['닥터 스트레인지', '스플릿', '슈퍼맨','배트맨']
# movie_rank.remove('스플릿', '베트맨')
# print(movie_rank)

# # movie_rank 리스트에서 '럭키'를 삭제하라.
# # 특정 원소 삭제시 2가지 방법을 사용할 수 있음. 
# # Index를 알고 있다면 del을, 원소이 값을 알고 있다면 remove를 사용할 수 있음.

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
# print(movie_rank)


# # movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1,"슈퍼맨") #리스트는 수정이 되므로 따로 변수를 지정해서 반환 값을 넣어주지 않아도 괜춘
# print(movie_rank)

# #리스트의 insert(인덱스, 원소) 메서드를 사용하면 특정 위치에 값을 끼워넣기 할 수 있다. 

# # 052 리스트에 원소 추가
# # 051의 movie_rank 리스트에 "배트맨"을 추가하라.

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append('베트맨')
# print(movie_rank)

# movie_rank.pop()
# print(movie_rank)

# additional = ['베트맨']
# movie_rank.extend(additional) #extend 메서드를 사용하기 위해서는 추가하려는 원소를 다른 리스트 속에 넣어 놔야 함. 
# print(movie_rank)

# # 051 리스트 생성
# # 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)

# # 순위	영화
# # 1	닥터 스트레인지
# # 2	스플릿
# # 3	럭키

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# print(movie_rank)
# # 영화 제목은 문자열로 표현 가능함. 여러 개의 값을 저장하기 위해 리스트 자료형을 사용

# # 050 rstrip 메서드
# # 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

# data = "039490     "
# data1 = data.rstrip()
# print(data1)

# data = "039490    -----"
# data1 = data.rstrip("-")
# print(data1)

# # rstrip 매서드에서 아무 값도 주지 않으면 공백을 삭제. 특정 문자를 넣으면 해당 문자와 공백을 함께 삭제함

# # 049 split 메서드
# # 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.

# date = "2020-05-01"
# date1 = date.split('-')
# print(date1)

# # 048 split 메서드
# # 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.

# ticker = "btc_krw"
# ticker1 = ticker.split('_')
# print(ticker1)

# # 047 split 메서드
# # 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.

# a = "hello world"
# print(a.split())

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.

# file_name = "2020_보고서.xlsx"
# print(file_name.startswith('2020'))
# print(file_name.startswith(('1999','2021')))

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# file_name = "report.xls"
# print(file_name.endswith(("xlsx", "xls")))
# # 위와 같이 endswith을 사용하여 두 가지 조건이 만족되는지를 확인하기 위해서는 괄호가 한 번 더 들어가 줘야 함. 




# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))
# endswith을 사용하면 파일 끝이 특정 문자로 끝나는지 확인하여 불린 형태로 반환하여 줌

# # 043 capitalize 메서드
# # 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
# v1 = "hello"
# v2 = v1.capitalize()
# print(v2)

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.

# ticker = "BTC_KRW"
# ticker1 = ticker.lower()
# print(ticker1)


# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.

# ticker = "btc_krw"
# ticker1 = ticker.upper()
# print(ticker1)
# upper 매서드를 호출하면 문자열을 대문자로 만들 수 있음. 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환됨.


# # 030 replace 메서드
# # 아래 코드의 실행 결과를 예상해보세요.
# # 예상 결과 = abcd
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# 문자열은 변경할 수 없는 자료형
# replace 메서드를 사용하면 원본은 그대로 둔 채 변경된 새로운 문자열 객체를 리턴해줌. 


# print(string) # 029 replace 메서드
# # 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

# string = 'abcdfe2a354a32a'
# # 실행 예:
# # Abcdfe2A354A32A

# print(string.replace("a", "A"))

# # 028 문자열은 immutable
# # 아래 코드의 실행 결과를 예상해보세요.
# # 예상 실행결과 = 에러나옴. 바꿀 수 없음
# # 문자열은 수정할 수 없음. 
# lang = 'python'
# lang[0] = 'P'
# print(lang)



# # 027 문자열 다루기
# # url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

# url = "http://sharebook.kr"
# url2 = "https://www.googole.co.kr"
# url3 = "https://www.naver.com"
# # 실행 예:
# # kr

# # print(url.rfind(".")) #rfind 함수는 찾고자 하는 문자가 등장하는 가장 마지막 위치를 반환한다. 
# # print(url2.rfind("."))
# # print(url2[22:])

# # 풀어서 만들어보기
# domain = url.rfind(".")
# print(url[domain +1 :])

# # 함수에 넣어서 출력하기
# def domain(x):
#     print(x[x.rfind(".") + 1 :])

# domain(url)
# domain(url2)
# domain(url3)

# # 기존 정답
# # split을 사용해야 했음
# url_split = url.split(".")
# print(url_split[-1])

# # split을 활용하여 함수 만들기
# def domain_split(x) :
#     url_split = x.split(".")
#     print(url_split[-1])

# domain_split(url3)


# # 026 문자열 다루기
# # 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# # 실행 예
# # 01011112222
# phone_number = "010-1111-2222"
# print(phone_number.replace("-",""))

# # 025 문자열 치환
# # 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

# phone_number = "010-1111-2222"
# # 실행 예
# # 010 1111 2222

# print(phone_number.replace("-"," "))

# # 024 문자열 슬라이싱
# # 문자열을 거꾸로 뒤집어 출력하세요.

# string = "PYTHON"
# # 실행 예:
# # NOHTYP

# # reversed 사용법 정확하게 모르고 있음. 복습할 것. 리스트 형태로 반환해서 사용 가능
# print(list(reversed(string)))
# print(string[::-1])


# # 023 문자열 인덱싱
# # 아래의 문자열에서 '홀' 만 출력하세요.

# string = "홀짝홀짝홀짝"
# # 실행 예:
# # 홀홀홀

# print(string[::2])

# # 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

# license_plate = "24가 2210"
# # 실행 예: 2210

# print(license_plate[len(license_plate)-4:len(license_plate)]) # 타이핑이 많음
# print(license_plate[4:]) # 세야 함
# print(license_plate[-4:]) # 개인적으로 가장 깔끔한 코드라고 생각


# # 021 문자열 인덱싱
# # letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

# letters = 'python'
# # 실행 예
# # p t

# print(letters[0], letters[2])


# # 020 파이썬 계산
# # 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
# # MI = Monthly Installment
# AC_MI = 48584
# Total_Amount = AC_MI * 36
# print(Total_Amount)

# # 019 문자열을 정수로 변환
# # year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

# year = "2020"
# year_int = int(year)
# print(year_int, year_int + 1, year_int + 2)

# # 018 문자열을 실수로 변환
# # 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
# num_str = 15.79
# num_float = float(num_str)
# print(num_float + 0.1, type(num_float))



# # 017 정수를 문자열 100으로 변환
# # 정수 100을 문자열 '100'으로 변환해보세요.

# num = 100
# num_str = str(num)
# print(num_str, type(num_str))

# # 016 문자열을 정수로 변환
# # 문자열 '720'를 정수형으로 변환해보세요.

# num_str = "720"
# num_int = int(num_str)
# print(num_int + 1, type(num_int))


# # 015 type 함수
# # type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.

# # >> a = 128
# # >> print (type(a))
# # <class 'int'>
# # 아래 변수에 바인딩된 값의 타입을 판별해보세요.

# # >> a = "132"
# # 예상 결과값 = str
# a = "132"
# print(type(a))


# # 014 파이썬을 이용한 값 계산
# # 아래 코드의 실행 결과를 예상해보세요.

# # >> 2 + 2 * 3 
# # 예상 결과값 = 8
# print(2 + 2 * 3)


# # 013 문자열 출력
# # 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.

# # >> s = "hello"
# # >> t = "python"
# # 두 변수를 이용하여 아래와 같이 출력해보세요.

# # 실행 예:
# # hello! python

# s = "hello"
# t = "python"
# print(s+"!", t) #콤마 표시 다음에 오는 변수에는 자동으로 한 칸 띄어쓰기가 된 다는 사실 기억하기

# # 012 변수 사용하기
# # 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# market_cap = 298000000000
# price = 50000
# PER = 15.79

# print(market_cap, type(market_cap))
# print(price, type(price))
# print(PER, type(PER))


# #011 변수 사용하기
# # 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
# samsung = 50000
# samsung_value = samsung * 10
# print(samsung_value)


# #010 연산 결과 출력
# # 5/3의 결과를 화면에 출력하세요.
# print(5/3)


# # 009 print 줄바꿈
# # 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# # print("first");print("second")
# print("first", end="");print("second")

# # 008 print 기초
# # print() 함수를 사용하여 다음과 같이 출력하세요.
# # naver/kakao/sk/samsung
# print('naver', 'kakao', 'sk', 'samsung', sep='/')

# # # 007 print 기초
# # # print() 함수를 사용하여 다음과 같이 출력하세요.
# # naver;kakao;sk;samsung
# print('naver', 'kakao', 'sk', 'samsung', sep=";")
# # print 함수의 sep 인자로 ";" 를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.

# # 006 print 여러 데이터 출력
# # print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
# print ("오늘은", "일요일")
# # 오늘은 일요일
# # 중간에 콤마 없이 띄어쓰기 한칸이 있고, 자료가 출력


# # 005 print 탭과 줄바꿈
# # 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
# # print("안녕하세요.\n만나서\t\t반갑습니다.")
# print("안녕하세요.\n만나서\t\t반갑습니다.")
# # \n은 줄바꿈을 한다.
# # \t는 탭 역할을 한다.


# # 004 print 기초
# # 화면에 "C:\Windows"를 출력하세요.
# print('"C:\Window"')

# # 003 print 기초
# # 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# # 신씨가 소리질렀다. "도둑이야".
# print('신씨가 소리질렀다. "도둑이야".')


# # 002 print 기초
# # 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
# print("Mary's cosmetics")

# # 001 print 기초
# # 화면에 Hello World 문자열을 출력하세요.
# print("Hello World")