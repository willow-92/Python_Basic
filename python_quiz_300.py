# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def __del__(self):
#         print("나의 죽음을 알리지마라")

#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")
# del(areum)

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")

# class Human:
#     def __init__(self, name, age, gender):
#         print("응애응애")
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def who(self):
#         print(self.name, self.age, self.gender)
  
#     def setInfo(self, name, age, sex):
#             self.name = name
#             self.age = age
#             self.sex = sex


# areum = Human("불명", "미상", "모름")
# areum.who()      # Human.who(areum)

# areum.setInfo("아름", 25, "여자")
# areum.who()      # Human.who(areum)    

# # 클래스는 나중에 다시 복습할 것.




# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자

class Human:
    def __init__(self, name, age, gender):
        print("응애응애")
        self.name = name
        self.age = age
        self.gender = gender
    
    def who(self):
        print(self.name, self.age, self.gender)
    
areum = Human("조아름", 25, "여성")
Human.who(areum)
areum.who()


# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예

# >>> areum.age
# 25

# class Human:
#     def __init__(self, name, age, gender):
#         print("응애응애")
#         self.name = name
#         self.age = age
#         self.gender = gender
# areum = Human("조아름", 25, "여성")

# print(areum.name, areum.age, areum.gender)

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.

# print("hello")

# class Human:
#     def __init__(self, name, age, gender):
#         print("응애응애")
#         self.name = name
#         self.age = age
#         self.gender = gender

# areum = Human("아름", 25, "여성")
# print(areum.name)

# 사람 클래스가 앞에서 있었고. 안에는 비어 있었다.
# 이 클래스로 부터 객체를 생성할 수 있는데, 클래스 이름을 적고 가로를 적어주면 "Human()" 메모리에 무엇인가가 생기고. 그것을 우리는 객체라고 부른다.
# 메모리에 생성된 값을 "areum"이라는 변수로 바인딩. 
# 휴먼이라는 변수가 비어있는 클래스 객체를 가르키고, 클래스 이름이 있고 괄호가 있으면 메모리에 또 무언가 비어있는 공간을 할당하게 된다. 이를 객체라고 한다. 
# 객체 - 오브젝트 - 인스턴스
# 클래스 객체, 다른 프로그램에서는 말이 안되지만, 파이썬에서 클래스 라는 것이 어떤 타입을 만들어 내는 진짜 클래스는 아니고, 타입이라는 클래스의 객체인데, 그러다 보니 메모리에 할당이 되는 것.
# 어떤 타입을 만들어내는 입장에서 어떤 역할을 하기 때문에 그렇게 부르기는 하지만, 실제로 내부적으로는 어떤 메타 클래스라고 부르는, 클래스 위에 메타클래스라는게 있는게 그게 이름이 타입이고.
# 그것의 객체임. 사실 클래스도 객체인데, 이렇게 말하면 헷갈리니까. 
# 파이썬에서 클래스도 메모리에 무언가 할당이 된다 이렇게 일단 이해를 하면 된다. 
# 이 클래스로부터 만들어진 객체도 다른 메모리 공간을 가진다.

# 다시 돌아가서 areum = Human()
# 이 생성된 공간을, 이 객체를 어떤 변수로 바인딩을 해줘야 한다.
# 이걸 바인딩 하지 않으면 객체가 소멸된다.
# 항상 객체를 생성했으면 변수로 바인딩을 해 주어야 한다. 
#

# # 252 클래스 정의
# # 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human:
#     pass

# 클래스 정의를 할 때 클래스 이름은 관례적으로 대문자를 쓴다.
# 휴먼 클래스를 정의하면 함수와 마찮가지로, 휴먼 클래스 안에 들여쓰기된 것이 아무것도 없기 때문에 비어 있고.
# 클래스 이름이 객체를 가르키게 됨. 
# 그 빈 공간 안에는 함수가 있을 수 있는데, 그 함수를 특별히 메소드라고 부른다. 

# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

# 클래스 : 붕어빵 틀과 같은 것, 객체나 인스턴스의 설계도.
# 프로그램 입장에서는 타입을 만들어 내는 도구가 바로 클래스
# 파이썬에서 int, float, string, list, tuple, dictionary 같이 어떤 타입이 있는 것.
# 그 타입을 만들어 내는 문법적인 도구가 바로 클래스.

# 그렇다면 왜 타입을 만들어 내는가? 
# 문자열 타입이 파이썬에 존재하기 때문에 .을 찍고 upper라던가 low라던가 타입 안에 있는 함수를 가져다가 사용하므로써
# 타입에 관련된 여러가지 기능들을 쉽게 사용할 수 있다. 

# datetime class의 now를 호출하면 시간이 오고
# timedelta를 쓰니까 날짜가 하루 가거나 뒤로 가거나 하는 것을 쉽게 할 수 있엇던 것 처럼
# 타입에 대해서 프로그램을 좀 더 쉽게 할 수 있도록 잘 만들어 놓은 것이 클래스

# 그 클래스로 부터 만들어진, 메모리에 할당 되는 것을 객체 또는 인스턴스라고 부른다.
# 붕어빵 틀이 클래스라면, 그 틀로부터 만들어진 붕어빵 자체를 객체나 인스턴스라고 부른다. 
# 객체가 영어로 Object이기 때문에 객체 또는 오브젝트라고 부른다.
# 인스턴스 라는 용어도 많이 쓴다.

# 일반적으로 특정 클래스로부터 만들어진 객체, 특정 클래스를 강조하고 싶지 않을 때는 객체라는 말을 쓰고
# "A라는 클래스의 객체야" 라고 할 때는 주로 인스턴스라는 용어를 사용한다.
# 문자열 클래스의 인스턴스야 이렇게 써도 되고, 문자열 객체 이렇게 사용해도 된다.

# 어떤 클래스에서 만들어진 무엇이다 라고 할 때는 일반적으로 객체라는 용어를 사용하고
# 어떤 클래스로부터 만들어졌는데, str에서 만들어졌는데, int에서 만들어 졌는지를 강조하고 싶을 때는 주로 인스턴스라는 용어를 쓴다.
# 그러나 꼭 그래야 하는 것은 아니다. 
# 그래서 그냥 객체, 오브젝트, 인스턴스가 같은 용어라고 생각하면 된다. 

