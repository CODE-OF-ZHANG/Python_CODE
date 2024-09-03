"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 15-绘制直方图(标准正态分布)
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 生成1000个标准正态分布随机数
x = np.random.randn(1000)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 设置标题
plt.title('标准正态分布直方图')
# 绘制直方图
plt.hist(x, bins=100)  # 将数据分成100个箱子
# 显示绘制的图形
plt.show()
