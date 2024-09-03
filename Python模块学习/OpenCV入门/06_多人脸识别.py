# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 06_多人脸识别
# @Software: PyCharm
# @Date : 2024/5/19

# pip install dlib -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
import cv2 as cv


def face_detect_demo():
    # 将图片灰度
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 加载特征数据
    face_detector = cv.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt_tree.xml')
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.01)
    for x, y, w, h in faces:
        print(x, y, w, h)
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    # 显示图片
    cv.imshow('result', img)


# 加载图片
img = cv.imread('face3.jpg')
# 调用人脸检测方法
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