# 클래스는 객체의 설계도다. 자동차로 치면 자동차의 설계도.
# 그 설계도로 부터 만들어진 자동차를 객체 오브젝트 또는 인스턴스 이렇게 3가지 형태로 부른다. 

# # 250 numpy
# # numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
# from numpy import arange
# print(arange(0.0, 5.1, 0.1))

# for i in arange(0, 5.1, 0.1):
#     print(i)


# # 249 rename 함수
# # 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
# from hashlib import new
# import os
# old_name = os.path.join("C:\\Users\\User_name\\Desktop", "새 텍스트 문서.txt")
# new_name = os.path.join("C:\\Users\\User_name\\Desktop", "바꾼 텍스트 문서.txt")
# # os.rename(old_name, new_name)
# os.rename(new_name, old_name)

# import os
# os.rename("C:/Users/User_name/Desktop/before.txt", "C:/Users/User_name/Desktop/after.txt")

# # 248 os 모듈
# # os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
# import os
# print(type(os.getcwd()), os.getcwd())


# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# import를 통해 불러오는 방식
# from ~ import를 통에 불러오는 방식
# from ~ import * ~ 안에 있는 여러 함수나 클래스, 변수를 바로 가져오는 방식
# import as xxx 모듈 이름이 너무 길 때 xxx로 

# 이름이 충돌나는 경우가 있기 때문에, 필요에 따라서 import를 쓸지 from ~ import를 사용할지 결정해야 한다
# 모듈 마다 임포트 하는 방식이 다른데, 대부분이 사용하는 사람들이 모듈을 임포트 하는 방식을 따라 사용하면 쉽게 코드를 가져다 쓸 수 있음
# 모듈에 있는 도움말을 보고, 어떤 식으로 임포트를 하는지 확인해서 코딩하는게 좋다. 



# # 246 sleep 함수
# # time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# from datetime import datetime
# from time import sleep
# for i in range(10):
#     print(datetime.now())
#     sleep(1)


# # 245 strptime
# # datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
# from datetime import datetime
# word = "2020-05-04"
# time = datetime.strptime(word, '%Y-%m-%d')
# print(type(time), time)


# # 244 strftime
# # 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.

# # 18:35:01 

# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%H:%M:%S"))

# strftime 함수는 원하는 포맷에 맞춰 출력 포맷을 설정하게 해준다. 
# strftime 함수는 시간 튜플을 받아 매개 변수 형식에 의해 결정, 읽을 수 있는 형식으로 로컬 시간의 문자열을 반환한다.

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
# from datetime import datetime, timedelta
# today = datetime.now()
# for i in range(5, 0, -1):
#     day = timedelta(days=i)
#     print(i, "일 전 = ", today.day - day.days, "일")


# 문제에서 제시한 정답
# import datetime

# now = datetime.datetime.now()

# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)

# timedelta module
# datetime 모듈의 timedelta 클래스는 기간을 표현하기 위해 사용됨
# timedelta 클래스의 생성인자는 주, 일, 시, 분, 초, 마이크로 초, 밀리초를 인자로 받음
# time delta를 통해 산술/대소 연산자를 사용할 수 있음

# 예시
# >>> from datetime import date, timedelta
# >>> week = timedelta(weeks=1)
# >>> week
# datetime.timedelta(days=7)
# >>> next_week = date.today() + week
# >>> next_week
# datetime.date(2020, 7, 25)
# >>> two_weeks = week * 2
# >>> two_weeks
# datetime.timedelta(days=14)
# >>> week < two_weeks
# True
# >>> two_weeks == timedelta(weeks=2)
# True
# >>> last_week = next_week - two_weeks
# >>> last_week
# datetime.date(2020, 7, 11)

# # 242 현재시간의 타입
# # datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
# from datetime import datetime
# print(type(datetime.now()))


# # 241 현재시간
# # datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
# from datetime import datetime
# print(datetime.now())


# 240
# 아래 코드의 실행 결과를 예측하라.

# def 함수0(num) :
#     return num * 2

# def 함수1(num) :
#     return 함수0(num + 2)

# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2)
# print(c)

# 28

# 239
# 아래 코드의 실행 결과를 예측하라.

# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)

# c = 함수2(10)
# print(c)

# 16

# 238
# 아래 코드의 실행 결과를 예측하라.

# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     return num * 10

# a = 함수1(10)
# c = 함수2(a)
# print(c)


# 140

# 237
# 아래 코드의 실행 결과를 예측하라.

# def 함수(num) :
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# 22


# 236
# 아래 코드의 실행 결과를 예측하라.

# def 함수(num) :
#     return num + 4

# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# 22


# # 235
# # 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

# # convert_int("1,234,567")
# # 1234567

# def convert_int(string : str) -> int:
#     return int(string.replace(',', ''))

# print(type(convert_int("1,234,567")),convert_int("1,234,567"))

# # 234
# # 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

# # pickup_even([3, 4, 5, 6, 7, 8])
# # [4, 6, 8]

# def pickup_even(num_list : list) -> list:
#     my_list = []
#     for i in num_list:
#         if i % 2 == 0:
#             my_list.append(i)
#     return my_list

# print(pickup_even([3, 4, 5, 6, 7, 8]))


# # 233
# # 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

# # make_list("abcd")
# # ['a', 'b', 'c', 'd']

# def make_list(string : str) -> list:
#     s_list = []
#     for i in string:
#         s_list.append(i)
#     return s_list
    
# print(make_list('abcd'))
        

# # 232
# # 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.

# # make_url("naver")
# # www.naver.com

# def make_url (string : str) -> str:
#     return "www."+ string + ".com"

# print(make_url("naver"))


# 231
# 아래 코드를 실행한 결과를 예상하라.

# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)

# 4 --> 틀렸음
# 함수 내부에서 사용한 변수는 함수 밖에서 접근할 수 없음.
# 함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용해야 함



# # 230
# # 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)



# 왼쪽: 200
# 오른쪽: 100

# # 229
# # 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)

# 왼쪽: 100 
# 오른쪽: 200



# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

#  calc_monthly_salary(12000000)
# 1000000

