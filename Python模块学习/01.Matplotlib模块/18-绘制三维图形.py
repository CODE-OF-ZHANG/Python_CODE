"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 18-绘制三维图形
# @Software: PyCharm
# @Date : 2024/1/26 
"""
import matplotlib

matplotlib.use('TkAgg')
# # 导入模块
# import matplotlib.pyplot as plt
# # 导入3d包
# from mpl_toolkits.mplot3d import Axes3D
# # % matplotlib inline
#
# # 创建X，Y，Z
# X = [1, 1, 2, 2]
# Y = [3, 4, 4, 3]
# Z = [1, 100, 1, 1]
# figure = plt.figure()
# # 创建Axes3D对象
# ax = Axes3D(figure)
# ax.plot_trisurf(X, Y, Z)
# # 显示绘制图形
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
#
# ax3d = fig.add_subplot(projection='3d')  # 创建3d坐标系
# # from mpl_toolkits.mplot3d import Axes3D
# # ax = Axes3D(fig)   #创建3d坐标系的第二种方法
#
# theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)
# x = np.sin(theta)
# y = np.cos(theta)
# z = np.linspace(-2, 2, 100)
#
# ax3d.plot(x, y, z)  # 绘制3d螺旋线
#
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax3d = fig.add_subplot(projection='3d')  # 创建3d坐标系
#
# x = np.random.randn(50)
# y = np.random.randn(50)
# z = np.random.randn(50)
# s = np.random.randn(50) * 100
#
# # ax3d.scatter(x,y,z)  #绘制3d散点图
# # ax3d.scatter(x,y,z,marker=['*','o',...]) #设置不同的点样式
# ax3d.scatter(x, y, z, s=s, c=s)  # 绘制3d散点图
# ax3d.scatter(x, y, -3, zdir='z', c='r')  # 3d坐标系绘制平面散点
#
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax3d = fig.add_subplot(projection='3d')  # 创建3d坐标系
# np.random.seed(202201)
#
# t = np.linspace(-np.pi, np.pi, 50)
# x = np.sin(t)
# y = np.cos(t)
# z = np.linspace(-2, 2, 50)
#
# ax3d.stem(x, y, z)  # 绘制3d火柴图
# # ax3d.stem(x,y,z,orientation="x", bottom=-2) #火柴根在yz平面
#
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax3d = fig.add_subplot(projection='3d')  # 创建3d坐标系
#
# x, y = np.mgrid[-3:3:0.2, -3:3:0.2]
# z = x * np.exp(-x ** 2 - y ** 2)
#
# ax3d.plot_surface(x, y, z)
# ax3d.plot_surface(x, y, z, rstride=2, cstride=2)  # 两条线合并为一条线
# ax3d.plot_surface(x, y, z, rcount=16, ccount=18)  # 设置最大显示线条数
# ax3d.plot_surface(x, y, z, cmap="YlOrRd")
# ax3d.plot_surface(x, y, z, cmap="YlOrRd")
#
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax3d = fig.add_subplot(121, projection='3d')

# filled为bool类型数组，在True的元素下标位置绘制体元素
i, j, k = np.indices((3, 3, 3))
filled = (i == j) & (j == k)  # 3行3列3层，对角线为True
c = plt.get_cmap('RdBu')(np.linspace(0, 1, 27)).reshape(3, 3, 3, 4)

# ax3d.voxels(filled)             #filled为True的位置绘制六面体
ax3d.voxels(filled, facecolors=c)  # filled为True的位置绘制六面体,并设置颜色

#
ax3d = fig.add_subplot(122, projection='3d')
# x,y,z=np.indices((3,4,5))
# ax3d.voxels(x,y,z,filled)

plt.show()
