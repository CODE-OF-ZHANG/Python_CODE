"""
-*- coding: utf-8 -*-
@Author : ZX
@File : 01-绘制直线图
@Software: PyCharm
@Date : 2024/1/26
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib模块
import matplotlib.pyplot as plt

# 准备要绘制点的坐标(1, 2) (4, 8)
# 调用绘制plot方法
plt.plot([1, 4], [2, 8])  # 第一个中括号里是绘制点的横坐标，第二个为绘制点的纵坐标
# 显示绘制的图
plt.show()