# def calc_monthly_salary(annual_salary):
#     print(round((annual_salary/12) - annual_salary/12 % 10))

# calc_monthly_salary(35000000)


# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.

# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

# string = "아이엠어보이유알어걸"

# return으로 특정 값을 지정해주지 않으면 none으로 적는 것이 맞음
# def print_mxn(string : str, number : int) -> none:
#     chunk_num = int(len(string)/number)
#     for i in range(chunk_num + 1) :
#         print(string[i * number : i * number + number])

# print_mxn(string, 3)




# # 226
# # 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

# # print_5xn("아이엠어보이유알어걸")
# # 아이엠어보
# # 이유알어걸

# def print_5xn(string : str) -> str:
#     for i in range(len(string)+1):
#         if i % 5 == 0 and i >= 5:
#             print(string[i-5:i])


# string = '''아이엠어보이유알어걸'''
# print_5xn(string)

# 문제가 제시한 정답
# for 문 도는 걸 최소화 한 것으로 보여져서, 더 효과적이라고 생각됨
# # def print_5xn(line):
#     chunk_num = int(len(line) / 5)
#     for x in range(chunk_num + 1) :
#         print(line[x * 5: x * 5 + 5])


# # 225
# # my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# # my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# # print_value_by_key  (my_dict, "10/26")
# # [100, 130, 100, 100]

# def print_value_by_key(dict : dict, day : str) -> list:
#     print(dict[day])


# print_value_by_key  (my_dict, "10/26")

#224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별

# def print_keys(profile : dict) -> str:
#     for i in profile.keys():
#         print(i)

# print_keys ({"이름":"김말똥", "나이":30, "성별":0})


# # 223
# # 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

# # print_even ([1, 3, 2, 10, 12, 11, 15])
# # 2
# # 10
# # 12

# def print_even(sl : list) -> int:
#     for i in sl:
#         if i % 2 == 0:
#             print(int(i))

# print_even([1, 3, 2, 10, 12, 11, 15])


# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.

# print_score ([1, 2, 3])
# # 2.0

# def print_score (*args : int) -> int:
#     print(sum(args)/len(args))

# print_score(3,6,9)

    



# # 221
# # 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.

# # print_reverse("python")
# # nohtyp


# word = "python"
# word = list(word)
# word.reverse()
# print(''.join(word))

# 슬라이싱 사용
# def print_reverse(word):
#     print(word[::-1])


# # reverse 사용
# def print_reverse(word : str) -> str:
#     word = list(word)
#     word.reverse()
#     print(''.join(word))

# reversed 사용
# def print_reverse(word : str) -> str :
#     word = reversed(word)
#     print(''.join(word))

# print_reverse('python')

# # 220
# # 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
# def print_max(a, b, c):
#     max = a
#     if a > b and a > c:
#         max = a
#     elif b > a and b > c:
#         max = b
#     else:
#         max = c
#     print(max)


# print_max(3,6,7)



# # 219
# # 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

# # print_arithmetic_operation(3, 4)
# # 3 + 4 = 7
# # 3 - 4 = -1
# # 3 * 4 = 12
# # 3 / 4 = 0.75

# def print_arithmetic_operation(a, b):
#     print(a, "+", b, "=", a + b)
#     print(a, "-", b, "=", a - b)
#     print(a, "*", b, "=", a * b)
#     print(a, "/", b, "=", a / b)

# print_arithmetic_operation(3, 4)


# # 218
# # 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
# def print_sum(num1, num2):
#     print(num1 + num2)

# print_sum(1, 2)



# # 217
# # 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

# def print_upper_price(num):
#     print(num * 1.3)

# print_upper_price(100)


# # 216
# # 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
# def print_with_smile(word):
#     print(word + ' :D')

# print_with_smile('안녕하세요')


# # 215
# # 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile(word):
#     print(word + ' :D')


# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)
# TypeError: must be str, not int
# 파라미터에 int 형태가 들어가야 하는데 str 형태를 넣어서
# 답: 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다. 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다.


# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# 함수에 필수적으로 들어가야 하는 인자가 들어가지 않아서
# 답: 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.


# 212
# 함수의 호출 결과를 예측하라.

# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)

# 7
# 15



# 211
# 함수의 호출 결과를 예측하라.

# def 함수(문자열) :
#     print(문자열)

# 함수("안녕")
# 함수("Hi")

# 안녕
# Hi



# 210
# 아래 코드의 실행 결과를 예측하라.

# def message1():
#     print("A")

# def message2():
#     print("B")

# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()

# message3()


'''
B
C
B
C
B
C
A
'''


# # 209
# # 아래 코드의 실행 결과를 예측하라.

# # def message1():
# #     print("A")

# # def message2():
# #     print("B")
# #     message1()

# # message2()


# '''
# B
# A
# '''


# # 208
# # 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)

# # print("A")
# # def message1() :
# #     print("B")
# # print("C")
# # def message2() :
# #     print("D")
# # message1()
# # print("E")
# # message2()

# '''
# A
# C
# B
# E
# D
# '''


# # 207
# # 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)

# # print("A")

# # def message() :
# #     print("B")

# # print("C")
# # message()


# '''
# A
# C
# B
# '''


# # 206
# # 아래 코드의 실행 결과를 예측하라.

# def message() :
#     print("A")
#     print("B")

# message()
# print("C")
# message()


# # 예측 결과
# '''
# A
# B
# C
# A
# B
# '''

# 205
# 아래의 에러가 발생하는 이유에 대해 설명하라.
# name 'hello' is not defined

# hello()
# def hello():
#     print("Hi")

# 함수가 선언되기 이전에 호출을 했기 때문


# # 204
# # "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coin():
#     for i in range(100):
#         print("비트코인")

# print_coin()


# # 203
# # 201번에서 정의한 print_coin 함수를 100번호출하라.
# def print_coin():
#     print("비트코인")

# for i in range(100):
#     print_coin()


# 202
# 201번에서 정의한 함수를 호출하라.

# def print_coin():
#     print("비트코인")

# print_coin()


# # 201
# # "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.

# def print_coin():
#     print("비트코인")




# # 200
# # 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.

# # 0
# profit = 0
# for i in ohlc[1:]:
#     profit += i[3] - i[0]
# print(profit)


