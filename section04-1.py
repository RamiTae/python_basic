# 데이터 타입
import math
v_str1 = "NiceRami"
print("v_str1:", type(v_str1))
# 출력> v_str1: <class 'str'>

v_bool = True
print("v_bool:", type(v_bool))
# 출력> v_bool: <class 'bool'>

v_str2 = "GoodRami"
print("v_str2:", type(v_str2))
# 출력> v_str2: <class 'str'>

v_float = 10.3
print("v_float:", type(v_float))
# 출력> v_float: < class 'float' >

v_int = 7
print("v_int:", type(v_int))
# 출력> v_int: < class 'int' >

v_dic = {
    "name": "Tae",
    "age": 25
}
print("v_dic:", type(v_dic))
# 출력> v_dic: < class 'dict' >

v_list = [3, 5, 7]
print("v_list:", type(v_list))
# 출력> v_list: < class 'list' >

v_tuple = 3, 5, 7
print("v_tuple:", type(v_tuple))
# 출력> v_tuple: < class 'tuple' >

v_set = {7, 8, 9}
print("v_set:", type(v_set))
# 출력> v_set: < class 'set' >

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)  # 출력> 36621
# 출력> 77777777777777777777777777777777777777777777777777762222222222222222222222222222222222222222222222222223
print(big_int1 * big_int2)
print(f1 ** f2)  # 출력> 2.2158306445574567

result = f3 + i2
print(result, type(result))  # 출력> 939.5 <class 'float'>
# print(type(complex(1)))


# 형변환
a = 5.
b = 4
c = 10

print('a:', type(a), 'b:', type(b))
# 출력> a: <class 'float'> b: <class 'int'>

result2 = a + b
print('a+b:', result2, type(result2))
# 출력> a+b: 9.0 <class 'float'>

# 형변환
# int, float, complex(복소수)

print('int(result2):', int(result2), type(int(result2)), sep='\t')
# 출력> int(result2):   9       <class 'int'>

print('float(c):', float(c), type(float(c)), sep='\t')
# 출력> float(c):       10.0    <class 'float'>

print('complex(3):', complex(3), type(complex(3)), sep='\t')
# 출력> complex(3):     (3+0j)  <class 'complex'>

print('int(True):', int(True), type(int(True)), sep='\t')
# 출력> int(True):      1       <class 'int'>

print('int(False):', int(False), type(int(False)), sep='\t')
# 출력> int(False):     0       <class 'int'>

print("int('3'):", int('3'), type(int('3')), sep='\t')
# 출력> int('3'):       3       <class 'int'>

print("complex(True):", complex(True), type(complex(True)), sep='\t')
# 출력> complex(True):  (1+0j)  <class 'complex'>

print("complex(False):", complex(False), type(complex(False)), sep='\t')
# 출력> complex(False): 0j      <class 'complex'>

# 단항연산자
y = 100
y *= 100
print(y)


# 수치 연산 함수
print(abs(-7))  # 절대값을 반환한다.
# 출력> 7

n, m = divmod(100, 8)  # 앞의 변수에 몫을, 뒤의 변수에 나머지를 저장한다
print(n, m)
# 출력> 12 4

# math 함수

print(math.ceil(5.1))  # 올림
# 출력> 6

print(math.floor(3.874))  # 버림
# 출력> 3
