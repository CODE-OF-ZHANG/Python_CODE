"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 11-绘制柱状图
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import matplotlib

matplotlib.use('TkAgg')
# 导入matplotlib模块
import matplotlib.pyplot as plt

# 创建x，y坐标
x = [1980, 1985, 1990, 1995]
y = [1000, 3000, 4000, 5000]
x_label = ['1980年', '1985年', '1990年', '1995年']
# 调用bar函数绘制柱状图
plt.bar(x, y, width=3)  # 通过width修改柱的宽度，数值为标准柱宽度的倍数
# 设置字体解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 通过xticks修改x坐标的值
# plt.xticks(x, x)
plt.xticks(x, x_label)
# 设置x，y轴的名称
plt.xlabel('年份')
plt.ylabel('销量')
# 设置图例名称
plt.title('年份销量对比图')
# 显示绘制图形
plt.show()
