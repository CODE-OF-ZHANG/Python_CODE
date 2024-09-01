"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 05-类的其他内置方法
# @Software: PyCharm
# @Date : 2024/1/26 
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # stu1 = Student('张三', 18)
    # print(stu1)  # 输出：<__main__.Student object at 0x000001EDFFB09FD0>
    # print(str(stu1))  # 输出：<__main__.Student object at 0x000001EDFFB09FD0>
    # __str__魔法方法: 实现类对象转字符串的行为
    def __str__(self):
        return f'name:{self.name}, age:{self.age}'

    # __lt__魔法方法: 两个类对象进行大于或小于的比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔法方法: 两个类对象进行大于等于或小于等于的比较
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔法方法: 两个类对象进行相等的比较
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student('张三', 18)
stu2 = Student('李四', 19)
# print(stu1)  # 输出：name:张三, age:18
# print(str(stu1))  # 输出：name:张三, age:18

# print(stu1 < stu2)  # 输出：True
# print(stu1 > stu2)  # 输出：False

# print(stu1 <= stu2)  # 输出：True
# print(stu1 >= stu2)  # 输出：False

print(stu1 == stu2)  # 输出：False
