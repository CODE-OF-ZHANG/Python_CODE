# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 03_图片缩放
# @Software: PyCharm
# @Date : 2024/5/19


# # 加载部分图像数据
# import cv2 as cv
#
# # 加载图片
# img = cv.imread('1.png')
#
# # 截取部分图像
# cat = img[0:200, 0:200]
#
# # 显示截取的图像
# cv.imshow("cat", cat)
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv

img = cv.imread('1.png')
cv.imshow('input image', img)
# 修改图片的尺寸
# resize_img=cv.resize(img,dsize=(110,160))
resize_img = cv.resize(img, dsize=(400, 360))
print(resize_img.shape)
cv.imshow('resize_img', resize_img)
# 如果键盘输入的是 q 时候 退出
while True:
    if ord('q') == cv.waitKey(0):
        break
cv.destroyAllWindows()
