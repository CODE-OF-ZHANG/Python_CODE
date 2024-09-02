"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : pickle 序列化
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import pickle

with open(r"data.dat", "wb") as f:
    a1 = ['ZX', [123], {'age': 18}]
    pickle.dump(a1, f)
