"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 练习-学生信息录入
# @Software: PyCharm
# @Date : 2024/1/26 
"""

"""
需求：设计一个类，记录学生的姓名,年龄,地址
1、使用for循环,配合input输入语句,并使用构造方法,完成学生信息的键盘录入
2、输入完成后,使用print语句,完成信息的输出
"""


class Student:
    def __init__(self, name, age, ip):
        self.name = name
        self.age = age
        self.ip = ip


for i in range(1, 11):
    print(f'当前录入第{i}位同学信息, 总共需录入10位同学信息')
    name = input('请输入学生姓名:')
    age = input('请输入学生年龄:')
    ip = input('请输入学生地址:')
    stu = Student(name, age, ip)
    print(f'学生{i}信息录入完毕，信息为【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.ip}】')
