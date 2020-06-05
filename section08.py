# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233

print("ex1 :", Fibonacci.fib2(400))
# ex1 : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

print("ex1 :", Fibonacci().title)
# ex1 : fibonacci


# 사용2(클래스) : 메모리를 많이 차지하기 때문에 권장하지 않음
from pkg.fibonacci import * # 여러 개의 클래스를 한 번에 다 가져오겠다

Fibonacci.fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233

print("ex2 :", Fibonacci.fib2(500))
# ex2 : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

print("ex2 :", Fibonacci().title)
# ex2 : fibonacci


# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

print("ex3 :", fb.fib2(1600))
# ex3 : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
print("ex3 :", fb().title)
# ex3 : fibonacci


# 사용4(함수)
import pkg.calculations as c

print("ex4 :", c.add(10, 100))
# ex4 : 110
print("ex4 :", c.mul(10, 100))
# ex4 : 1000

# 사용5(함수): 필요한것만 가져와서 사용하는 것이 좋다 -> 리소스 낭비 방지
from pkg.calculations import div as d

print("ex5 :", int(d(100, 10)))
# ex5 : 10

# 사용6
import pkg.prints as p
import builtins
# 파이썬에서 기본적으로 제공하는 모듈들: 기본으로 import되기 때문에 이렇게 명시적으로 import하지 않아도 된다.
p.prt1()  # I'm Nicebody!
p.prt2()  # I'm Goodboy!
print(dir(builtins))
