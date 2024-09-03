"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 12-bar以及barh函数的使用
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# # 导入模块
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 创建x，y
# np.random.seed(0)
# x = np.arange(5)  # 生成[0, 5)之间的整数
# y = np.random.randint(-5, 5, 5)  # 随机生成[-5, 5)之间的整数
# # 将画布分为一行两列，在第一部分用bar函数画
# plt.subplot(1, 2, 1)
# # 在0位置处添加水平方向蓝色线条
# plt.axhline(0, color='blue', linewidth=3)
# plt.bar(x, y, color='blue')
# # 在第二部分用barh函数画
# plt.subplot(1, 2, 2)
# # 在0位置处添加垂直方向红色线条
# plt.axvline(0, color='red', linewidth=2)
# plt.barh(x, y, color='red')
# # 显示绘制图形
# plt.show()

# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 创建x，y
np.random.seed(0)
x = np.arange(5)  # 生成[0, 5)之间的整数
y = np.random.randint(-5, 5, 5)  # 随机生成[-5, 5)之间的整数
v_bar = plt.bar(x, y, color='blue')
# 对y大于0的合作为蓝色，小于0设置为绿色
for bar, height in zip(v_bar, y):
    if height < 0:
        bar.set(color='green')
# 显示绘制图形
plt.show()
