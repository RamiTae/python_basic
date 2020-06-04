# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# *코드 재사용, 중복 코드 최소화 => 가독성, 유지보수

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car class "Show Method!"'


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

    def show(self):
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('M5', 'sedan', 'red')

print(model1.color)  # Super
# red

print(model1.type)  # Super
# sedan

print(model1.car_name)  # Sub
# M5

print(model1.show())  # Super
# Car class "Show Method!"

print(model1.show_model())  # Sub
# Your Car Name : M5

print(model1.__dict__)
# {'type': 'sedan', 'color': 'red', 'car_name': 'M5'}


# Method Overriding(오버라이딩)
model2 = BenzCar('400d', 'suv', 'black')

print(model2.show())
# Car Info : 400d suv black


# Parent Method Call
class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


model3 = BenzCar('63AMG', 'sedan', 'silver')
print(model3.show())
# Car class "Show Method!"
# Car Info : 63AMG sedan silver


# Inheritance Info(상속 정보) : 상속 정보를 list 형태로 보여줌
print(BmwCar.mro())  # 상속관계 보여줌
# [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]

print(BenzCar.mro())
# [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
# *너무 깊은 다중상속은 코드의 복잡도가 커지기 때문에 지양해야한다.

print(A.mro())
# [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
