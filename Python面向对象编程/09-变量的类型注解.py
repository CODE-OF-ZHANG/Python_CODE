"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 09-变量的类型注解
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import json
import random
# 变量的类型注解

var1: int = 10
var2: str = '张三'
var3: bool = True

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"name": "张三"}

# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, str, bool] = (1, "张三", True)
my_dict1: dict[str, str] = {"name": "张三"}


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 在注释中进行类型注解
var_1: random.randint(1, 10)  # type: int
var_2: json.loads('{"name": "张三"}')  # type: dict


# 函数形参的类型注解
def add(x: int, y: int):
    return x + y


# 函数形参和返回值的类型注解
def fnuc(data: list) -> list:
    return data
