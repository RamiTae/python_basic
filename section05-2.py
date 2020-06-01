# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문: for, while

v1 = 1
while v1 < 11:
    print("v1 is:", v1)
    v1 += 1
# v1 is: 1
# v1 is: 2
# v1 is: 3
# v1 is: 4
# v1 is: 5
# v1 is: 6
# v1 is: 7
# v1 is: 8
# v1 is: 9
# v1 is: 10

for v2 in range(10):
    print("v2 is:", v2)
# v2 is: 0
# v2 is: 1
# v2 is: 2
# v2 is: 3
# v2 is: 4
# v2 is: 5
# v2 is: 6
# v2 is: 7
# v2 is: 8
# v2 is: 9

for v3 in range(1, 11):
    print("v3 is:", v3)
# v3 is: 1
# v3 is: 2
# v3 is: 3
# v3 is: 4
# v3 is: 5
# v3 is: 6
# v3 is: 7
# v3 is: 8
# v3 is: 9
# v3 is: 10

print()

# 1 ~ 100 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print("1 ~ 100:", sum1)  # 1 ~ 100: 5050
print("1 ~ 100:", sum(range(1, 101)))  # 1 ~ 100: 5050
print("1 ~ 100:", sum(range(1, 101, 2)))  # 1~100까지 중 하나씩 건너뛰며 더하기
# 1 ~ 100: 2500

# range() 연속적인 숫자를 가지는 시퀀스 타입
print(type(range(10)), range(10))
# <class 'range'> range(0, 10)

print()

# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전 등 반복할 수 있음
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Tae", "Yoo"]

for v in names:
    print("You are:", v)
# You are: Kim
# You are: Park
# You are: Cho
# You are: Tae
# You are: Yoo

word = "dreams"
for s in word:
    print("Word:", s)
# Word: d
# Word: r
# Word: e
# Word: a
# Word: m
# Word: s

my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

# 기본 값은 키
for key in my_info:
    print("my_info", key)
# my_info name
# my_info age
# my_info city

# 값
for key in my_info.values():
    print("my_info value", key)
# my_info value Kim
# my_info value 33
# my_info value Seoul

# 키
for key in my_info.keys():
    print("my_info key", key)
# my_info key name
# my_info key age
# my_info key city

# 키 and 값
for k, v in my_info.items():
    print("my_info item", k, v)
# my_info item name Kim
# my_info item age 33
# my_info item city Seoul

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower(), end="")
    else:
        print(n.upper(), end="")
# kENNry

print()

# break: 하고자 하는 작업의 조건에 맞으면 작업을 바로 중지하고 나갈 수 있게 함
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found: 33!")
        break
    else:
        print("not found: 33!")
# not found: 33!
# not found: 33!
# not found: 33!
# not found: 33!
# not found: 33!
# not found: 33!
# not found: 33!
# not found: 33!
# found: 33!

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]
# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
    if num == 33:
        print("found: 33!")
        break
    else:
        print("not found: 33!")
else:
    print("Not found 33........")
# not found: 33!
# ...
# not found: 33!
# Not found 33........

# continue: 스킵
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입:", type(v))
# 타입: <class 'str'>
# 타입: <class 'int'>
# 타입: <class 'int'>
# 타입: <class 'bool'>
# 타입: <class 'complex'>

print()

name = "Niceman"
print(reversed(name))  # <reversed object at 0x7f61570f5e20>
print(list(reversed(name)))  # ['n', 'a', 'm', 'e', 'c', 'i', 'N']
print(tuple(reversed(name)))  # ('n', 'a', 'm', 'e', 'c', 'i', 'N')
