# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for key in q1:
    if key == "가을":
        print("#1 가을에 해당하는 과일은 :", q1[key])


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
if a > b and a > c:
    print("가장 큰 숫자는?", a)
elif b > a and b > c:
    print("가장 큰 숫자는?", b)
else:
    print("가장 큰 숫자는?", c)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

num = str(2468734)
print(num)
print(num[0])
if num[0] == "2" or num[0] == "4":
    print("여자")
if num[0] == "1" or num[0] == "3":
    print("남자")


# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요. 
q3 = ["갑", "을", "병", "정"]
for char in q3:
    if char == '정':
        continue
    print(char)

  # 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
line = []
for i in range(1, 100, 2):
    line.append(i)
print(line)

  # 8. # 6 ~ 10 반복문 사용(while 또는 for)


  # 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4= ["nice", "study", "python", "anaconda", "!"]
word2 = []
for word in q4:
    if len(word) >= 5:
        word2.append(word)
print(word2)

 # 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
q5ls = []
for char in q5:
    if char.islower() == True:
        q5ls.append(char)
print(q5ls)


 # 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6= ["A", "b", "c", "D", "e", "F", "G", "h"]
q6ls = []
for word in q6:
    if word.islower() == True:
        q6ls.append((word.upper()))
    else :
        q6ls.append(word.lower())
print(q6ls)

