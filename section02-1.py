# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
# print('Hello Python!')
# print("Hello Python!")
# print("""Hello Python!""")
# print('''Hello Python!''')

# print()

# # Separator 옵션 사용
# print('s', 'e', 'p', 'a', 'r', 'a', 't', 'o', 'r', sep='~')
# print('T', 'E', 'S', 'T')
# print('T', 'E', 'S', 'T', sep='')
# print('2019', '02', '19', sep='-')
# print('nickname', 'google.com', sep='@')

# print()

# # end 옵션 사용
# print('Welcome To', end=' ')
# print('the black friday', end=' ')
# print('piano notes')
# # 출력: Welcome To the black friday piano notes

# print()

# # format 사용
# print('{} and {}'.format('You', 'Me'))  # 출력: You and Me
# print("{0} and {1} and {0}".format('You', 'Me'))  # 출력: You and Me and You
# print('{a} are {b}'.format(a='You', b='Me'))  # 출력: You and Me

# # %s: 숫자, %d: 정수, %f: 실수
# print("%s's favorate number is %d" %
#       ('Ram', 2))  # 출력: Ram's favorate number is 2

# print("Test1: %5d, Price: %4.2f" % (776, 6543.123))
# print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6543.123))
# print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6543.123))
# # 모두 같은 출력> Test1:   776, Price:  6543.12

# print()

print("'you'")
print('\'you\'')
print("""'you'""")
print('\\you\\')
print('\t\ttest')
