"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 设置中文乱码问题
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# f = open(r'中文乱码.txt', 'a', encoding='utf-8')
# s = '你好！\n'
# a = ['a\n', 'b\n', 'c\n']
# f.write(s)  # 把字符串 s 写入到文件中
# f.writelines(a)  # 把字符串列表写入文件中，不添加换行符
# f.close()

f = open(r'中文乱码.txt', 'w', encoding='utf-8')
s = '你好！\n'
f.write(s)  # 把字符串 s 写入到文件中
f.close()
