"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : CSV文件读取
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import csv
with open('豆瓣.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for row in read:
        print(row)
