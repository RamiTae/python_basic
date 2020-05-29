# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am persion."
str2 = "Rami"
str3 = ''
str4 = str('')  # 잘 쓰이지 않는 형식이다.

print(len(str1), len(str2), len(str3), len(str4))
# 13 4 0 0

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
# Do you have a "big collection"

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)
# Tab     Tab     Tab

# Raw String : 경로표시(escape문자가 적용되지 않음)
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
# C:\Programs\Test\Bin

raw_s2 = r'\\a\\a'
print(raw_s2)
# \\a\\a

# 멀티라인(한 쌍 짜리는 멀티라인이 안 됨)
multi = \
    """
문자열

멀티라인

테스트
"""
print(multi)
#
# 문자열
#
# 멀티라인
#
# 테스트


# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'Rami'

print(str_o1 * 100)
# ****************************************************************************************************

print(str_o2 + str_o3)
# abcdef

# print(str_o1 + 3) : 에러

print('a' in str_o4)  # 'a'가 str_o4에 포함되어있는가?
# True
print('f' in str_o4)
# False

print('z' not in str_o4)  # 'a'가 str_o4에 포함되어있지 않은(not)가?
# True

# 문자열 형 변환
print(str(77) + 'a')
# 77a
print(str(10.4), type(str(10.4)))
# 10.4 <class 'str'>

print()

# 문자열 함수
a = 'niceman'
b = 'orange'

print(a.islower())  # 전부 소문자인가
# True

print(b.endswith('e'))  # 마지막 글자 확인
# True

print(a.capitalize())  # 첫 글자 대문자로
# Niceman

print(a.replace('nice', 'good'))  # 변경
# goodman

print(list(reversed(b)))  # 순서를 변경 후 list화
# ['e', 'g', 'n', 'a', 'r', 'o']

print()

# 문자열은 재선언 불가능 -> 인덱싱때문 ...? 왜?
# 뭔... 정방향 역방향 인덱싱에 대한 설명이랑 재선언 불가능이랑 무슨 상관관계가 있는거임???
a = 'goodman'
b = 'orange'

# 데이터분석, 웹 등에서 많이 쓰임
print(a[0:3])  # 문자열 중 0부터 3미만 인덱스까지
# goo

print(a[0:4])  # 문자열 중 0부터 4미만 인덱스까지
# good

print(a[0:len(a)])
# goodman

print(a[:4])  # 처음부터 4미만까지
# good

print(a[:])  # 처음부터 끝까지
# goodman

print(b[0:4:2])  # 0부터 4미만까지 스킵단위 2
# oa

print(b[1:-2])  # 뒤에서부터 세기.
# ran

print(b[::-1])  # 처음부터 끝까지 스킵단위 -1
# egnaro
