"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 结合异常机制finally 确保关闭文件对象
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# 结合异常机制 finally 确保关闭文件对象
try:
    f = open('close关闭流.txt', 'w')
    str1 = 'hello'
    f.write(str1)
except BaseException as e:
    print(e)
finally:
    f.close()
