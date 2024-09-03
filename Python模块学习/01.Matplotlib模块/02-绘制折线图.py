"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 02-绘制折线图
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib模块
import matplotlib.pyplot as plt

# 准备绘制点的坐标
x = [1, 3, 5, 7, 9]  # 绘制点的横坐标
y = [1, 9, 25, 49, 81]  # 绘制点的纵坐标
# 调用绘制plot方法
plt.plot(x, y)
# 显示绘制的图
plt.show()




