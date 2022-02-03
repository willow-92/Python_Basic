# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 
# 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171

exchange_rate = {'달러' : 1167, '엔' : 1.096 , '유로' : 1268, '위안' : 171}

# 한글, 숫자, 공백 입력 검증을 위한 정규식
import re
check = '(^[\d]*[\s]{1}[가-힣]*)'

# 입력값의 검증
while True:
    currency = input('환전을 희망하는 금액과 통화를 입력하세요 ex) 100 달러, 1000 엔, 13 유로, 171 위안 (공백에 유의하세요) : ')
    if re.match(check, currency) == None:
        print("잘 못 입력하셨습니다. 형식에 맞게 입력하세요. 내가 입력 값 : ", currency)
    else:
        break

# 금액과 통화를 추출
exchange_num = int(re.sub('[^0-9]', "", currency))
exchange_str = re.sub('[^가-힣]', "", currency)

# 환전
if exchange_str in exchange_rate:
    exchanged = exchange_rate.get(exchange_str) * exchange_num
    print(currency+'(을)를 원화로 환전하면', str(format(exchanged,',')) + ' 원 입니다')

else:
    print('지원하지 않는 통화입니다')


# print('환전 희망 통화 및 금액은', currency, '이고 환전 금액은' )


# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.

# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A

# # 숫자 입력 검증을 위한 정규식
# import re
# check = '(^[\d]*$)'

# # 입력값의 숫자 검증
# while True: 
#     score = input("점수를 입력하세요 : ")
#     if re.match(check, score) == None:
#           print("잘 못 입력하셨습니다. 정수만 입력하세요. 내가 입력 값 : ", score)
#     else:
#         break

# # 점수 구간 출력
# score = int(score)
# if score < 21 :
#     print("grade is E")
# elif score < 41 :
#     print("grade is D")
# elif score < 61 :
#     print("grade is C")
# elif score < 81 :
#     print("grade is B")
# else :
#     print("grade is A")



# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# >> a
# A
# # 힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.

# # 영문 입력 및 글자수 검증을 위한 정규식
# import re
# check = '(^[a-zA-Z]{1}$)'

# # 입력값의 영문 입력 검증
# while True:
#     word = input("영문 문자 1개를 입력하세요 : ")
#     if re.match(check, word) == None:
#         print("잘 못 입력하셨습니다. 영문 문자 1개만 입력하세요. 내가 입력한 문자 : ", word)
#     else:
#         break

# # 입력값의 대소문자 변형
# if word.lower() == word:
#     print(word.upper())
# else:
#     print(word.lower())

# # 답안지의 코드
# user = input("")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())
# # True의 경우 if 문이 진행되므로 따로 == 기호를 사용하지 않아도 됨

# # 120
# # 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# # >> 좋아하는과일은? 한라봉
# # 오답입니다.

# v_fruit = list(fruit.values())

# # 국문 입력 검증을 위한 정규식
# import re
# check = '(^[가-힣]*$)'

# # 입력값의 국문 검증
# while True:
#     word = input("내가 좋아하는 과일은 무엇일까요? : ")
#     c = re.match(check, word) 
#     if c == None :
#         print('잘못 입력하셨습니다. 한글만 입력하세요. 내가 입력한 값 :' , word)
#         continue
#     else:
#         break

# if word in v_fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')



# # 119
# # 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# # >> 제가좋아하는계절은: 봄
# # 정답입니다.

# import re
# check = '(^[가-힣]*$)'

# # 입력값의 국문 검증
# while True:
#     season = input("내가 좋아하는 계절은 무엇일까요? : ")
#     c = re.match(check, season) 
#     if c == None :
#         print('잘못 입력하셨습니다. 사계절 중 하나만 입력하세요. 내가 입력한 값 :' , season)
#         continue
#     else:
#         break

# # 내가 짠 코드
# if season in list(fruit.keys()):
#     print("정답입니다")
# else:
#     print("오답입니다")

# # 제시된 정답
# season = input("제가좋아하는계절은: ")
# if season in fruit:
#     print("정답입니다.")
# else:
#    print("오답입니다.")
# 키값에 포함되어 있는지 여부를 확인할 때 딕셔너리의 키 값을 리스트 형태로 넣지 않아도 확인이 가능함


# # 118
# # 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]


# # 대소문자 구분의 영향을 받지 않도록 모두 대문자로 전처리
# trans_i_list = []
# for ticker in warn_investment_list:
#     trans_i_list.append(ticker.upper())
    
# # 영문 검사를 위한 정규식 정의
# import re
# check = '(^[a-zA-Z]*$)'

