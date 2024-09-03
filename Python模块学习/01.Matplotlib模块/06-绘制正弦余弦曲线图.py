"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 06-绘制正弦余弦曲线图
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib和numpy模块
import matplotlib.pyplot as plt
import numpy as np

# 生成0-10之间100个等差数列
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)  # sin函数用于计算给定角度的正弦值
cos_y = np.cos(x)  # cos函数用于计算给定角度的余弦值
# 调用绘制plot方法
plt.plot(x, sin_y)  # 默认第一条曲线颜色为蓝色，第二条为橘色
plt.plot(x, cos_y)
# 保存图片
plt.savefig('正弦余弦曲线图.jpg')
# 显示绘制的图片
plt.show()
