"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 01-类
# @Software: PyCharm
# @Date : 2024/1/26 
"""


# 类的创建
class Student:
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 创建方法
    def say_score(self):
        print('{0}的年龄是{1}'.format(self.name, self.age))


# 类的调用
s1 = Student('ZX', 19)
s1.say_score()
