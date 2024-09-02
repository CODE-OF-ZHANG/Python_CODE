"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 测试递归：求n的阶乘
# @Software: PyCharm
# @Date : 2024/1/26 
"""


# 测试递归
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


a = factorial(5)
print(a)
