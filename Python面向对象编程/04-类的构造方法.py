"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 04-类的构造方法
# @Software: PyCharm
# @Date : 2024/1/26 
"""

"""
需求：演示类的构造方法对成员变量进行赋值
"""


class Student:
    # 成员对象
    """
    __init__构造方法里对成员变量进行了声明并赋值
    所以成员对象这里可省略
    """
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print('Student类创建了一个类对象')  # 输出：Student类创建了一个类对象


stu1 = Student('张三', '18', '13066660')
print(stu1.name)  # 输出：张三
print(stu1.age)  # 输出：18
print(stu1.tel)  # 输出：13066660


# class Student:
#     name = None  # 姓名
#     age = None  # 年龄
#     tel = None  # 手机号
#
#
# stu1 = Student()
# stu1.name = '张三'
# stu1.age = 18
# stu1.tel = "1686400001"
# stu2 = Student()
# stu2.name = '李四'
# stu2.age = 19
# stu2.tel = "163200002"
