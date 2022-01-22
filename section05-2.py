# section 05-2
# 파이썬 흐름제어 (반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
# while 문의 경우 while 뒷쪽에 조건이 들어감
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1 # 1씩 계속 증가된다는 의미


#range 함수는 0부터 시작해서 10 미만의 값 까지 반복을 함.   
for v2 in range(10): 
        print("v2 is : ", v2)

# 0부터 시작하는 것이 싫을 떄, range 시작 숫자, 끝나는 숫자 보다 1 더 큰 숫자
for v3 in range(1,11):
    print("v3 is", v3)

# 1 ~ 100의 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
    print("sum1 : ", sum1)
    print("cnt1 : ", sum1)
print('1 ~ 100 : ', sum1)

# 1 ~ 100의 합 더 쉬운 방법
print('1 ~ 100 : ', sum(range(1,101)))
print('1 ~ 100 : ', sum(range(1, 101, 2)))
# range 함수의 3번째 인수는 건너뛰는 단위, 위 코드의 경우 2 단위씩 건더뛰어서 더한다는 의미

# 시퀀스 (순서가 있는) 자료형 반복
# 반복문을 통해 순서에 맞게 반복 할 수 있음
# 문자열, 리스트, 튜플, 집합, 딕셔너리 -> 반복 가능
# iterable, 이런 것들을 이터러블 이라고 함. 
# iterable을 리턴하는 함수 : range, reversed, enumerate, fileter, map, zip

names = ["kim", "park", "cho", "choi", "yoo"]

# 아래와 같이 하면 순서에 맞게 리턴을 해서 값이 name 안으로 들어가게 됨. 
for name in names:
    print("yout name is : ", name)

word = "dreams"

for s in word:
    print("word : ", s)

my_info = {
    "name" : "kim",
    "age" : "33",
    "city" : "Seoul"
}

# 딕셔너리 내에서 키만 반복함 (기본값)
for key in my_info:
    print("my_info", key)

# 밸류만 반복함 (값)
for key in my_info.values():
    print("my_info", key)

# 키만 반복함 (키)
for key in my_info.keys():
    print("my_info", key)

# 키값과 밸류값을 모두 (키, 값)
for k, v in my_info.items():
    print("my_info: ", k, v)

# 위에 네가지 패턴에 대해서 모두 알고 있어야 함. 

name = "KennRY"

# 대문자는 소문자로 바꾸고, 소문자는 대문자로 바꿔라
# 어떻게 할 수 있을까? 

# 대소문자 변경 관련된 내용 확인
print(name[0].isupper())
print(name[0])
print(name.lower())
print(name[0].lower())


# 일단 강의 보기 전에 어떻게 할 수 있을지 고민


upper = []

for i in name:
    if i.isupper() == True:
        upper.append(i.lower())
    else:
        upper.append(i.upper())
print("".join(upper))

# 위치마다 대문자인지 소문자인지 검사, 대문자면 소문자로, 소문자면 대문자로 바꾸어 리스트에 담음
# 담은 리스트를 조인하여 출력

# 강의에서 짠 코드

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper()) 

# 강의 코드는 출력만
# 내가 짠 코드는 리스트에 담는 부분이 추가됨  
# True 인지 검증하는 부분이 있는데, 그렇게 하지 않고, 대문자이면 바로 바꾸는 부분
# 구지 붙이지 않아도 되는 부분인데 붙었음.  
# 개선하면 아래와 같음

# upper = []

# for i in name:
#     if i.isupper():
#         upper.append(i.lower())
#     else:
#         upper.append(i.upper())
# print("".join(upper))


# 33 찾는 코드 (직접)
cnt = 0
# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]
for i in numbers:
    cnt+= 1
    if i == 33:
        break
print("찾는 숫자의 위치는 = ", cnt,"번째")

# 33 찾는 코드 (강의)
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found 33!")

# for 문의 특수한 문법. for 문에도 else가 있음. for -else 구문
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found 33!")

else: 
    print("not found 33...")


# for문의 break가 작동했을 경우에는 else가 작동하지 않고, break가 작동하지 않으면 else가 작동함
# 반복문이 정상적으로 수행 된 경우 else 블럭 수행
# break가 들어갔다는 것은 정상적으로 수행되지 않은 것이기 때문에 else가 수행되지 않음


# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
# 하나의 리스트에 여러가지 데이터 타입을 넣을 수 있음. 상당히 유연함
# 이 리스트 안에 실수형이 있는지 찾고 싶다면? 어떻게 찾을까? 

# 직접
for i in lt:
    if type(i) == float:
        print("exist")

# float형태를 제외한 나머지를 출력하고 싶다면?
for i in lt:
    if type(i) is float:
        continue
    print(type(i), i)

# 컨티뉴를 만나면 바로 다음 순회할 값으로 이동을 한다.
# 컨티뉴를 만나면 하위 부분은 실행하지 않음. 

name = "Niceman"
print(list(reversed(name)))