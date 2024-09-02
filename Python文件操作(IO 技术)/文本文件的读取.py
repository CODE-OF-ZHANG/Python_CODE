"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 文本文件的读取
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# 文件较小，一次将文件内容读入到程序中
with open('with语句(上下文管理器).txt', 'r', encoding='utf-8') as f:
    str1 = f.read()
    print(str1)

# 使用迭代器（每次返回一行）读取文本文件
# with open('中文乱码.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         print(i, end='')
