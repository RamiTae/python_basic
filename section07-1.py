# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print('Name:', self.name)


user1 = UserInfo('Tae')
print(user1.name)  # Tae
user1.user_info_p()  # Name: Tae

user2 = UserInfo('Park')
print(user2.name)  # Park
user2.user_info_p()  # Name: Park

# id(): 주소값 확인
print(id(user1))  # 140350650158624
print(id(user2))  # 140350650343328

# 네임스페이스 확인
print(user1.__dict__)  # {'name': 'Tae'}
print(user2.__dict__)  # {'name': 'Park'}


# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')

    def function2(self):
        print('function2 called!')
        print(id(self))


self_test = SelfTest()
# self_test.function1()
# => 에러 TypeError: function1() takes 0 positional arguments but 1 was given
SelfTest.function1()  # function1 called!
self_test.function2()
# function2 called!
# 140556938638240

print(id(self_test))  # 140556938638240
SelfTest.function2(self_test)
# function2 called!
# 140556938638240


# 예제3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수: 하나의 변수를 모든 인스턴스가 공유가능
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('Tae')
user2 = WareHouse('Kim')
user3 = WareHouse('Lee')

print(user1.__dict__)  # {'name': 'Tae'}
print(user2.__dict__)  # {'name': 'Kim'}
print(user3.__dict__)  # {'name': 'Lee'}
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수(공유)
# {'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x7fd157b5b700>, '__del__': <function WareHouse.__del__ at 0x7fd157b5b790>, '__dict__': <attribute '__dict__' of 'WareHouse' objects>, '__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, '__doc__': None}

print(user1.name)  # Tae
print(user2.name)  # Kim
print(user3.name)  # Lee

# 자기 네임스페이스에 없으면 클래스 네임스페이스에서 찾음
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)
# 3

del user1

print(user2.stock_num)
print(user3.stock_num)
# 2
