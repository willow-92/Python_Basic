# section 09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드 : w(기존 파일 삭제), 추가 모드(파일 생성 또는 추가) : a 
# .. : 상대경로, . : 절대 경로
# 기타 : https://docs.pytohn.org/3.7/library/functions.html#open

# 파일 읽기
# 예제 1

f = open('./Python_Basic/resource/review.txt', 'r')
content = f.read()
print(content)
f.close

# 열었으면 close를 해서 리소스를 반환해 주여야 함. 
# 자바나, 데이터베스연결을 하든, 외부 작업을 할 때는 커넥션 작업이 이루어 지는데,
# 리소스를 사용한 이후에 닫지 않으면, 언젠가는 그것에 대한 예외가 발생한다.
# 그래서 한 번 사용한 리소스는 클로스로 닫아 주어야 한다. 


print(dir(f))
# 프린트 문에서 f가 무엇을 하는지 찍어 볼 때는 dir이라는 것으로 출력. 
# 이 f안에 있는 모든 속성값들을 볼 수 있음. 
# 메소드 부터. 이 안에 read 메소드도 있고. read lines, seek 탐색하는 등 여러 메소드가 f라는 변수의 인스턴스로서 할당이 되었음. 
# 사용법도 잘 나와 있음. 

# 예제 2
# 항상 사용하면 클로스로 닫아야 한다. 
# 그래서 파이썬에는 with 문이라는게 있다. 
# r로 일고 엘리아스를 f로 주겠다고 하면 f를 가지고 바로 사용한 것. 이게 위의 f = open('./Python_Basic/resource/review.txt', 'r')와 똑같은 의미.
# 다만 with 문은 편한게, 클로즈를 하지 않아도 with 문이 끝나면 자동으로 리소스를 반환한다. 
# 그래서 close를 생략해도 된다는 것.

print("----------------------------------")

with open('./Python_Basic/resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
# 여기서 가져온 내용들은 참고로 리스트 형태로도 형 변환을 할 수 있음. 
# 한 글자 단위로 알아서 들어간다. 캐릭터 단위이기 때문에. 
    print(iter(c))
# iter 함수를 사용하면 이터레이터를 반환하기 때문에 for문에서 사용할 수 있음.
# 1번과 2번에서 다른 점은 with 문을 사용했다는 것. 그래서 close를 해주지 않아도 파이썬에서 한다는 것. 
# 다만 with문 아래 하위에 인덴트가 들어가 줘야 함. 

print("----------------------------------")
print("----------------------------------")

# 예제3
# f자체가 iterable하기 때문에 바로 for문에 가져다가 붙여서 쓸 수 있다. 
with open('./Python_Basic/resource/review.txt', 'r') as f:
    for c in f:
#        print(c)
        print(c.strip())
# 이렇게 출력하면 한 라인씩 출력해줌. 라인 단위로 가져온다. 
# 띄어쓰기가 들어가 있는데, 끝에 \n이 들어가 있어서 그렇다. 
# 이걸 파이썬 문자열 함수인 strip을 사용하면 양쪽 공백을 제거해줌.

print("----------------------------------")
print("----------------------------------")

# 예제 4
# 한 줄 한 줄씩 읽어와서 어떻게 내부적으로 증명이 되는지? 
with open('./Python_Basic/resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)

# 위와 같이 출력하면 한 번에 read를 다 가져왔다. 
# 그 다음에 또 read를 하게 되면 어떻게 될까? 
    content = f.read() 
# 아무것도 나오지 않는다. 커서가 처음에서 끝으로 이동했기 때문. 
# 시작점에서 마지막 까지 읽었다 라고 하는 끝을 커서하는 커서가 units. 뒤에 있기 때문
# 그 하위에는 다른 내용이 없다. 
# 그렇기 때문에 빈 내용이 표시된다. 
# 여기서 부터는 내용 없음.

# 그래서 한 번에 읽어오는게 아니라, 한 줄씩 읽어오는 메소드가 존재한다. 
print("----------------------------------")
print("----------------------------------")

# 예제 5
with open('./Python_Basic/resource/review.txt', 'r') as f:
    line =f.readline()
    # print(line)
    # 현재 첫 번째 줄 까지 읽어왔고. 첫 번째 줄을 읽은 커서가 다음줄 시작점에 위치해서 읽어올 준비를 하고 있음
    # 이걸 반복문을 통해서 호출할 수 있음. 

    while line:
        print(line, end='## ')
        line = f.readline()

# 한 문장 단위로 읽어와서 전처리를 할 때는 read line을 사용하는게 좋다. 