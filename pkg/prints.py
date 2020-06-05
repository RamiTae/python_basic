def prt1():
    print("I'm Nicebody!")


def prt2():
    print("I'm Goodboy!")


# 단위 실행(독립적으로 파일 실행): 단위 테스트
# *import로 다른 파일에서 실행할 때에는 아래 부분이 실행되지 않음.
if __name__ == "__main__":
    prt1()
    prt2()