# # 199
# # 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다. 따라서 이 거래일의 변동성은 10 (310 - 300)이다.
# # 10


# for i in ohlc[1:]:
#     if i[3] > i[0]:
#         print(i[1] - i[2])

# # 198
# # ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # >> print(volatility)
# # [40, 30, 10]

# volatility = []
# for i in ohlc[1:] : 
#     volatility.append(i[1] - i[2])
# print(volatility)


# # 197
# # ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 100
# # 310

# for i in ohlc[1:]:
#     if i[3] >= i[0] :
#         print(i[3])

# # 196
# # ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 190
# # 310

# for i in ohlc[1:]:
#     if i[3] > 150:
#         print(i[3])

# # 195
# # ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 100
# # 190
# # 310

# for close in ohlc[1:]:
#     print(close[3])


# # 194
# # 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.

# # >> print(result)
# # [
# #  [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
# #  [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
# #  [15452.163, 15052.107, 15552.177, 14902.086000000001]
# # ]

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# result = []
# for line in data:
#     sub = []
#     for col in line:
#         sub.append(col * 1.00014)
#     result.append(sub)
# print(result)

# 193
# 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.

# >> print(result)
# [2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]


# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# result = []
# for line in data:
#     for col in line:
#         result.append(col * 1.00014)

# print(result)

# # 192
# # 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# # 2000.28
# # 3050.427
# # 2050.2870000000003
# # 1980.2772
# # ----
# # 7501.05
# # 2050.2870000000003
# # 2050.2870000000003
# # 1980.2772
# # ----
# # 15452.163
# # 15052.107
# # 15552.177
# # 14902.086000000001
# # ----

# for line in data:
#     for col in line:
#         print(col * 1.00014)
#     print("----")


# # 191
# # data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# # 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.

# # 2000.28
# # 3050.427
# # 2050.2870000000003
# # ...


# for line in data:
#     for col in line:
#         print(col + col * 0.014/100)
# # 문제에서는 =  print(column * 1.00014)



# # 190
# # 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# # 101 호
# # 102 호
# # 201 호
# # 202 호
# # 301 호
# # 302 호
# # -----

# for floor in apart:
#     for unit in floor:
#         print(unit, "호")
# print("-----")


# # 189
# # 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# # 101 호
# # 102 호
# # -----
# # 201 호
# # 202 호
# # -----
# # 301 호
# # 302 호
# # -----

# for floor in apart:
#     for unit in floor:
#         print(unit, "호")
#     print("-----")


# # 188
# # 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# # 101 호
# # -----
# # 102 호
# # -----
# # 201 호
# # -----
# # 202 호
# # -----
# # 301 호
# # -----
# # 302 호
# # -----

# for floor in apart:
#     for unit in floor:
#         print(unit, "호")
#         print("-----")





# # 187
# # 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# # 302 호
# # 301 호
# # 202 호
# # 201 호
# # 102 호
# # 101 호

# for floor in apart[::-1]:
#     for unit in floor[::-1]:
#         print(unit, "호")


# # 186
# # 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# # 301 호
# # 302 호
# # 201 호
# # 202 호
# # 101 호
# # 102 호


# for floor in apart[::-1]:
#     for unit in floor:
#         print(unit, "호")

# # 185
# # 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# # 101 호
# # 102 호
# # 201 호
# # 202 호
# # 301 호
# # 302 호

# for i in range(3):
#     for j in range(2):
#         print(apart[i][j], "호")


# print("------------------")
# # 문제가 제시한 정답
# for row in apart:
#     for col in row:
#         print(col, "호")
        
# # 184
# # 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 
# # 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.

# # 10/10	80	110	70	90
# # 10/11	210	230	190	200

# stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}


# # 183
# # 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 
# # 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 
# # 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.

# # 시가	종가
# # 100	80
# # 200	210
# # 300	330


# stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}


# # 182
# # 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.

# # 시가	종가
# # 100	80
# # 200	210
# # 300	330

# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]


# # 181
# # 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.

# # 101호	102호
# # 201호	202호
# # 301호	302호

# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]



# # 180
# # 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, 
# # low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.

# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range (5):
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)
    

# # 179
# # 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.

# my_list = [100, 200, 400, 800, 1000, 1300]
# # 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 같은 방식으로 나머지 데이터의 평균을 출력한다.

# print(my_list[0:3])

# for i in range(len(my_list)-2):
#     print((my_list[i] + my_list[i+1] + my_list[i+2])/3)

# print("------------------------------------------------")

# for i in range(len(my_list)-2):
#     print(sum(my_list[i:i+3])/3)

# print("------------------------------------------------")

# import numpy

# for i in range(len(my_list)-2):
#     print(numpy.mean(my_list[i:i+3]))

# print("------------------------------------------------")

# import statistics
# for i in range(len(my_list)-2):
#     print(statistics.mean(my_list[i:i+3]))

# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333



# # 178
# # 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.

# my_list = [100, 200, 400, 800]
# # 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다. 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.

# # 100
# # 200
# # 400

# for i in range(len(my_list)-1):
#     print(my_list[i+1] - my_list[i])

# # 177
# # 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.

# my_list = ["가", "나", "다", "라"]
# # 라 다
# # 다 나
# # 나 가

# print(len(my_list)-1)

# for i in range(len(my_list)-1):
#     print(my_list[-(i+1):-(i+3):-1])


# 0 -1
# 1 -2
# 2 -3
# 3 -4


# # 176
# # 리스트를 아래와 같이 출력하라.

# my_list = ["가", "나", "다", "라", "마"]
# # 가 나 다
# # 나 다 라
# # 다 라 마

# for i in range(len(my_list)-2):
#     print(my_list[i:i+3])


# # 175
# # my_list를 아래와 같이 출력하라.

# my_list = ["가", "나", "다", "라"]
# # 가 나
# # 나 다
# # 다 라

# for i in range(0,3):
#     print(my_list[i], my_list[i+1])

# # 문제에서 제시한 다양한 방법
# for i in [0, 1, 2]:
#     print(my_list[i])

# for i in [0, 1, 2]:
#     print(my_list[i], my_list[i+1])

# for i in range( len(my_list) - 1 ) :
#     print(my_list[i], my_list[i+1])

