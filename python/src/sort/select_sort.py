"""
选择排序
时间复杂度：O(n^2)
空间复杂度：1
"""


def select_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swap(i, j)

    return arr
