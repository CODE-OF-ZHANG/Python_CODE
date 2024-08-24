# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 20_图片灰色处理
# @Software: PyCharm
# @Date : 2024/5/19

# # 灰色显示
# import cv2 as cv
#
# # cv2 读取图片的通道是 BGR（蓝绿红）
# # PIL 读取图片的通道是 RGB
# img = cv.imread('1.png', cv.IMREAD_GRAYSCALE)
# # 打印信息
# # print(img)
# cv.imshow("image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv

src = cv.imread('1.png')
cv.imshow('input image', src)
# cv2 读取图片的通道是 BGR（蓝绿红）
# PIL 读取图片的通道是 RGB
gray_img = cv.cvtColor(src, code=cv.COLOR_BGR2GRAY)
cv.imshow('gray_image', gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
# 保存图片
cv.imwrite('gray_lena.jpg', gray_img)