# # 입력값의 영문 검증
# while True:
#     invest = input("투자할 종목을 입력하세요 (종목명은 영문입니다): ")
#     c = re.match(check, invest) 
#     if c == None :
#         print('잘못 입력하셨습니다. 영문만 입력하세요. 내가 입력한 종목명 :' , invest)
#         continue
#     else:
#         break
        
# # 투자 경고 종목 판별
# if invest.upper() in trans_i_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# 117
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit = ["사과", "포도", "홍시"]
# >> 좋아하는 과일은? 사과
# 정답입니다.

# 더 짧은 코드
# fruit_name = input("과일을 이름을 입력하세요 : ")
# if fruit_name in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")


# for 문을 안 쓰고도 확인하는 방법이 있었음.
# fruit_name = input("과일을 이름을 입력하세요 : ")
# for word in fruit :
#     if word == fruit_name:
#         print("정답입니다")
#         break
# else:
#     print("오답입니다")

# 116
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.

# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다

# 단축시킨 코드
# import re
# check = '^([1-9]|[01][0-9]|2[0-3]):([0-5][0-9])$'
# while True:
#     time = input("시간과 분을 입력하세요 예) 09:30, 15:25 : ")
#     t = re.match(check, time)
#     if t == None:
#         print("입력이 잘 못 되었습니다. 형식에 맞게 입력해주세요 예 09:07.  내가 입력한 값: ", time)
#     else:
#         break    
# if time[-2:] == "00":
#     print("내가 입력한 값 :", time, "| 정각입니다.")
# else:
#     print("내가 입력한 값 :", time, "| 정각이 아닙니다")


# # 정수 검사
# # 시간과 분을 나눠서 받지 않는 방법에 대한 고민이 필요
# import re
# print("시간과 분을 차례대로 입력하세요. 단, 정수만 입력 하세요")
# while True:
#     hour = input("현재 '시간'을 입력하세요 ('시간'만 입력) : ")
#     min = input("현재 '분'을 입력해주세요 : ")
#     h = re.match('^([1-9]|[01][0-9]|2[0-3])$', hour)
#     m = re.match('^([1-9]|[01][0-9]|2[0-3])$', min)
#     print(h,m)
#     if h == None and m == None:
#         print("입력이 잘 못 되었습니다. 정수만 입력해주세요. 내가 입력한 값:",hour+"시",min+"분")
#     else:
#         break



# 코드가 너무 길어짐.
# print("시간과 분을 차례대로 입력하세요. 단, 정수만 입력 하세요")
# while True:
#     try: 
#         hour = int(input("현재 몇 시 입니까? ('시간'만 입력. ex) 오전 9시 = 9, 오후 3시 = 15) : "))
#         break
#     except ValueError:
#         print("정수를 입력하지 않았습니다. 정수를 입력해주세요")

# hour = str(hour)
# while True:
#     try: 
#         min = int(input("현재 몇 분 입니까? ('분'만 입력. ex) 3시 30분 = 30, 5시 9분 = 9 : ")) 
#         min = str(min)
#         break   
#     except ValueError:
#         print("정수를 입력하지 않았습니다. 정수를 입력해주세요")

# if len(hour)<2:
#     str_hour = "0" + hour
# else: str_hour = hour

# if len(min)<2:
#     str_min = "0" + min
# else: str_min = min

# if str_min == "00" or str_min == "0" :
#     print("현재시간 :", str_hour+"시", str_min+"분 정각입니다.")
# else: 
#     print("현재시간 :", str_hour+"시", str_min+"분 정각이 아닙니다.")



'''
115
사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
>> 입력값: 200
출력값: 180
>> 입력값: 15
출력값: 0
'''


# while True:
#     try:
#         num = int(input("정수를 입력하세요 : "))
#         a = num - 20
#         if a > 255:
#             print('입력한 값 :', num, "출력값 : ", 255)
#             break
#         elif a < 0:
#             print('입력한 값 : ', num, "출력값 : ", 0)
#             break
#         else:
#             print('입력한 값 : ', num, "출력값 : ", a)
#             break
#     except ValueError:
#        print("정수를 입력하지 않았습니다. 정수를 입력해주세요")


# 114
# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.

# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255
# 정답확인

# num = input("숫자를 입력하세요 : ")
# while True:
#     try:
#         a = float(num) + 20
#         if a > 255:
#             print(255)
#         print(a)
#         break
#     except ValueError:
#         num = input("숫자를 입력하지 않았습니다. 숫자를 입력하세요 : ")


# 113
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.

# num = input("숫자를 입력하세요 : ")
# while True:
#     try:
#         if float(num) % 2 == 1 :
#             print("홀수입니다")
#         else:
#             print("짝수입니다")
#         break
#     except ValueError:
#             num = input("숫자를 입력하지 않았습니다. 숫자를 입력하세요 : ")


