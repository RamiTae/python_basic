# # Section06
# # 파이썬 함수식 및 람다(lambda)

# # 함수 정의 방법
# # def 함수명(parameter):
# #     code

# # 함수 호출
# # 함수명(parameter)

# # 함수 선언 위치 중요

# # hello('world')
# # NameError: name 'hello' is not defined

# # 예제1
# def hello(world):
#     print('Hello', world)


# hello('Python!')  # Hello Python!
# hello(1234)  # Hello 1234


# # 예제2
# def hello_return(world):
#     val = 'Hello ' + str(world)
#     return val


# string = hello_return('Python!!!!!!')
# print(string)  # Hello Python!!!!!!


# # 예제3(다중리턴)
# def func_mul(x):
#     y1 = x * 100
#     y2 = x * 200
#     y3 = x * 300
#     return y1, y2, y3


# val1, val2, val3 = func_mul(100)
# print(val1, val2, val3, type(val1))
# # 10000 20000 30000 <class 'int'>


# # (데이터 타입 반환)
# def func_mul2(x):
#     y1 = x * 100
#     y2 = x * 200
#     y3 = x * 300
#     return (y1, y2, y3)


# lt = func_mul2(100)
# print(lt, type(lt))
# # (10000, 20000, 30000) <class 'tuple'>


# 예제4(가변 인자)
# *args, **kwargs
# args
def args_func(*args):
    print(args)
    for t in args:
        print(t, end=' ')
    print()
    for i, v in enumerate(args):
        print(i, v, end=' ')
    print()


args_func('kim')
# ('kim',)
# kim
# 0 kim
args_func('kim', 'Park')
# ('kim', 'Park')
# kim Park
# 0 kim 1 Park
args_func('kim', 'Park', 'Tae')
# ('kim', 'Park', 'Tae')
# kim Park Tae
# 0 kim 1 Park 2 Tae


# kwargs 키워드
def kwargs_func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v, end=' ')
    print()


kwargs_func(name1='Kim')
# {'name1': 'Kim'}
# name1 Kim
kwargs_func(name1='Kim', name2='Park', name3='Lee')
# {'name1': 'Kim', 'name2': 'Park', 'name3': 'Lee'}
# name1 Kim name2 Park name3 Lee


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
# 10 20 () {}
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)
# 10 20 ('park', 'kim') {'age1': 24, 'age2': 35}
example_mul(10, 20, age1=24, age2=35)
# 10 20 () {'age1': 24, 'age2': 35}


# 예제5
# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func')
    func_in_func(num + 1000)


nested_func(1000)
# in func
# 2000
# 파이썬 데코레이터 클로저


# 예제6(hint)
def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(5))
# [500, 1000, 1500]


# 람다식 예제
# 람다식: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화


# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)
# <function mul_10 at 0x7f66b2237700>
print(type(var_func))
# <class 'function'>


print(var_func(10))  # 100


# lambda_mul_10 = lambda x: x * 10
def lambda_mul_10(x): return x * 10


print('>>>', lambda_mul_10(10))  # >>> 100


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10)  # 10000

func_final(10, 10, lambda x: x * 1000)  # 1000000
