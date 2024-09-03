"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 09-绘制不同样式不同颜色的线
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import matplotlib

matplotlib.use('TkAgg')
# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 创建0-10之间的100个等差数列
x = np.linspace(0, 10, 100)
# 调用绘制plot方法
plt.plot(x, x + 0, '-g')  # 实线 绿色
plt.plot(x, x + 1, '--c')  # 虚线 浅蓝色
plt.plot(x, x + 2, '-.k')  # 点划线 黑色
plt.plot(x, x + 3, 'or')  # 圆标记 红色
plt.plot(x, x + 4, 'xy')  # 叉叉 黄色
plt.plot(x, x + 5, 'dm')  # 砖石 品红色
# 显示绘制的图
plt.show()
