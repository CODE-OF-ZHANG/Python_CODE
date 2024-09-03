"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 07-绘制散点图
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')

# 导入matplotlib和numpy模块
import matplotlib.pyplot as plt
import numpy as np

# 生成0-10之间的100个等差数列
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)
# 绘制正弦余弦图
# plt.plot(x, sin_y, 'o')  # 加一个参数'o'效果与scatter一样
# plt.plot(x, cos_y, 'o')
# 绘制散点图
plt.scatter(x, sin_y)
plt.scatter(x, cos_y)
# 显示绘制的图
plt.show()
