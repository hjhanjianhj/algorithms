"""
有一个整形数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。
例如，数组为[4,3,5,4,3,3,6,7]，窗口大小为3时：
[4  3  5] 4  3  3  6  7     窗口中最大值为5
 4 [3  5  4] 3  3  6  7     窗口中最大值为5
 4  3 [5  4  3] 3  6  7     窗口中最大值为5
 4  3  5 [4  3  3] 6  7     窗口中最大值为4
 4  3  5  4 [3  3  6] 7     窗口中最大值为6
 4  3  5  4  3 [3  6  7]    窗口中最大值为7
"""
from collections import deque


def max_window_array(arr, w):
    d_queue = deque()
    result = []
    index = 0
    for i, num in enumerate(arr):
        while d_queue and arr[d_queue[-1]] <= num:
            d_queue.pop()
        d_queue.append(i)
        if d_queue[0] <= i-w:
            d_queue.popleft()
        if i >= w - 1:
            result.append(arr[d_queue[0]])

    return result


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    # arr = [1,2,3,4,5,6,7,8,9,10]
    w = 3
    result = max_window_array(arr, w)

    print(result)