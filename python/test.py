import random
from time import time


def main():
    scort = 0
    start = time()
    for i in range(0,5):
        a = random.randint(100,999)
        b = random.randint(0,9)
        print(f"{a} * {b} = ?")
        result = input()
        print(result)
        if int(result) == (a*b):
            print("回答正确，加2分")
            scort = scort+2
        else:
            print("回答错误")
    end = time()
    print(f"得分：{scort}, 用时：{(end - start)}秒")

if __name__ == '__main__':
    main()
    