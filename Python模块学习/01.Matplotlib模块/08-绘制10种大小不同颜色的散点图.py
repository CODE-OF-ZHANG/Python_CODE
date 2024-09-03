"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 08-绘制10种大小不同颜色的散点图
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib和numpy模块
import matplotlib.pyplot as plt
import numpy as np

# 创建x, y
np.random.seed(0)  # 执行多次，通过设置相同的种子，可以确保每次运行生成的随机数序列是可重复的。
x = np.random.rand(100)  # 生成100个[0, 1)之间的随机数
y = np.random.rand(100)
# 生成100种不同大小
size = np.random.rand(100) * 1000  # 乘一千扩大范围，效果跟明显
# 生成100种不同的颜色
color = np.random.rand(100)
# print(x)
# 绘制散点图
plt.scatter(x, y, s=size, c=color, alpha=0.8)  # s表示大小, c表示颜色，alpha表示透明度
plt.show()
