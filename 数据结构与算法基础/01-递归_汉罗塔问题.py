"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 01-递归_汉罗塔问题
# @Software: PyCharm
# @Date : 2024/1/26 
"""


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('moving from %s to %s' % (a, c))
        hanoi(n - 1, b, c, a)


hanoi(3, 'A', 'B', 'C')