# for i in range( 1, len(my_list) ) :
#     print(my_list[i-1], my_list[i])

# # 174
# # 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.

# price_list = [32100, 32150, 32000, 32500]
# # 100 32150
# # 110 32000
# # 120 32500

# for i in range(1,4):
#     print(i*10 + 90, price_list[i])

# # 문제에서 제시한 정답
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])


# 173
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.

# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500

# for i in range(4):
#     print(abs(i-3), price_list[i])

# # 문제가 제시한 정답
# price_list = [32100, 32150, 32000, 32500]
# for i, data in enumerate(price_list):
#     print(i, data)

# enumerate 함수
# 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가짐
# enumerate는 "열거하다" 라는 의미
# 이 함수는 순서가 있는 자료형 (리스트, 셋, 튜플, 딕셔너리, 스트링)을 입력으로 받아 인덱스 값을 포함하는 enumerate객체를 리턴한다.
# for 문과 함께 자주 사용된다. 



# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.

# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500

# # 171
# # 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.

# price_list = [32100, 32150, 32000, 32500]
# # 32100
# # 32150
# # 32000
# # 32500

# for i in range(4):
#     print(price_list[i])

# # 170
# # 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# total = 1
# for i in range (1,11):
#     total *= i
# print(total)

# # 169
# # 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# # 합: 25

# total = 0
# for i in range(1,11,2):
#     total += i
# print(total)

# print('---------------')

# total = 0
# for i in range(1,11):
#     if i % 2 == 1:
#         total += i 
# print(total)

    


# # 168
# # 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# # 합 : 55

# total = 0
# for i in range(1,11):
#     total = i + total
# print(total)

## 문제가 제시한 정답
# hab = 0
# for i in range(1, 11):
#     hab += i
# print ("합 :", hab)

# # 167
# # 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.

# # 3x1 = 3
# # 3x3 = 9
# # 3x5 = 15
# # 3x7 = 21
# # 3x9 = 27

# for i in range(10):
#     if i % 2 == 1:
#         print("3x{} = {}".format(i, 3*i))

# # 문제가 제시한 정답
# ange(1, 10, 2)를 사용해서 홀수를 만듭니다.
# num = 3
# for i in range(1, 10, 2) :
#     print (num, "x", i, " = ", num * i)

# 혹은 조건문을 사용해서 해결할 수도 있습니다.

# num = 3
# for i in range(1, 10) :
#     if i % 2 == 1 :
#         print (num, "x", i, " = ", num * i)

# # 166
# # 구구단 3단을 출력하라.

# # 3x1 = 3
# # 3x2 = 6
# # 3x3 = 9
# # 3x4 = 12
# # 3x5 = 15
# # 3x6 = 18
# # 3x7 = 21
# # 3x8 = 24
# # 3x9 = 27

# for i in range(1,10):
#     print(3, "x", i, " = ", 3*i)

# print("--------------------")

# for i in range(1,10):
#     print("3x{} = {}".format(i, 3*i))



# # 165
# # for문을 사용해서 아래와 같이 출력하라.

# # 0.0
# # 0.1
# # 0.2
# # 0.3
# # 0.4
# # 0.5
# # ...
# # 0.9

# for i in range(10):
#     print(i / 10,)

# # 164
# # 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.

# for i in range(99, -1, -1):
#     print(i)

# print('------------------------------')

# for i in range(100):
#     print(99-i)

# # 163
# # 1부터 30까지의 숫자 중 3의 배수를 출력하라.

# # 3 
# # 6 
# # 9 
# # 12 
# # 15 
# # 18 
# # 21 
# # 24 
# # 27 
# # 30

# for i in range(1,31):
#     if i % 3 == 0:
#         print(i)

# print('---------------------------')

# for i in range(3,31,3):
#     print(i)

# 162
# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050
# 참고) range의 세번 째 파라미터는 증감폭을 결정합니다.

# >> print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]

# for i in range(2002,2051,4):
#     print(i)

# # 161
# # for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.

# for i in range(100):
#     print(i)



# # 160
# # 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# # intra.h
# # intra.c
# # define.h

# for i in 리스트 : 
#     if i.split(".")[1] == "h" or i.split(".")[1] == "c":
#         print(i)

# # 159
# # 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# # intra.h

# for i in 리스트:
#     if i.split(".")[1] == "h":
#         print(i)


# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro

# for i in 리스트 :
#     print(i.split(".")[0])

# 문제에서 제시한 정답
# split() 메서드는 문자열을 입력된 구분자로 분할해서 리스트로 반환합니다. 다음 예제 코드의 결과를 예상해봅시다.
# 변수 = "abcdef"
# print(변수.split("c"))
# 입력된 구분자 ("c")로 문자열을 분할해서 "ab"와 "def"를 리스트에 저장합니다.

# ['ab', 'def']
# split() 메서드를 사용해서 마침표를 구분자 (".")로 문자열을 분할합니다. 그리고 0번 인덱스에 들어있는 파일 이름만 화면에 출력합니다.

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for 변수 in 리스트:
#   split = 변수.split(".")
#   print(split[0])  

# 157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.

# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
# (참고) upper() 메서드는 문자열을 대문자로 변경합니다.

# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC

# for i in 리스트:
#     i = i.replace(i[0], i[0].upper())
#     print(i)

# 문제에서 제시한 정답
# 지금까지 배웠던 내용을 모두 응용해야 하는 문제입니다. 첫 번째 단어만 대문자로 변경해야하기 때문에 아래의 순서로 처리해야 합니다.
# 1) 인덱싱으로 첫번째 문자를 가져온다.
# 2) upper() 함수로 대문자로 변경한다.
# 3) 변경한 대문자와 나머지 문자를 이어붙인다.
# 정리한 내용을 코드로 작성하면 다음과 같습니다.
# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#   첫글자 = 변수[0]              # 1)
#   대문자 = 첫글자.upper()     # 2)
#   print(대문자 + 변수[1:])      # 3)
# 간단하기 때문에 한줄에 코드를 작성해도 좋습니다.

# for 변수 in 리스트:
#   print(변수[0].upper() + 변수[1:])

# # 156
# # 리스트에서 소문자만 화면에 출력하라.

