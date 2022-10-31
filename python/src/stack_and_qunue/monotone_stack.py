"""
给定一个数组arr，找到每一个i位置左边和右边离i位置最近且值比arr[i]小的位置，返回所有位置相应的信息
arr = [3,4,1,5,6,2,7]
[
    [-1,2],
    [0,2],
    [-1,-1],
    [2,5],
    [3,5],
    [2,-1],
    [5,-1]
]
"""


def get_no_rep_near_less(arr):
    """
    不包含重复值
    :param arr:
    :return:
    """
    rs = [[0] * 2] * len(arr)
    stack = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            curr_index = stack.pop()
            right_index = i
            left_index = stack[-1] if stack else -1
            rs[curr_index] = [left_index, right_index]

        stack.append(i)

    while stack:
        curr_index = stack.pop()
        right_index = -1
        left_index = stack[-1] if stack else -1
        rs[curr_index] = [left_index, right_index]

    return rs

if __name__ == '__main__':
    arr = [3,4,1,5,6,2,7]
    arr = [3, 1, 3, 4, 3, 5, 3, 2, 2]
    ret = get_no_rep_near_less(arr)
    print(ret)

    arr = [3,1,3,4,3,5,3,2,2]