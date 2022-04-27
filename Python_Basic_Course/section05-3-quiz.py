# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
from re import L


q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for key in q1:
    if key == "가을":
        print("#1 가을에 해당하는 과일은 :", q1[key])

# 다른 방법
for key, value in q1.items():
    if key == '가을' :
        print(value)

# 딕셔너리 형태는 키를 찾아와야 함. for 문을 통해서 반복을 했을 때, 키를 가져오는 방법을 택할 수 있다.

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for key in q2:
    if q2[key] == "사과":
        print("#2.2 사과가 있습니다")

for value in q2.values():
    if value != "사과":
        continue
    print("#2.2 사과가 있습니다")
    break    
else:
    print("#2.2 사과가 없습니다")


# 다른 방법
for k, v in q2.items():
    if v == '사과' :
        print(k, v)
        break
else:
    print('사과 없음')

#if 문과 같은 문에 넣을 수도 있지만
# for else 문으로 사용해야 함. for 문을 다 돌고 나서도 사과가 없을 경우에 출력을 해야 하기 떄문
# break를 만나면 else문이 수행되지 않고, 정상적으로 포문이 다 수행된 뒤에 else가 실행되도록 해야 하기 때문


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점


# score = int(input("점수를 입력하세요 : "))
score = 47
if score >= 81:
    print("A학점")
elif score >= 61:
    print("B학점")
elif score >= 41:
    print("C학점")
elif score >= 21:
    print("D학점")
else :
    print("E학점")


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18

# 여러개의 라인을 쓰는 것 보다 한 줄에 쓸 수 있다면 그렇게 출력하기
a, b, c = 12, 6, 18

if a > b and a > c:
    print("가장 큰 숫자는?", a)
elif b > a and b > c:
    print("가장 큰 숫자는?", b)
else:
    print("가장 큰 숫자는?", c)


# 다른 방법
best = a
if b > a:
    best = b
if c > b:
    best = c
print('best :', best)

# 나중에는 max 함수를 이용해서 쉽게 처리할 수 있음



# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

num = str(2468734)
print(num)
print(num[0])
if num[0] == "2" or num[0] == "4":
    print("여자")
if num[0] == "1" or num[0] == "3":
    print("남자")

# 다른 버전
s = '891022-2473837'
if int(s[7]) %2 == 1:
    print('남자')
else :
    print('여자')
# 이건 하기 나름. 아닌 경우라고 판단을 해도 되고. 푸는 사람마다 모두 정답이 다르다. 
# 출력값이 맞으면 잘 풀었다고 생각하면 됨.

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요. 
q3 = ["갑", "을", "병", "정"]
for char in q3:
    if char == '정':
        continue
    else:
        # print(char)
        print(char, end='') # 한 라인 안에 출력하고 싶을 때 end를 사용할 수 있다.




  # 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
line = []
for i in range(1, 101, 2):
    line.append(i)
print(line)

# 다른 방법
for n in range(1, 101):
    if n %2 != 0:
        print(n, end=',')



  # 8. # 6 ~ 10 반복문 사용(while 또는 for)


  # 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4= ["nice", "study", "python", "anaconda", "!"]
word2 = []
for word in q4:
    if len(word) >= 5:
        word2.append(word)
print(word2)

# 다른 방법
q4= ["nice", "study", "python", "anaconda", "!"]
for v in q4:
    if len(v) >= 5:
        print(v, end=', ')

 # 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
q5ls = []
for char in q5:
    if char.islower() == True:
        q5ls.append(char)
print(q5ls)

# 다른 방법
q5 = q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for v in q5:
    if v.islower():
        print(v, end=" ")

 # 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6= ["A", "b", "c", "D", "e", "F", "G", "h"]
q6ls = []
for word in q6:
    if word.islower() == True:
        q6ls.append((word.upper()))
    else :
        q6ls.append(word.lower())
print(q6ls)

# 다른 풀이
q6= ["A", "b", "c", "D", "e", "F", "G", "h"]
for v in q6:
    if v.isupper():
        print(v.lower(), end=' ')
    else:
        print(v.upper(), end=' ')


# 리스트 컴프리핸션
# 리스트를 쉽게 만들어 주는 것을 뜻함
# 리스트 컴프리헨션을 구글에서 검색하면 많이 나온다. 
# 하나의 문법. 리스트를 만드는 기법을 뜻하는데, 파이썬에서 한 줄로 쉽게 만들 수 있음
# 예를 들어 1부터 100까지 리스트를 만드려면 매번 일일히 입력해야 하는데
# 쉽게 리스트 컴프리헨션으로 만들수가 있다. 

numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)

# 위와 같이 하는게 일반적인 방법인데,
# 리스트 컴프리핸션을 쓰면 너무 쉽게 할 수 있다.
# 리스트 안에서 문법을 하는 방법인데,

numbers2 = [x for x in range(1, 101)]
print (numbers2)

# 결과값이 똑같다.
# 아래가 더 직관적이고 빠르다.
# range 내부적으로 작동하는겁니다. 1부터 101이니까. 그 1은 뒤쪽에 나오는 x이다. 
# 근데 뒤에 나오는 x를 앞에 나오는 x에 넣어라. x가 바로 어펜드가 되었다는 것.
# 그 다음에 2가 나오고 2가 앞쪽 x에 할당되고. 순서대로 100번까지.
# 결국은 1부터 100까지 100번 할당을 해서 리스트를 매우 쉽게 만들수가 있다.
# 위에서 풀었던 문제도 리스트 컴프리핸션을 이용하면 쉽게 풀리는 문제들이 있다.

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요. - 리스트컴프리핸션
q5 = ["갑", "을", "병", "정"]
ls = [v for v in q3]

q5 = [x for x in q3 if x !="정"]
# 리스트 컴프리핸션 안에 이프문도 쓸 수 있다. 
# q3에서 값을 꺼내왔어요, 값을 꺼내 온게 x죠. 그 다음에 이 x를 if 문에 대입해봐요."정"이 아니야? 그러면 오케이 트루. 그러면 앞에 엑스로 넘어와서
# 어펜드가 된다는 것.
# 그래서 이렇게 한 줄로 리스트를 만들 때 풀 수가 있다는 것. 
print(q5)

  # 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
odd = [x for x in range(1, 101) if x % 2 == 1]
print(odd)

#리스트 컴프리핸션은 어펜드 할 변수를 선언하고, 그 다음에 for문. 그 다음에 조건문이 있으면, 넣고

