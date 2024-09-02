"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 二进制文件的读取和写入
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# 二进制文件的读取
with open('aa.gif', 'rb') as f:
    line = f.read()

# 二进制文件的写入
with open('copy_aa.gif', 'wb') as f:
    f.write(line)
