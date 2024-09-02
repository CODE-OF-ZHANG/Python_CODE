"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 实现文件的拷贝
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import shutil

# copy 文件内容
shutil.copy('1.txt', '1_copy.txt')
# "音乐"文件夹不存在才能用。
shutil.copytree("电影/学习", "音乐", ignore=shutil.ignore_patterns("*.html", "*.htm"))
