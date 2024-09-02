"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 练习：列出指定目录下所有的.py 文件，并输出文件名
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# 方法一
# import os.path
# path = os.getcwd()
# file_list = os.listdir(path)
# for filename in file_list:
#     if filename.endswith('py'):
#         print(filename)

# 方法二
import os.path
path = os.getcwd()
file_list = os.listdir(path)
filename = [filename for filename in file_list if filename.endswith('py')]
for f in filename:
    print(f)



