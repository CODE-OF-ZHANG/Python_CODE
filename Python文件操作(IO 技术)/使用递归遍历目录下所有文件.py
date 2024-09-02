"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 使用递归遍历目录下所有文件
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import os

allfile = []


def getFiles(path, level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getFiles(filepath, level + 1)
        allfile.append("\t" * level + filepath)


getFiles(os.getcwd(), 0)
for f in reversed(allfile):
    print(f)
