"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 02-成员方法
# @Software: PyCharm
# @Date : 2024/1/26 
"""


# 定义一个带有成员方法的类
class Student:
    # 成员变量
    name = None  # 学生的姓名

    # 定义方法
    def say_hi1(self):
        print(f'大家好，我叫{self.name}')  # 成员方法中访问成员变量必须要用self关键字！

    def say_hi2(self, msg):
        print(f'大家好，我是{self.name},{msg}')  # msg为外部传入的不需要用self！


stu1 = Student()
stu1.name = '张三'
stu1.say_hi1()
stu2 = Student()
stu2.name = '李四'
stu2.say_hi2('请多多关照')