# 리스트 = ["A", "b", "c", "D"]
# # b
# # c

# for i in 리스트:
#     if i.islower():
#         print(i)

# # 155
# # 리스트에서 대문자만 화면에 출력하라.

# 리스트 = ["A", "b", "c", "D"]
# # A
# # D
# # (참고) isupper() 메서드는 대문자 여부를 판별합니다.

# # >> 변수 = "A"
# # >> 변수.isupper()
# # True
# # >> 변수 = "a"
# # >> 변수.isupper()
# # False

# for i in 리스트:
#     if i.isupper():
#         print(i)

# # 154
# # 리스트에서 세 글자 이상의 문자를 화면에 출력하라

# 리스트 = ["I", "study", "python", "language", "!"]
# # study
# # python
# # language

# for i in 리스트:
#     if len(i) > 3 :
#         print(i)

# # 153
# # 리스트에서 20 보다 작은 3의 배수를 출력하라

# 리스트 = [13, 21, 12, 14, 30, 18]
# # 12
# # 18

# for i in 리스트:
#     if i < 20 and i % 3 == 0 :
#         print(i)

# # 152
# # for문을 사용해서 3의 배수만을 출력하라.

# 리스트 = [3, 100, 23, 44]
# # 3

# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# # 151
# # 리스트에는 네 개의 정수가 저장돼 있다.

# 리스트 = [3, -20, -3, 44]
# # for문을 사용해서 리스트의 음수를 출력하라.

# # -20
# # -3

# for i in 리스트:
#     if i < 0:
#         print(i)

# # 150
# # 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]
# # for문을 사용해서 다음과 같이 출력하라.

# # 라
# # 다
# # 나
# # 가

# for i in 리스트[::-1]:
#     print(i)

# # 149
# # 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]
# # for문을 사용해서 다음과 같이 출력하라.

# # 가
# # 다
# for i in 리스트[0::2]:
#     print(i)


# # 148
# # 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]
# # for문을 사용해서 다음과 같이 출력하라.

# # 나
# # 다
# # 라


# for i in range(3):
#     print(리스트[i+1])

# for i in 리스트[1:]:
#     print(i)


# # 147
# # 리스트에는 세 개의 숫자가 바인딩돼 있다.

# 리스트 = [1, 2, 3]
# # for문을 사용해서 다음과 같이 출력하라.

# # 3 x 1 = 3
# # 3 x 2 = 6
# # 3 x 3 = 9

# for i in 리스트:
#     print("3 x", i, "=", 3*i)


# 문제가 제시한 정답
# 1장에서 배운 문자열 함수를 활용하면 코드가 더욱 읽기 쉬워집니다.

# 리스트 = [1, 2, 3]
# for 변수 in 리스트:
#   print("3 x {} = {}".format(변수, 3 * 변수))


# # 146
# # 리스트에는 세 개의 숫자가 바인딩돼 있다.

# 리스트 = [1, 2, 3]
# # for문을 사용해서 다음과 같이 출력하라.

# # 3 x 1
# # 3 x 2
# # 3 x 3

# for i in 리스트:
#     print("3 x", i)



# # 145
# # 리스트에 동물 이름 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']
# # for문을 사용해서 동물 이름의 첫 글자만 출력하라.

# # d
# # c
# # p

# for word in 리스트:
#     print(word[0])

# # 144
# # 리스트에는 동물이름이 문자열로 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']
# # 동물 이름과 글자수를 다음과 같이 출력하라.

# # dog 3
# # cat 3
# # parrot 6

# for 동물이름 in 리스트:
#     print(동물이름, len(동물이름))

# # 143
# # 리스트에 주식 종목이름이 저장돼 있다.

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# # 저장된 문자열의 길이를 다음과 같이 출력하라.

# 6
# 4
# 4

# for i in 리스트:
#     print(len(i))

# # 142
# # for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.

# 리스트 = ["김밥", "라면", "튀김"]
# # 오늘의 메뉴: 김밥
# # 오늘의 메뉴: 라면
# # 오늘의 메뉴: 튀김

# for menu in 리스트:
#     print("오늘의 메뉴 : ", menu)

# # 141
# # 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.

# 리스트 = [100, 200, 300]
# 110
# 210
# 310

# for price in 리스트:
#     print(price + 10)


# # 140
# # 다음 코드를 for문으로 작성하라.

# print("-------")
# print("-------")
# print("-------")
# print("-------")

# print("\n")
# for i in range(4):
#     print("-------")

# # 139
# # 다음 코드를 for문으로 작성하라.

# print("++++")
# print(10)
# print(20)
# print(30)


# var = [10, 20, 30]
# print("++++")
# for i in var:
#     print(i)
    

# # 138
# # 다음 코드를 for문으로 작성하라.

# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")

# var = [10, 20, 30]
# for i in var:
#     print(i)
#     print("-------")

# 137
# 다음 코드를 for문으로 작성하라.

# print(10)
# print(20)
# print(30)

# var = [10, 20, 30]
# for i in var:
#     print(i)


# # 136
# # 다음 코드를 for문으로 작성하라.

# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

# var = [10, 20, 30]
# for i in var:
#     print(i)

# # 135
# # for문을 풀어서 동일한 동작을 하는 코드를 작성하라.

# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)

# 변수 = "A"
# b = 변수.lower()
# print("변환:", b)

# 변수 = "B"
# b = 변수.lower()
# print("변환:", b)

# 변수 = "C"
# b = 변수.lower()
# print("변환:", b)
  

# # 133
# # 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.

# for 변수 in ["A", "B", "C"]:
#   print(변수)

# print("A")
# print("B")
# print("C")

# 132
# for문의 실행결과를 예측하라.

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")
# 정답
# #####
# #####
# #####


# 131
# for문의 실행결과를 예측하라.

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 정답 :
# 사과
# 귤
# 수박

# 파이썬 반복문


# #130

# # 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

# from numpy import s_
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# # btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# # Key Name	Description
# # opening_price	최근 24시간 내 시작 거래금액 (시가)
# # closing_price	최근 24시간 내 마지막 거래금액 (종가)
# # min_price	최근 24시간 내 최저 거래금액
# # max_price	최근 24시간 내 최고 거래금액

