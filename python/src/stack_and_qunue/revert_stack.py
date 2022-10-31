"""
不额外使用栈，逆序栈

1. 首先通过一个递归实现返回并删除一个栈底数据
2. 然后实现逆序栈
"""
from typing import List


def getAndRemoveLastData(stack: List):
    data = stack.pop()
    if not stack:
        return data
    result = getAndRemoveLastData(stack)
    stack.append(data)
    return result

def revert(stack: List):
    if not stack:
        return
    data = getAndRemoveLastData(stack)
    revert(stack)
    stack.append(data)


if __name__ == '__main__':
    stack = [2,3,5,6,3,5]

    revert(stack)
    print(stack)