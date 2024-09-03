# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 05_人脸检测
# @Software: PyCharm
# @Date : 2024/5/19

import cv2 as cv


def face_detect_demo():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('D:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml')
    faces = face_detector.detectMultiScale(gray, 1.02, 5)
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x + w, y + h), color=(0, 0, 255))
    cv.imshow('result', src)


src = cv.imread('lena.jpg')
cv.imshow('result', src)
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
