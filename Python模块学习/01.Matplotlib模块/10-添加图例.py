"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 10-添加图例
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
# 给plot方法添加参数label
plt.plot(x, x + 0, '-g', label='-g')  # 实线 绿色
plt.plot(x, x + 1, '--c', label='--c')  # 虚线 浅蓝色
plt.plot(x, x + 2, '-.k', label='-.k')  # 点划线 黑色
plt.plot(x, x + 3, 'or', label='or')  # 圆标记 红色
plt.plot(x, x + 4, 'xy', label='xy')  # 叉叉 黄色
plt.plot(x, x + 5, 'dm', label='dm')  # 砖石 品红色
# 使用legend()添加图例
# 通过参数loc设置图例位置，默认在upper left左上角， fancybox边框  framealpha透明度  shadow阴影  borderpad边框宽度
plt.legend(loc='lower right', fancybox=True, framealpha=0.5, shadow=True, borderpad=1)
# 显示绘制的图
plt.show()
