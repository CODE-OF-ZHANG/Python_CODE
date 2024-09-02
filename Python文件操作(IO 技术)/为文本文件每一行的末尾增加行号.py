"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 为文本文件每一行的末尾增加行号
# @Software: PyCharm
# @Date : 2024/1/26 
"""

with open('中文乱码.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.rstrip() + '  # ' + str(index + 1) + '\n' for index, line in enumerate(lines)]


with open('文本文件每一行的末尾增加行号.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
