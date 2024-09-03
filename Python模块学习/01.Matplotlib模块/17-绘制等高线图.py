"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 17-绘制等高线图
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import matplotlib

matplotlib.use('TkAgg')
# 导入模块
import matplotlib.pyplot as plt
import numpy as np
# 生成100个-10-10之间的等差数列
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
# 计算出x，y相交的点X，Y
X, Y = np.meshgrid(x, y)
# 计算Z
Z = np.sqrt(X**2 + Y**2)  # 计算括号内值的开方
# 绘制等高线图
# plt.contour(X, Y, Z)
plt.contourf(X, Y, Z)  # 在contour()的基础上有颜色填充
# 显示绘制的图形
plt.show()


