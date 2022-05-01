# # section04-3
# # 파이썬 데이터 타입 (자료형)
# # 리스트, 튜플

# # 리스(순서O, 중복O, 수정O, 삭제O)
# # 순서가 있음. 중복도 허용. 수정도 가능. 삭제도 가능함. 
# # 파이썬에서 딕셔너리와 더불어 가장 많이 쓰이는 자료형


# name1 = 'lee'
# name2 = 'Park'
# # 이렇게 매번 변수로 이름을 입력하는 것은 효율적이지 못 함. 
# # 그래서 자료 구조를 이용해야 함. 
# # 리스트는 그릇. 배열. 



# a = [] # 선언은 대괄호로 할 수 있음.
# b = list() # 명시적으로 리스트라고 표현 하는 것도 가능
# c = [1, 2, 3, 4] # 정수의 모음으로 볼 수 있음. 계속 선언 가능
# d = [10, 100, 'pen', 'Banana', 'Orange'] # 데이터 타입이 달라도 담을 수 있음. # 리스트 안에 숫자와 스트링을 모두 담을 수 있음
# e = [10, 100, ['pen', 'Banana', 'Orange']] # 리스트 안에 리스트로 중첩해서 사용 가능. 데이터 타입이 다른데도 리스트 안에 담을 수 있음. 

# # indexing
# print(d[3]) #예상 답안 : 바나나 
# print(d[-3]) # 예상 답안 : 펜
# print(d[0] + d[1]) # 예상 답안 : 110
# print(e[2][1]) # 예상 답안: 바나나
# print(e[-1][-2]) # 예상 답안: 바나나

# # slicing # 리스트로 반환을 해서 나옴
# print(d[0:3]) # 예상 답안 : [10, 100, 'pen']
# print(e[2][1:3]) #예상 답안 : [Banana, Orange]

# # 연산
# # 리스트와 리스트를 합쳐줌. 즉 리스트가 확장이 됨
# print(c + d) # 예상 답안 : [1, 2, 3, 4, 10, 100, 'pen', 'Banana', 'Orange']
# print(c * 3) # 예상 답안 : [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# # print(c[1]+'hi') 에러가 발생함. 왜? int와 스트링을 더했으니까 연산이 되지 않음
# print(str(c[1]) + 'hi') # 연산을 하기 위해서는 형변환을 통해서 동일한 타입으로 맞추어 줘야 함. 그래서 c[1]을 스트링으로 변환한 다음 연산을 진행

# # 리스트 수정, 삭제
# c[0] = 77 # c[0]에 77을 할당. 그러면 c[0]에 있던 기존 값인 1이 77로 수정됨
# print('c[0] = ', c[0])
# print('c = ', c)

# c[1:2] = [100, 1000, 1000] 
# # 해당 자리에 있는 원소를 100, 1000, 1000으로 대체함. C의 [1:2] 이므로 C[1]과 동일. 기존 c[1]은 2였으나,
# # 해당 코드를 실행하고 나면 c[1] 자리에 들어있던 2가 100, 1000, 1000으로 바뀌게 됨. 3과 4는 뒤로 밀리게 됨
# print('c[1:2] = ', c[1:2])
# print(c)

# c[1] = ['a', 'b', 'c'] # c[1]자리에 새로운 리스트를 집어 넣는 코드. 
# print(c)

# # 리스트 삭제
# del (c[1])
# print(c)
# # del 함수는 인덱스에 있는 값을 지워줌

# # 숫자 4만 지우기
# del (c[-1])
# print(c)


# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
# append 함수는 리스트 맨 마지막에 값을 더하는 함수

print(y)
y.sort()
# sort 함수는 리스트를 순차적으로 정렬하는 함수, 왼쪽에서 오른쪽으로 오름차순 정렬

print(y)
y.reverse()
# reverse 함수는 리스트를 역순으로 정렬하는 함수. 왼쪽에서 오른쪽으로 내림차순 정렬

print(y)
y.insert(2,7)
# insert 함수는 리스트 중간에 값을 집어 넣는 함수. ex ) y.insert(2,7) =  y[2]번 리스트에 7을 넣는다
# insert와 append의 차이점을 알고 있어야 함.
print(y)

y.remove(2)
# remove 함수는 리스트 내에서 입력한 값을 찾아 삭제하는 함수
# del의 경우 해당 자리를 찾아서 지우지만, remove는 리스트 내의 값을 찾아 삭제함

print(y)



y.remove(7)
print(y)

y.pop()
#pop 함수는 리스트 맨 마지막에 있는 데이터를 뽑고 삭제하는 함수
# pop과 push는 자료구조 같은 것을 공부하다 보면 스택이라고 부른다.
print(y) #LIFO 마지막에 들어간게 먼저 먼저 나온다.

ex = [88,77]
y.extend(ex)
# 현재 리스트에서 값을 연장할 때. ex라는 리스트 안에 있는 원소를 가져와서 추가하는 함수
# 끝 부분에 88,77을 넣음. 
# append로 넣어도 됨. 

y.append(ex)
# ex에 들어있는 리스트 자체를 y의 원소로 가져옴. extend와 차이점은 extend는 리스트 자체가 아닌 원소를 가져와서 추가함
print(y)

# 삭제: del, remove, pop
# pop을 계속 쓰다보면 언젠가 에러가 발생함. 

# 튜플 (순서 O, 중복 O, 수정x, 삭제x) 외울 것. 
# 삭제 메소드가 없음
# 수정이 안되기 때문이 인서트, 익스텐드 다 안됨.
# 어디에 쓰냐? 프로그램에 영향을 끼치는 중요한 키값. 계좌번호 같은 것. 한 번 데이터가 들어가면 변경이 되면 안되니까. 삭제하고 통장을 새로 만드는 규칙이 있다면 중요한 값이 변경되면 실행이 오작동 되거나, 프로그램 흐름에 크리티컬한 영향을 미치는 것을 방지하기 위해서. 중요 데이터는 튜플에 저장을 하고 사용하면 방지가 가능하다.

# 리스트는 대괄호를 넣었지만, 튜플은 소괄호가 끝임
a = ()
# 값을 넣을 때 콤마를 마지막에 넣어서  튜플을 끝내면 된다.
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# 튜플도 리스트와 인덱싱 방법은 동일함. 
print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
# 튜플도 리스트와 동일하게 앞에 있는 것을 첫 번째로 두고 두번쨰를 확장해서 하나의 튜플을 반환한다.

print(c*3)
# 확장이 됨

# 튜플 함수
# 튜플 함수는 몇 개 없음. 

z = (5,2,1,3,1)
print(z)
print(3 in z)
print(z.index(3))
# 3이 있는 곳의 인덱스를 반환함. 3이 나옴

print(z.index(5 ))
# 내가 찾고자 하는 값의 인덱스를 반환함
# 5는 0번째 인덱스이기 때문에 0이 나옴. 


print(z.count(1))
# 이 튜플 안에 "1"의 값을 가진 원소가 얼마나 들어 있는지 세는 함. 그래서 2가 반환이 됨. 
# 이런 자료 구조는 많이 할 수록 여러 언어의 적응력이 강해진다.
# 감을 통해서 다른 언어도 여기서는 배열을 이렇게 사용한다. 하고 알 수 있음. 
# 파일 다운로드 받아서 코딩을 해볼 것. 눈으로라도 확인 해볼 것.
# 인덱싱과 슬라이싱은 계속 따라다닐 것임. 셋과 딕셔너리에도 계쏙 따라옴.