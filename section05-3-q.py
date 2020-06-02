# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print('Q1.', q1['가을'])

for k in q1.keys():
    if k == '가을':
        print(q1[k])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print('Q2.', ('사과' in q2.keys()) | ('사과' in q2.values()))

for k, v in q2.items():
    if v == '사과':
        print(k, v, sep=':')
        break
else:
    print('사과 없음')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 41
if score > 80:
    grade = 'A'
elif score > 60:
    grade = 'B'
elif score > 40:
    grade = 'C'
elif score > 20:
    grade = 'D'
else:
    grade = 'E'
print('Q3. 점수: {s}, 학점: {g}'.format(s=score, g=grade))


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
largest = 0
a = 12
b = 6
c = 18
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print('04. 가장 큰 수:', largest)

a, b, c = 12, 6, 18
best = a
if b > a:
    best = b
if c > b:
    best = c
print('best:', best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
idCode = '920422-2000000'
gender = ''

if int(idCode[7]) % 2 == 0:
    gender = '여자'
else:
    gender = '남자'
print('Q5. 당신은 {g} 입니다.'.format(g=gender))


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

print('Q6.', end=' ')
for char in q3:
    if char == '정':
        continue
    print(char, end=' ')

print()

q5 = [x for x in q3 if x != '정']
print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print('Q7.', end=' ')
for num in range(1, 101):
    if num % 2 == 1:
        print(num, end=' ')

print()

q6 = [x for x in range(1, 101) if x % 2 != 0]
print(q6)


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print('Q8.', end=' ')
for string in q4:
    if len(string) >= 5:
        print(string, end=' ')

print()


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print('Q9.', end=' ')
for char in q5:
    if char.islower():
        print(char, end=' ')

print()


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print('Q10.', end=' ')
for char in q6:
    if char.islower():
        print(char.upper(), end=' ')
    else:
        print(char.lower(), end=' ')

print()
print()

# 일반적인 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

# List Comprehension: 리스트를 쉽게 만드는 기법
numbers2 = [x for x in range(1, 101)]
print(numbers2)

# x = [x for x in range(1, 100) if 조건문]
