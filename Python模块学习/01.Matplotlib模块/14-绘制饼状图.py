"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 14-绘制饼状图
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import matplotlib

matplotlib.use('TkAgg')
# 导入模块
import matplotlib.pyplot as plt
# 男女人数及比例 单位：万人
man = 71135
woman = 68185
# 比例
man_perc = man / (man + woman)
woman_perc = woman / (man + woman)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 添加名称
labels = ['男', '女']
# 颜色
colors = ['biue', 'orange']
# 绘制饼状图 调用pie方法
plt.pie([man_perc, woman_perc], labels=labels, explode=(0, 0.05), autopct='%0.1f%%')
# 显示绘制图形
plt.show()
