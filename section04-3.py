# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 코드의 변경, 수정을 수월하게 하기 위해 자료구조를 사용해야 한다.

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언
a = []
b = list()  # 명시적 선언
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']  # 데이터 타입이 다르더라도 list에 넣을 수 있다.
e = [10, 100, ['Pen', 'Banana', 'Orange']]  # 이중 리스트가 가능하다.

# 인덱싱
print(d[3])  # Banana
print(d[-2])  # Banana
print(d[0] + d[1])  # 110
print(e[2][1])  # Banana
print(e[-1][-2])  # Banana

# 슬라이싱
print(d[0:3])  # [10, 100, 'Pen']
print(e[2][1:3])  # ['Banana', 'Orange']


# 연산
print(c + d)
# [1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']
print(c * 3)
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(str(c[0]) + 'hi')  # 1hi

print(c + ['hi'])


# 리스트 수정, 삭제
print(c)  # [1, 2, 3, 4]
c[0] = 77
print(c)  # [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000]
print(c)
# [77, 100, 1000, 10000, 3, 4]

c[1] = ['a', 'b', 'c']
print(c)
# [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]


del c[1]
print(c)
# [77, 1000, 10000, 3, 4]

del c[-1]
print(c)
# [77, 1000, 10000, 3]

print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)  # [5, 2, 3, 1, 4]
y.append(6)
print(y)  # [5, 2, 3, 1, 4, 6]
y.sort()
print(y)  # [1, 2, 3, 4, 5, 6]
y.reverse()
print(y)  # [6, 5, 4, 3, 2, 1]
y.insert(2, 7)
print(y)  # [6, 5, 7, 4, 3, 2, 1]
y.remove(2)
y.remove(7)
print(y)  # [6, 5, 4, 3, 1]
y.pop()  # LIFO
print(y)  # [6, 5, 4, 3]
ex = [88, 77]
y.append(ex)
print(y)  # [6, 5, 4, 3, [88, 77]]
y.pop()
y.extend(ex)
print(y)  # [6, 5, 4, 3, 88, 77]
y.extend(10)
print(y)  # [6, 5, 4, 3, 88, 77]
# 삭제: del, remove, pop


# 튜플 (순서o, 중복o, 수정X, 삭제X)
# 프로그램에 중요한 영항을 주는 중요한 key값(변경되면 안되는)에 주로 사용됨

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])  # 3
print(c[3])  # 4
print(d[2][1])  # b

print(d[2:])  # (('a', 'b', 'c'),)
print(d[2][0:2])  # ('a', 'b')

print(c + d)
# (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))

print(c * 3)
# (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

print()

# 튜플 함수
z = (5, 2, 1, 3, 4, 1)
print(z)  # (5, 2, 1, 3, 4, 1)
print(3 in z)  # True
print(z.index(5))  # 0
print(z.count(1))  # 2
