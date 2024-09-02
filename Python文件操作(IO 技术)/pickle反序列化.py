"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : pickle反序列化
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import pickle

with open('data.dat', 'rb') as f:
    a = pickle.load(f)
print(a)
