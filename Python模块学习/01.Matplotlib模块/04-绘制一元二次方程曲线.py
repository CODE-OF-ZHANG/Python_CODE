"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 04-绘制一元二次方程曲线
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib模块
import matplotlib.pyplot as plt

# 准备绘制点坐标
x = range(-100, 100)  # range函数用于生成一个整数序列，这里用于生成-100到100的整数
y = [i ** 2 for i in x]  # 列表推导式生成了一个包含-100到100的平方的列表
# 调用绘制plot方法
plt.plot(x, y)
# 保存图片
# plt.savefig('一元二次方程曲线图')  # 默认图片格式为png
plt.savefig('一元二次方程曲线图.jpg')  # 设置图片格式
# 显示绘制的图
plt.show()
