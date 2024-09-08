"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 02-顺序查找
# @Software: PyCharm
# @Date : 2024/1/26 
"""


def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search(li1, 4))
