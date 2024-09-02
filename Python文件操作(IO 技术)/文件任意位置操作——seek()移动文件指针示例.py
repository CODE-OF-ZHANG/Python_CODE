"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 文件任意位置操作——seek()移动文件指针示例
# @Software: PyCharm
# @Date : 2024/1/26 
"""

with open('中文乱码.txt', 'r', encoding='utf-8') as f:
    print('文件名：{0}'.format(f.name))
    print(f.tell())
    print('读取的内容：{0}'.format(str(f.readline())))
    print(f.tell())
    f.seek(0, 0)
    print('读取的内容：{0}'.format(str(f.readline())))