# fluc = float(btc['max_price']) - float(btc['min_price'])
# s_price = float(btc['opening_price'])
# print('변동폭 : ', s_price + fluc, '\n최고가 : ', float(btc['max_price']))

# if fluc + s_price > float(btc['max_price']):
#     print('상승장')
# else :
#     print('하락장')


# 129
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 유효하지 않은 주민등록번호입니다. 

# 해당 문제를 보기 전에 이미 아래 문제들에서 유효성 검사에 대한 코드 작업을 진행함. 

# weighted_num = '234567892345'
# new_total = 0
# total = 0
# import re
# check = '\d{6}-\d{7}'

# while True:
#     ssn = input('주민등록번호를 입력하세요 (예: 821010-1635210) :')
#     if re.match(check, ssn) == None:
#         print('주민등록번호 형식이 잘못 되었습니다. 다시 입력해주세요.')
#     else:
#         ssn = re.sub('[^0-9]','',ssn)
#         for i in range(12):
#             new_total = new_total + int(weighted_num[i])*int(ssn[i])
#         check_num = 11-(new_total%11)
#         if len(str(check_num))>1 :
#             check_num = check_num%10          
#         if str(check_num)[-1] != str(ssn[-1]):
#             print('유효하지 않은 주민등록번호 입니다. 다시 입력해주세요.')
#             new_total = 0
#             continue
#         else:
#             print('유효한 주민등록 번호입니다.')
   
#     break

# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
#
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# >> 주민등록번호: 821010-1635210
# 서울이 아닙니다.
# >> 주민등록번호: 861010-1015210
# 서울 입니다.

# 최종 정리

# weighted_num = '234567892345'
# new_total = 0
# total = 0
# import re
# check = '\d{6}-\d{7}'

# while True:
#     ssn = input('주민등록번호를 입력하세요 (예: 821010-1635210) :')
#     if re.match(check, ssn) == None:
#         print('주민등록번호 형식이 잘못 되었습니다. 다시 입력해주세요.')
#     else:
#         ssn = re.sub('[^0-9]','',ssn)
#         for i in range(12):
#             new_total = new_total + int(weighted_num[i])*int(ssn[i])
#         check_num = 11-(new_total%11)
#         if len(str(check_num))>1 :
#             check_num = check_num%10          
#         if str(check_num)[-1] != str(ssn[-1]):
#             print('유효하지 않은 주민등록번호 입니다. 다시 입력해주세요.')
#             new_total = 0
#             continue
#         else:
#             if int(ssn[7:9]) <= 8:
#                 print('서울입니다.')
#             elif int(ssn[7:9]) > 8 :
#                 print('서울이 아닙니다.')
#     break



# 디버그를 몰라 하나 하나 프린트문 찍어서 짠 코드
# 가중치 정의
# weighted_num = '234567892345'
# new_total = 0
# total = 0
# import re
# check = '\d{6}-\d{7}'

# while True:
#     ssn = input('주민등록번호를 입력하세요 (예: 821010-1635210) :')
#     if re.match(check, ssn) == None:
#         print('주민등록번호 형식이 잘못 되었습니다. 다시 입력해주세요.')
#     else:
#         ssn = re.sub('[^0-9]','',ssn)
#         for i in range(12):
#             print('    weighted_num[i] = ',int(weighted_num[i]),'    ssn[i] = ',int(ssn[i]))
#             print(weighted_num[i], '*', int(ssn[i]), '=', int(weighted_num[i])*int(ssn[i]))
#             print('new_total = ',int(weighted_num[i])*int(ssn[i]),"+",new_total,'=', new_total + int(weighted_num[i])*int(ssn[i]))
#             new_total = new_total + int(weighted_num[i])*int(ssn[i])
#         print("new_total%11 = ",new_total%11)
#         print("11 - ",new_total%11,"= ",11-(new_total%11))
#         check_num = 11-(new_total%11)
#         print('나머지 자리 수는 = ', len(str(check_num)))
#         if len(str(check_num))>1 :
#             check_num = check_num%10
#             print("나머지 자리 숫자가 2자리 이상이기 때문에 10으로 나눈 나머지를 사용함")
#             print("check_num%10 = ", check_num%10)
#         else: 
#             print("나머지 자릿수가 1 이므로 10으로 나눈 나머지값을 사용하지 않고 그대로 ",check_num, "활용")
#         print("유효성 검증을 위한 숫자는", str(check_num)[-1], "입력한 주민등록 번호의 맨 뒷 자리는", str(ssn)[-1])
#         if str(check_num)[-1] != str(ssn[-1]):
#             print('유효하지 않은 주민등록번호 입니다. 다시 입력해주세요.')
#             new_total = 0
#             continue
#         else:
#             if int(ssn[7:9]) <= 8:
#                 print('서울입니다.')
#             elif int(ssn[7:9]) > 8 :
#                 print('서울이 아닙니다.')
#     break







# # 127
# # 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# # 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

# # >> 예시 - 주민등록번호: 821010-1635210
# # 남자

# # 주민등록번호에는 각 숫자에 대응하는 가중치가 있고, 값에 따라 유효성을 검증하기 위한 규칙이 있다는 것을 알게 됨
# # 문제에서 입력값의 형태를 지정하였으므로, 입력값의 형식에 맞게 입력했는지 검증하고, 주민등록번호의 유효성을 검사하기로 함.
# # 가중치는 주민등록번호의 순서에 따라 2 3 4 5 6 7 8 9 2 3 4 5 라고 함
# # 먼저 마지막 숫자는 제외하고, 기본코드의 각 12자리와 가중치를 모두 곱하여 합하여야 함
# # 합한 값을 11로 나눈 나머지 값을 구해야 함
# # 11에서 그 나머지 값을 뺀다. 단 나머지 자리가 2자리인 경우 이를 10을 나눈 나머지 값을 구해야 함   -> 이 부분을 놓쳤음. 나중에 코드 수정할 것
# # 나머지의 1의 자리 값과 주민등록번호 마지막 자리 값이 맞아야 유효한 주민등록번호이다.

# # 가중치 정의
# weighted_num = '234567892345'
# total = 0

# import re
# check = '\d{6}-\d{7}'

