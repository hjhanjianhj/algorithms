import unittest

from sort.bubble_sort import bubble_sort
from sort.insertion_sort import insertion_sort


def is_sorted(array):
    """
    检查数组是否有序的工具方法，数据从小到大排序
    :param array: 待检查的数组
    :return: 返回True，则说明传入的数组为升序排列，否则返回False
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


class TestSuite(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertTrue(is_sorted(bubble_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_insertion_sort(self):
        self.assertTrue(is_sorted(insertion_sort([1, 3, 2, 5, 65, 23, 57, 1232])))


if __name__ == '__main__':
    unittest.main()
