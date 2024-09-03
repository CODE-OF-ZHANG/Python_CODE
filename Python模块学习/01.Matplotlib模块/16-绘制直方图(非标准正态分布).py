"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 16-绘制直方图(非标准正态分布)
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 调用np.rangom.normal()指定期望和方差的正态分布
x = np.random.normal(0, 0.8, 1000)
y = np.random.normal(-2, 1, 1000)
z = np.random.normal(3, 2, 1000)
kwargs = dict(bins=100, alpha=0.5)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 设置图形标题
plt.title('非标准正态分布直方图')
# 绘制直方图
plt.hist(x, **kwargs)
plt.hist(y, **kwargs)
plt.hist(z, **kwargs)
# 显示绘制的图形
plt.show()