# while True:
#     ssn = input('주민등록번호를 입력하세요 (예: 821010-1635210) :')
#     if re.match(check, ssn) == None:
#         print('주민등록번호 형식이 잘못 되었습니다. 다시 입력해주세요.')
#     else:
#         ssn = re.sub('[^0-9]','',ssn)
#         for i in range(12):
#             total = total + int(weighted_num[i])*int(ssn[i])
#         check_num = (11-(total%11))%10
#         if str(check_num)[-1] != ssn[-1]:
#             print('유효하지 않은 주민등록번호 입니다. 다시 입력해주세요.')
#             total = 0
#             continue
#         else:
#             if ssn[6] == '1' or ssn[6] == '3':
#                 print('남성입니다.')
#             else:
#                 print('여성입니다.')
#     break




# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

# -	      0	      1	     2   	3   	4   	5     6       7      8	     9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
# >> 우편번호: 01400
# 도봉구

# num = {'010': '강북구',
#        '011': '강북구',
#        '012': '강북구',
#        '013': '도봉구',
#        '014': '도봉구',
#        '015': '도봉구',
#        '016': '노원구',
#        '017': '노원구',
#        '018': '노원구',
#        '019': '노원구',
#        }

# # 입력값의 숫자 검증을 위한 정규식
# import re
# check = '\d'

# # 입력값 검증
# while True:
#     post = input('우편번호를 5자리를 입력하세요 (예: 01400) : ')
#     if re.match(check, post) == None:
#         print('우편번호를 잘못 입력하셨습니다. 다시 입력해주세요 : ')
#     else:
#         break   

# # 우편번호의 지역구 출력
# print(num.get(post[:3]))

# # 문제에서 제공하는 정답
# 우편번호 = input("우편번호: ")
# 우편번호 = 우편번호[:3]
# if 우편번호 in ["010", "011", "012"]:
#     print("강북구")
# elif 우편번호 in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")

# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.

# telecom = {'011': 'SKT',
#            '016': 'KT',
#            '019': 'LGU',
#            '010': '알수없음'}

# # 사용자 휴대전화 입력 검증식
# import re
# check = '\d{3}-\d{3,4}-\d{4}'

# # 입력값 검증
# while True:
#     num = input('핸드폰 번호를 입력하세요 (예: 000-0000-0000) : ')
#     if re.match(check, num) == None:
#         print('번호 입력 형식이 잘 못 되었습니다. 다시 입력해주세요.')
#     else:
#         break

# # 통신사 출력
# print('당신은', telecom.get(num[:3]), '사용자 입니다.')

# 문제에서 제공하는 답
# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

# # 124
# # 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# # >> input number1: 10
# # >> input number2: 9
# # >> input number3: 20
# # 20

# while True:
#     num1 = input('첫 번째 정수를 입력하세요 : ')
#     num2 = input('두 번째 정수를 입력하세요 : ')
#     num3 = input('세 번째 정수를 입력하세요 : ')
#     try :
#         num1 = int(num1)
#         num2 = int(num2)
#         num3 = int(num3)
#         break

#     except ValueError:
#         print('잘못된 값을 입력하였습니다. 내가 입력한 값:\n1 번: [', num1, ']\n2 번: [', num2,']  \n3 번: [', num3,']')

# if num1 >= num2 and num1 >= num3:
#     print('가장 큰 숫자는 : ', num1)
# elif num2 >= num1 and num2 >= num3:
#     print('가장 큰 숫자는 : ', num2)
# else:
#     print('가장 큰 숫자는 : ', num3)


# # 문제에서 제공하는 답
# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)


# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다.
# 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171

# exchange_rate = {'달러' : 1167,
#                  '엔' : 1.096 ,
#                  '유로' : 1268,
#                  '위안' : 171}

# # 한글, 숫자, 공백 입력 검증을 위한 정규식
# import re
# check = '(^[\d]*[\s]{1}[가-힣]*)'

# # 입력값의 검증
# while True:
#     currency = input('환전을 희망하는 금액과 통화를 입력하세요 ex) 100 달러, 1000 엔, 13 유로, 171 위안 (공백에 유의하세요) : ')
#     if re.match(check, currency) == None:
#         print("잘 못 입력하셨습니다. 형식에 맞게 입력하세요. 내가 입력 값 : ", currency)
#     else:
#         break

# # 금액과 통화를 추출
# exchange_num = int(re.sub('[^0-9]', "", currency))
# exchange_str = re.sub('[^가-힣]', "", currency)

# # 환전
# if exchange_str in exchange_rate:
#     exchanged = exchange_rate.get(exchange_str) * exchange_num
#     print(currency+'(을)를 원화로 환전하면', str(format(exchanged,',')) + ' 원 입니다')

# else:
#     print('지원하지 않는 통화입니다')


# #문제에서 준 정담
# 환율 = {"달러": 1167,
#         "엔": 1.096,
#         "유로": 1268,
#         "위안": 171}
# user = input("입력: ")
# # 이 부분이 중요해 보임. num과 currency에 공백을 기준으로 나누어 담으라는 코드
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")

# # 정답을 참고해서 더 단순화 한 코드
# exchange_rate = {'달러' : 1167,
#                  '엔' : 1.096 ,
#                  '유로' : 1268,
#                  '위안' : 171}

# # 한글, 숫자, 공백 입력 검증을 위한 정규식
# import re
# check = '(^[\d]*[\s]{1}[가-힣]*)'

# # 입력값의 검증
# while True:
#     currency = input('환전을 희망하는 금액과 통화를 입력하세요 ex) 100 달러, 1000 엔, 13 유로, 171 위안 (공백에 유의하세요) : ')
#     if re.match(check, currency) == None:
#         print("잘 못 입력하셨습니다. 형식에 맞게 입력하세요. 내가 입력 값 : ", currency)
#     else:
#         break

# # 금액과 통화를 추출
# exchange_num, exchange_str = currency.split()
# try :
#     print(currency+'(을)를 원화로 환전하면', float(exchange_num) * exchange_rate[exchange_str], ' 원 입니다')

# except :
#     print("지원하지 않는 통화입니다.")


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


# '''
# 115
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 180
# >> 입력값: 15
# 출력값: 0
# '''


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
