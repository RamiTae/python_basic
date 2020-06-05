# Section09
# 파일 읽기, 쓰기
# 읽기 모드: r(read), 쓰기 모드(기존 파일 삭제): w(write), 추가 모드(파일 생성 또는 추가): a(append)
# .. : 상대경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print('---------------------------------------')

# 예제2
# *with문을 사용하면 close를 사용하지 않더라도 자동으로 닫아줌
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('---------------------------------------')

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())  # *strip(): 양쪽 공백 없애줌(공백까지)

print('---------------------------------------')

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read()  # 내용 없음 : *커서가 파일의 끝으로 옮겨졌기 때문
    print('>', content)

print('---------------------------------------')

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()  # *한줄한줄 읽어옴
    # print(line)
    while line:
        print(line, end='###')
        line = f.readline()

print()
print('---------------------------------------')

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()  # 모든 문장을 줄바꿈을 기준으로 list로 가지고옴
    print(contents)
    for c in contents:
        print(c, end='***')

print()
print('---------------------------------------')

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average: {:6.3}'.format(sum(score) / len(score)))


# 파일 쓰기
# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')


# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0, 50)))
        f.write('\n')
    

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n','Park\n','Tae\n']
    f.writelines(list)


# 예제5
with open('./resource/text4.txt', 'w') as f:
    # *콘솔로 찍히는 것이 아니라 f에 print의 내용을 씀
    print('Test contests1!', file=f)
    print('Test contests2!', file=f)