# float 부분 리트라이
# num = input("숫자를 입력하세요 : ")
# while True:
#     try:
#         if int(num) % 2 == 1 :
#             print("홀수입니다")
#         else:
#             print("짝수입니다")
#         break
#     except ValueError:
#         try:
#             if int(float(num)) % 2 == 1 :
#                 print("홀수입니다")
#             else:
#                 print("짝수입니다")
#             break       
#         except ValueError:
#                 num = input("숫자를 입력하지 않았습니다. 숫자를 입력하세요 : ")
# # >> 30
# # 짝수


# 112
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.

# >> 숫자를 입력하세요: 30
# 40

# 정답지
# user = input("숫자를 입력하세요: ")
# print(10 + int(user))
# 정답지에서는 유저사 문자열을 넣을 상황에 대한 대비를 하지 않았음

# 2차 시도 : 성공
# num = input("숫자를 입력하세요 : ")
# while True:
#     try:
#         print(int(num)+10)
#         break
#     except ValueError:
#         try:
#             print(float(num)+10)
#             break       
#         except ValueError:
#                 num = input("숫자를 입력하지 않았습니다. 숫자를 입력하세요 : ")


# 1차 시도 실패
# from distutils.log import error
    # if int(num) == error("숫자를 입력하세요") or float(num) == error():
    #     num(input("숫자를 입력하세요 : "))
    # elif int(num) == type(int): 
    #     print(int(num) + 10)
    #     break
    # elif float(num) == float(int): 
    #     print(float(num) + 10)
    #     break
    # else: 
    #     num = input("숫자를 입력하세요 : ")

    

# # 111
# # 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.

# # >> 안녕하세요
# # 안녕하세요안녕하세요

# word = input(str("아무 글자나 입력하세요 : ㅇ"))
# print (word*2)

# 110
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")

# 3, 5

# 109
# 아래 코드의 출력 결과를 예상하라

# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")

# if Ture의 경우 기본값이 True로 반환이 되나보다...
# 답 = 1,2,4


# 108
# 아래 코드의 출력 결과를 예상하라

# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")

# Hi, there. 이 출력됨

# 107
# 아래 코드의 출력 결과를 예상하라

# if 4 < 3:
#     print("Hello World")
# 아무일도 일어나지 않음

# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.

# print(3 => 4)
# 이런 연산자는 없음. 

# 105
# 아래 코드의 결과를 예상하라.

# print ((3 == 3) and (4 != 3))
# # True

# 104
# 아래 코드의 결과를 예상하라.

# x = 4
# print(1 < x < 5)
# True

# 103
# 아래 코드의 출력 결과를 예상하라

# print(3 < 5)
# 답: True

# 102
# 아래 코드의 출력 결과를 예상하라
# print(3 == 5)
# False

# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# Bool type

# # 100 zip과 dict
# # date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# # 실행 예시:
# # >> print(close_table)
# # {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

# close_table = dict(zip(date, close_price))
# print(close_table)

# # 99 zip과 dict
# # 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.

# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# # 실행 예시:
# # >> print(result)
# # {'apple': 300, 'pear': 250, 'peach': 400}

# # i = 0
# # result = {}
# # for i in range(len(keys)):
# #     result[keys[i]] = vals[i]
# # print(result)
# # zip 메서드를 몰라서 for문을 사용

# # zip 매서드 사용하는 방법
# # result = dict(zip(keys, vals))
# # print(result)

# # 더 간단하게 해결하는 방법이 있음. 모르면 google에 찾아보자...





# # 098 딕셔너리 update 메서드
# # 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# # 실행 예시:
# # >> print(icecream)
# # {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}

# icecream.update(new_product)

# print(icecream)

# # 097 딕셔너리 values() 메서드
# # icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# # 출력 예시:
# # 6700

# a = list(icecream.values())
# b = sum(a)
# print(b)

# # 96 딕셔너리 values() 메서드
# # 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# a = list(icecream.values())
# print(a)

# # 095 딕셔너리 keys() 메서드
# # 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# a = list(icecream.keys())
# print(a)


# # 094 딕셔너리 추가
# # inventory 딕셔너리에 아래 데이터를 추가하라.

# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}

# # 이름	가격	재고
# # 월드콘	500	7
# # 실행 예시:
# # >> print(inventory)
# # {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

# inventory['월드콘'] = [500,7]
# print(inventory)

# # 092 딕셔너리 인덱싱
# # inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.

# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# # 실행 예시:
# # 300 원

# print(inventory["메로나"][1], "개")

# # 092 딕셔너리 인덱싱
# # inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.

# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}
# # 실행 예시:
# # 300 원

# print(inventory["메로나"][0],"원")

