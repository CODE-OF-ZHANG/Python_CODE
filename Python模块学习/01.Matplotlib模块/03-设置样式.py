"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 03-设置样式
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib模块
import matplotlib.pyplot as plt

# 准备绘制点坐标
x = [1, 2, 3, 4, 5]
y = [1, 8, 27, 64, 125]
# 调用绘制plot方法
# 利用linewidth属性设置线条的宽度
plt.plot(x, y, linewidth=5)
# 添加x，y轴名称
plt.xlabel('x', fontsize=14)  # fontsize: 设置字体大小
plt.ylabel('x^3', fontsize=14)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签，字体可自由设置电脑中自带的字体
# 给图标添加标题
plt.title('折线绘制图', fontsize=24)
# 显示绘制的图
plt.show()
