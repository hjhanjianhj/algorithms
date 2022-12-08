"""
插入法排序
时间复杂度：O(n^2)
空间复杂度：1
"""


def insertion_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    for i in range(1, n):
        x = i
        while x > 0 and arr[x - 1] > arr[x]:
            swap(x - 1, x)

    return arr
