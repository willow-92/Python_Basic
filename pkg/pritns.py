def prt1():
    print("I'm Niceboy!")

def part2():
    print("I'm Goodboy!")

# 모듈 파일을 테스트 하고 싶을 때.
# control shift b를 해봤자 함수를 실행해봐야 아는데,
# 단위 테스트를 할 수 있는 부분이 있는데,

# 단위 실행 (독립적으로 파일 실행)
# 파이썬 2점대 버전
if __name__ == "__main__" :
    print(prt1())
    print(part2())

# section 08에서 실행할 때는 이 파일에서 실행하는게 아니라 section8에서 실행하는 것이라 main이 아니기 때문에 실행되지 않음. 
# 위와 같은 것들을 만들어 놓고. 직접 파일로 와서 실행하면 잘 되지만, section 8에서 실행하면 if 문이라 실행되지 않으므
# 단위 테스트를 할 때 해당 모듈 맨 아래 부분에 if __name__ == "__main__" : 이런 테스트 코드를 생성해 놓는 것도 좋다. 