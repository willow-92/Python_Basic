class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title
        
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

# 피보나치를 출력해주는 함수와 값을 반환하는 함수가 피보나치 클래스 안에 들어있다. 
# 패키지 형태가 피보나치 파이썬 파일 안에, 대문자 피보나치 클래스 안에 함수들이 있는 것. 
# 구조대로 나열할 수 있다는 것이고. 이 pkg 안에 수학 공식을 계산해주는 파일을 추가해주면 pkg 패키지는 수열을 처리하는 패키지구나 하고 알 수가 있다. 

        