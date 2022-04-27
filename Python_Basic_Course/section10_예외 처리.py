# section 10
# 파잌썬 예외 처리의 이해
# 예외는 에러를 뜻함. 아무리 수십명 수백명이 같이 협업을 했던라도, 아무리 실력 있는 프로그래머가 개발을 했다고 하더라도,
# 완벽한 프로그래밍은 있을 수가 없다. 항상 예상치 못한 에러가 발생할 수 있고.
# 잘못 된 코딩, 잘못 된 형 변환, 이런 미세한 실수 때문에 프로그램이 잘 운영이 되다가 에러가 발생되어서 긴급상황이 발생하기도 한다.
# 주로 결제 등.
# 수십명 수만명이 결제하는 이벤트를 하는데, 그 순간 에러가 난다면 회사가 입는 피해는 막심하다.
# 그래서 항상 예외, 에러 발생 가능성을 염두해서 코딩하는게 좋다.
# 파이썬에서도 예외처리를 위한 문법이 존재한다.
# 아무리 코드가 에러가 없더라도, 하드웨어에서 나타나는 오류를 완벽하게 잡을 수는 없다.
# 처리를 할 수가 없다.
# 그래서 예외처리를 통해 에러가 발생하는 순간 의도한 대로 코드를 실행하게 해 놓고, 그 부분을 바로 수정 해야 한다.
# 이런 과정을 통해 프로그램이 개선되는 과정이 있다.

# 파이썬의 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요.
# 문법적으로 에러가 나면 vscode나 파이참, 이런 IDE 개발 환경 도구에서 린터라는게 있다. 
# 이 린터가 하는 역활이 문법, 어떤 코드 스타일을 알려주고. 문법을 체크하는 것도 한다. 
# 만약 메모장에서 개발을 하는 것이라면 문법적인 부분도 생각을 해야 겠지만, 요즘은 이제 이런 통합 개발 환경에서 개발하기 때문에 그런 일은 거의 없다.
# 하지만 런타임 실행시 발생될 가능성이 있는 중요한 부분에서는 예외처리가 중요하다.

# SyntaxError : 잘못된 문법
# print('Test)

# if True
# pass

# x => Y

# NameError: 참조 변수 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0으로 나누기 에러
# print(10/0)

# # IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[3])

#keyError
# 없는 키를 조회 했을 때 딕셔너리 에러가 발생
dic = {'name' : 'kim', 'Age' : 33, 'City': 'Seoul'}
# print(dic['hobby'])

# 이런 것들을 피하기 위해서 get 메소드를 사용해 준다. 
# get 메소드의 경우 키 값이 없으면 None을 반환한다. 

# Attribute Error (속성 에러) : 모듈, 클래스에 있는 잘못된 속성 사용시에 발생하는 예외
import time
# print(time.time())
# print(time.month())  
# 처리가 쉬움. 직접 찾아가보고 확인

# ValueError: 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)
# 리스트에는 10이 포함되어 있지 않다. 

# FileNotFound Error
# f = open('test.txt', 'r')
# 외부 파일을 처리할 때 발생하는 에러

# TypeError
x = [1,2]
y = (1,2)
z = 'test'

# print(x + y)
# print(x + z)
# print(x + list(y))

 # 예외 종류가 많은데,
 # 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
 # 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)
 
 
 # 예외 처리 기본
 # try : 에러가 발생할 가능성이 있는 코드 실행
 # except : 에러명1
 # except : 에러명2
 # else : 에러가 발생하지 않았을 경우 실행
 # finally : 항상 실행

# # 예제 1
# name = ['kim', 'Lee', 'Park']
# try: 
#     z = 'kim' #cho 예외 발생
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except ValueError:
#     print('Not found it! - Occured ValueError!')
# else:
#     print('OK! else!')

# else 구분은 에러가 발생하지 않았을 경우에만 실행됨
# 즉 try문이 정상적으로 실행 되었을 때만 실행 됨.

# 예제 2
# name = ['kim', 'Lee', 'Park']
# try: 
#     z = 'kim'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except: #어떤 에러일지 모를 때는 그냥 둔다. 모든 에러의 종류를 캐치함. 
#     print('Not found it! - Occured Error!')
# else:
#     print('OK! else!')


# 예제 3
name = ['kim', 'Lee', 'Park']
try: 
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
else:
    print('OK! else!')
finally:
    print('finally ok!') #finally는 예외가 발생하든, 그렇지 않든 무조건 실행됨

# 만약, 예를 들어서 데이터 베이스를 연결하는 리소스를, 코드 외부에 있는 프로그램을 연결하는 스트림 작업을 했다면, 에러가 발생하든, 발생하지 않든, 그 연결을 끊어주는 작업을 처리 해야 한다. 
# 즉 내가 사용했던 것을 에러가 발생해도 처리 해줘야 하고, 발생하지 않고 잘 사용했어도 처리해주는. 이런 무조건적인 수행을 할 때는 Finally를 쓴다. 
# else 같은 경우에는 발생하지 않았을 경우. 즉 정상 실행 되었을 경우만 실행되는 것이고. Finally는 전부 다 실행을 할 수 있다는 것.

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('ok Finally!!!')
 # 자주 보이는 코딩 패턴

 

# 예제 5
name = ['kim', 'Lee', 'Park']
try: 
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l: #순서가 중요함. exception이 먼저 올라와 있으면 Exception에서 다 잡아버리기 때문에, 예측 가능한 에러를 순서대로 먼저 쓰고 최종적으로 exception이 잡는게 좋음
    print(l) # 프린트 구문으로 직접 쓰지 않아도, Value Error라는 것을 출력할 수 있음. 자주 사용되지는 않음
except IndexError:
    print('Not found it! - Occured ValueError!')
except Exception:
    print('Not found it! - Occured ValueError!')
else:
    print('OK! else!')
finally:
    print('finally ok!') #finally는 예외가 발생하든, 그렇지 않든 무조건 실행됨


# 예제 6
# 예외 발생: raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print('ok. 허가')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok!')

# 직접 예외 클래스를 규정해서 발생 시키는게 레이스. 고급 프로그래밍. 
# 파이썬 예외 종류를 발생시킴.

