# -*- coding: utf-8 -*-
# @Author : ZX
# @File : OpenCV基础
# @Software: PyCharm
# @Date : 2024/3/29


import cv2 as cv

print(cv.__version__)  # 打印OpenCV版本

# 加载图片
img = cv.imread("1.png")
# 打印图像类型
print(type(img))
print(img)
cv.imshow("image", img)
# 等待时间, 毫米级, 0表示按任意键终止
cv.waitKey(0)
cv.destroyAllWindows()


