# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 04_画图
# @Software: PyCharm
# @Date : 2024/5/19


import cv2 as cv

img = cv.imread('1.png')
# 画矩形
x, y, w, h = 50, 50, 80, 80
cv.rectangle(img, (x, y, x + w, y + h), color=(0, 255, 0), thickness=2)  # color=BGR
cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 0, 255), thickness=2)
cv.imshow('result image', img)
cv.waitKey(0)
cv.destroyAllWindows()
