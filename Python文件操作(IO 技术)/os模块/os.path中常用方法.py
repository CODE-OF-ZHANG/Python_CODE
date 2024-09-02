"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : os.path中常用方法
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import os.path
# 是否为绝对路径
print(os.path.isabs('d:/a1.txt'))
# 是否为目录
print(os.path.isdir('d:/a1.txt'))
# 是否为文件
print(os.path.isfile('d:/a1.txt'))
# 文件是否存在
print(os.path.exists('d:/a1.txt'))
# 文件大小
print(os.path.getsize('d:/a1.txt'))
# 输出所在目录
print(os.path.dirname('d:/a1.txt'))
# 返回创建时间
print(os.path.getctime('d:/a1.txt'))
# 返回最后访问时间
print(os.path.getatime('d:/a1.txt'))
# 返回最后修改时间
print(os.path.getmtime('d:/a1.txt'))
# 输出绝对路径
print(os.path.abspath('d:/a1.txt'))
# 返回元组：目录、文件
print(os.path.split('d:/a1.txt'))
# 返回元组：路径、扩展名
print(os.path.splitext('d:/a1.txt'))
# 路径连接
print(os.path.join('d: ', 'python', 'a.txt'))









