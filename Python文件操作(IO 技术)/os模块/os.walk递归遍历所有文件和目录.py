"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : os.walk递归遍历所有文件和目录
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import os

all_files = []
path = os.getcwd()
list_files = os.walk(path)
for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath, dir))
    for name in filenames:
        all_files.append(os.path.join(dirpath, name))
# 打印子目录和子文件
for file in all_files:
    print(file)
