"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 05-subplot的使用
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# # 导入matplotlib和numpy模块
# import matplotlib.pyplot as plt
# import numpy as np
# # 生成0-10之间的100个等差数列
# x = np.linspace(0, 10, 100)
# sin_y = np.sin(x)
# cos_y = np.cos(x)
# # 对画布进行分区处理, 将画布分为2行2列
# plt.subplot(2, 2, 1)  # 将图画在区1
# plt.plot(x, sin_y)
#
# plt.subplot(2, 2, 2)  # 将图画在区2
# plt.plot(x, cos_y)
# # 显示绘制的图片
# plt.show()


# 导入matplotlib和numpy模块
import matplotlib.pyplot as plt
import numpy as np

# 生成0-10之间的100个等差数列
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)
# 对画布进行分区处理, 将画布分为2行2列
plt.subplot(2, 2, 1)  # 将图画在区1
# 修改x, y轴的坐标
plt.xlim(-5, 20)
plt.ylim(-2, 2)
plt.plot(x, sin_y)

plt.subplot(2, 2, 2)  # 将图画在区2
plt.plot(x, cos_y)
# 显示绘制的图片
plt.show()
