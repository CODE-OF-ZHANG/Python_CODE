"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 13-柱状图的实际应用
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import matplotlib

matplotlib.use('TkAgg')
# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 准备数据如 电影名称以及电影票房数
movie_name = ['千与千寻', '玩具总动员4', '黑衣人：全球追缉']
# 连续3天的票房数
real_num1 = [7548, 4013, 1673]
real_num2 = [5435, 1845, 1028]
real_num3 = [4203, 3305, 1369]
x = np.arange(len(movie_name))
# 绘制柱状图
# 设置宽度
width = 0.3
plt.bar(x, real_num1, alpha=0.5, width=width, label=movie_name[0])
plt.bar([i + width for i in x], real_num2, alpha=0.5, width=width, label=movie_name[1])
plt.bar([i + 2 * width for i in x], real_num3, alpha=0.5, width=width, label=movie_name[2])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 设置x坐标的值， 第一天 第二天 第三天
x_label = ['第{}天'.format(i + 1) for i in x]
plt.xticks([i + width for i in x], x_label)
# 添加y轴名称
plt.ylabel('票房数')
# 添加图例
plt.legend()
# 添加标题
plt.title('电影票房数')
# 显示绘制图形
plt.show()
