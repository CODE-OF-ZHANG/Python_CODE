"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 03-二分查找
# @Software: PyCharm
# @Date : 2024/1/26
"""


def binary_search(li, var):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == var:
            return mid
        elif li[mid] > var:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(li1, 4))
