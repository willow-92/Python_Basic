# section07-2
# 파잌선 클래스 상세 이해
# 상속, 다중 상속

# 상속과 다중상속
# 지난시간에 어떤 클래스 변수는 공통으로 모두 접근이 가능해서 공유한다고 했고. 각각의 클래스를 바탕으로 생성된 인스턴스는
# 자기 자신의 네임 스페이스를 가지고 자기 자신의 속성, 메소드를 관리한다고 했습니다.
# 그래서 클래스도 네임 스페이스가 있따. dir이라는 함수로 출력을 해볼수가 있었다. 
# 클래스 상속과 파이썬의 특징인 다중상속
# 상속 부모에게 물려받는 것. 부모가 가지고 있는 모든 속성과 메소드를 자식에서 사용할 수가 있다. 
# 상속은 객체지향 프로그램에서 주는 이점이 너무 많기 떄문에 모든 언어에서 거의 다 제공하고 있따. 
# 물론 객체지향에서. 
# 그 중에서 파이썬은 다중상속을 허용하고 있다. 자바는 다중상속이 아닌 인터페이스를 지원한다. 
# 일단 만들면서 실습을 한다. 

# 상속 기본
# 부모 클래스 = 슈퍼 클래스
# 자식 = 서브 클래스
# 부모가 가지고 있는 재산을 물려 받았기 때문에 모든 속성 메소드를 사용 가능하다.

# 상속을 왜 사용할까? 
# 많은 이유들이 구글에서 상속의 필요성, 상속이 필요한 이유, 이런 것으로 검색해보면 많이 나옴
# 기초에서 알아둬야 할 것은, 상속을 통해서 코딩을 하면, 코드를 재사용 할 수 있고.
# 중복되는 코드를 최소화 할 수 있다는 것.
# 그래서 코드의 생산성과 유지보수, 가독성과 관련이 있다.
# 복잡한 코드를 단순화 하기 위한 객체지향 프로그래밍에서 상속, 클래스 이런게 나오기 시작했다.
# 라면이 있다고 했을 때, 이 라면은 속성이 뭐가 있을까? 
# 라면 종류가 여러가지인데, 종류가 될 수도 있을것이고. 제조사도 있을 수 있고. 맛, 면 종류, 라면 이름 이런 것들이 공통적인 속성으로 뽑을 수 있다.
# 이런 것들을 공통적으로 가지고 있는 것을 부모 클래스에서 생성하고
# 자식은 라면이라는 클래스를 상속을 받아서 공통으로 쓸 수 있는 것들은 물려받아서 속성과 메소드로 사용하고
# 나머지 것들은 각자 자식 클래스에서 구현해서 사용한다면 각각 하나하나에 라면 클래스를 생성하는 것 보다, (속성이 중복됨) 
# 하나의 클래스에서 공통 속성을 제거하고 상속받는 서브 클래스에서는 코드를 재사용하니까 코드 양이 줄어든다.
# 
# 예제 1
class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) #Sub
print(model1.show())

# 여러 클래스가 한 메소드를 공유한다면 코드의 중복을 피하고.
# car class를 상속받아서 사용할 수 있다.

print(model1.show_model()) #sub

# 부모의 있는 모든 속성과 메소드에 접근 가능하고. 자식도 자식만의 데이터를 네임스페이스에서 보관할 수 있따. 
print(model1.__dict__)
# 당연히 car name은 자식에서 생성할 때 초기화 한 것이고, 부모에서 초기화 한 것도 확인할 수가 있는 것. 