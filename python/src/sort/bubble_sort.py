"""
 冒泡排序
 平均时间复杂度: O(n^2)
 平均空间复杂度：1
 稳定排序
"""


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swapped = True
                swap(i - 1, i)

    return arr