# # 091 딕셔너리 생성
# # 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.

# # 이름	가격	재고
# # 메로나	300	20
# # 비비빅	400	3
# # 죠스바	250	100

# inventory = {'메로나' : [300, 20], '비비빅' : [400, 3], '죠스바': [250, 100]}
# print(inventory)

# 090
# 다음 코드에서 에러가 발생한 원인을 설명하라.

# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'

# 딕셔너리 내에 없는 키를 인덱싱 했기 때문에 에러가 발생함.

# 089
# 다음 딕셔너리에서 메로나를 삭제하라.

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}


# del ice['메로나']
# print(ice)

# 딕셔너리 관련 주요 메소드
# 메소드                                        리턴 값
# 딕셔너리변수.keys()                           # 변수 내 모든 키 값 출력 (LIST형태 저장가능)
# 딕셔너리변수.values()                         #  변수 내 모든 벨류 값 출력 (LIST형태 저장가능)
# 딕셔너리변수.items()                          # 변수 내 모든 키+값 쌍 출력 (LIST형태 저장가능)
# 딕셔너리변수.has_key(키값)                    # 변수 내 해당 키 값의 존재여부 (True / False)
# 딕셔너리변수[키값]                            # 해당 키 값에 해당하는 value값 조회 (에러O)
# 딕셔너리변수.get(키값)                        # 해당 키 값에 해당하는 value값 조회 (에러X)
# 딕셔너리변수[키값] = vlaue값                  # 변수 내 키+value값 추가
# del 딕셔너리변수[키값]                        # 변수 내 키+value값 삭제

# # 088
# # 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# # 딕셔너리의 특징  = 수정 가능, 삭제 가능, 순서 상관 없음, 중복 불가 
# ice['메로나'] = 1300
# print(ice)

# # 087
# # 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# # 실행 예:
# # 메로나 가격: 1000

# print("메로나 가격:", ice["메로나"])

# # 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.

# # 이름	희망 가격
# # 죠스바	1200
# # 월드콘	1500

# ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
# ice["죠스바"] = 1200
# ice['월드콘'] = 1500
# print(ice)

# # 085
# # 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.

# # 이름	희망 가격
# # 메로나	1000
# # 폴라포	1200
# # 빵빠레	1800

# ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
# print(ice)

# # 084 비어있는 딕셔너리
# # temp 이름의 비어있는 딕셔너리를 만들라.
# temp = {}
# print(type(temp))

# # 083
# # 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *valid_score, b = (scores)
# print(valid_score)

# # 082
# # 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = (scores)
# print(valid_score)

# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 
# 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.

# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *a, b, c = (scores)
# print(a)
# print(b)
# print(c)

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# 이 방법이 아니었음
# i = 0
# num = []
# while i<98:
#     i = i+2
#     num.append(i)
#     print(i)
# num2 = tuple(num)
# print(num2)
# print(type(num2))

# (2, 4, 6, 8 ... 98)


# data = tuple(range(2,100,2))
# print(data)


# # 079 튜플 언팩킹
# # 다음 코드의 실행 결과를 예상하라.

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# # a, b, c 각각의 위치와 상응하는 temp내의 원소가 들어감.
# print(a, b, c)

# 예상 답안 = apple, banana, cake

# # 077
# # 다음 튜플을 리스트로 변환하라.

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# print(type(interest))

# # 또는
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest2 = list(interest)
# print(type(interest2))

# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.

# t = ('a', 'b', 'c')
# t = ('A', 'b', 'c')
# print(t)

# 튜플은 한 번 정의된 이후 원소를 변경할 수 없으므로 새로운 튜플을 만들어야 한다. 

# # 075
# # 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?

# t = 1, 2, 3, 4
# # 정답: 튜플
# # 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호가 없이 동작하는 것 또한 가능하다. 

# # 074
# # 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

# t = (1, 2, 3)
# t[0] = 'a'
# # Traceback (most recent call last):
# #   File "<pyshell#46>", line 1, in <module>
# #     t[0] = 'a'
# # TypeError: 'tuple' object does not support item assignment

# # 튜플은 원소의 값을  변경할 수 없기 때문.


# # 073
# # 숫자 1 이 저장된 튜플을 생성하라.

# num = (1,)
# print(num)
# print(type(num))
# # 하나의 데이터가 저장되는 경우 마지막에 쉼표를 입력해 주어야 함.

# # 072
# # 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)

# # 순위	영화
# # 1	닥터 스트레인지
# # 2	스플릿
# # 3	럭키

# movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
# print(movie_rank)
# print(type(movie_rank))

# # 071
# # my_variable 이름의 비어있는 튜플을 만들라.
# my_variable = ()
# print(type(my_variable))

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