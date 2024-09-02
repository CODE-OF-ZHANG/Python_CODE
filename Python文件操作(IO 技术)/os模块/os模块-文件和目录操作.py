"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : os模块-文件和目录操作
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import os
# 获取文件和文件夹相关的信息
print(os.name)  # windows->nt; linux 和 unix->posix
print(os.sep)  # windows->\; linux 和 unix->/
print(repr(os.linesep))  # windows->\r\n;linux-->\n\
print(os.stat('os模块-文件和目录操作.py'))

# 关于工作目录的操作
print(os.getcwd())  # 返回当前工作目录
# os.chdir('d:')  # 改变当前的工作目录为：d:盘根目录

# 创建目录、创建多级目录、删除
os.mkdir('电影')  # 创建目录
os.makedirs('音乐/周杰伦/稻香')  # 创建多级目录
os.makedirs('../电影1')  # ../表示上一级

print(os.listdir('电影'))




