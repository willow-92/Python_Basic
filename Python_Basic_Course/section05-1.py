# section 05-1
# 파이썬 흐름제어(제어문) flow
# 조건문 실습

# 조건문에서 중요한 것은 불린

print(type(True))
print(type(False))

# 불린을 기억해둘 것. 

# 예 1.
if True :
    print("YES")

if False :
    print("No")
else:
    print("YES2")


# 관계연산자
# >, >=, <, <=, ==, != (같지 않다)

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)

# 참 거짓의 종류를 True와 False를 사용했다.
# 그러나 경우에 따라서 다르게 사용할 수 있음
# 참 : "내용", [내용], (내용), {내용}, 1
# 내용이 있는 문자열, 내용이 있는 리스트, 내용이 있는 튜플, 내용이 있는 딕셔너리, 숫자 1

# 거짓 : "", [], (), {}, 0

city = ""

if city: 
    print("True")
else:
    print(">>>False")

# 논리연산자
# and or not

a = 100
b = 60
c = 15

print('and :', a > b and b > c)
print('or : ', a >b or c > b)
print('not : ', not a >b)
print(not False)
print(not True)

# 산술, 관계, 논리 연산자 까지 했음. 
# 이것들의 우선순위가 있음.
# 산술 > 관계 > 논리 순서로 적용

print('ex1 : ', 5+ 10 > 0 and not 7 +3 == 10)
# and 조건이 있기 때문에 5 + 10 >0 을 먼저 계산하고, 뒤 쪽도 10이 나와서 트루지만 not이 붙었기 때문에 False가 됨. 
# 즉 True and Flase가 되었기 때문에 False를 리턴함.

s1 = 90
s2 = 'A'

if s1 > 90 and s2 =='A':
    print('합격하셨습니다')
else :
    print('불합격 입니다.')

# 다중 조건문
num = 90
if num >= 90:
    print("num 등급 A", num)
    
elif num >= 80:
    print("num 등급 B", num)

elif num >= 70:
    print("num 등급 c", num)
elif num >= 60:
    print("num 등급 d", num)
else :
    print("꽝")


# 중첩조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print('A class')
    elif height >= 160:
        print('B class')
    else :
        print('reject')

# 참 거짓 종류 기억할 것



    