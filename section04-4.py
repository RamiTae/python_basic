# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x(키는 중복x, 값은 중복o), 수정o, 삭제o

# Key, Value (Json과 형식이 비슷함) -> MongoDB
# 선언
a = {'name': 'Tae', 'Phone': '010-7777-7777', 'birth': 920422}
b = {0: 'Hello Python', 1: 'Hello Coding'}  # Key를 숫자로 하는 경우는 잘 쓰이지 않음
c = {'arr': [0, 1, 2, 3, 4, 5]}  # Value는 모든 형식이 들어갈 수 있음

print(type(a))  # <class 'dict'>

# 출력
# print(a.name)
print(a['name'])  # Tae
# print(a['address'])  # KeyError: 'address'

print(a.get('name'))  # Tae
print(a.get('address'))  # None
print(c['arr'][1:3])  # None

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
# {'name': 'Tae', 'Phone': '010-7777-7777', 'birth': 920422, 'address': 'Seoul'}

a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)
# {'name': 'Tae', 'Phone': '010-7777-7777', 'birth': 920422, 'address': 'Seoul', 'rank': [1, 3, 4], 'rank2': (1, 2, 3)}


# keys, values, items item(key, value 쌍)
print(a.keys())
# dict_keys(['name', 'Phone', 'birth', 'address', 'rank', 'rank2'])
# print(a.keys().[0]) # SyntaxError: invalid syntax

temp = list(a.keys())
print(temp[1:3])  # ['Phone', 'birth']

print(a.values())
# dict_values(['Tae', '010-7777-7777', 920422, 'Seoul', [1, 3, 4], (1, 2, 3)])

print(list(a.values()))
# ['Tae', '010-7777-7777', 920422, 'Seoul', [1, 3, 4], (1, 2, 3)]

print(a.items())
# dict_items([('name', 'Tae'), ('Phone', '010-7777-7777'), ('birth', 920422), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))])

print(list(a.items()))  # list 안에 tuple이 있는 형태
# [('name', 'Tae'), ('Phone', '010-7777-7777'), ('birth', 920422), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))]

print('rank' in a)  # True
print('Tae' in a)  # False

print()
print()


# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))  # <class 'set'>
print(c)  # {1, 4, 5, 6}

t = tuple(b)
print(t)  # (1, 2, 3, 4)
l = list(b)
print(l)  # [1, 2, 3, 4]

print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2)
# {4, 5, 6}

# 합집합
print(s1 | s2)
print(s1.union(s2))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
print(s1 - s2)
print(s1.difference(s2))
# {1, 2, 3}


# 추가 & 제거
s3 = set([7, 8, 9, 10, 15])

s3.add(18)
s3.add(7)

print(s3)  # {7, 8, 9, 10, 15, 18}

s3.remove(15)
print(s3)  # {7, 8, 9, 10, 18}

print(type(s3))  # <class 'set'>
