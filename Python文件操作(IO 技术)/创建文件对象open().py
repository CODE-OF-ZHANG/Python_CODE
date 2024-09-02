"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 创建文件对象open()
# @Software: PyCharm
# @Date : 2024/1/26 
"""

f = open(r'文件对象.txt', 'a')
s = 'hello world!'
f.write(s)
f.close()


