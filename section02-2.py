# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)  # 출력> utf-8
print(sys.stdout.encoding)  # 출력> utf-8

# 출력문
print('My name is rami!')

# 변수 선언
myName = 'rami'
print('myName:', myName)

# 조건문
if myName == 'rami':
    print('Ok', myName)

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d + %d = ' % (i, j), i*j)
# 들여쓰기가 하나의 문법이기 때문에 들여쓰기가 중요함!

# 변수 선언(한글)
이름 = '좋은사람'

# 출력
print(이름)

# 함수 선언


def greeting():
    print('Hello!')


greeting()

# 클래스


class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
