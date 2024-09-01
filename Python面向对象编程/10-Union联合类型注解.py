"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 10-Union联合类型注解
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# 使用Union类型，必须先导包
from typing import Union

my_list: list[Union[int, str, dict]] = [1, 2, 'name', {"age": 18}]

my_dict: dict[str, Union[int, str, list]] = {"name": "张三", "age": 18, "grade": [98, 97]}

my_list1: list[Union[int, str, dict[Union[str, int]]]] = [1, 2, 'name', {"age": 18}]


# 函数的Union类型
def func(data: Union[int, str]) -> Union[int, str]:
    return data

# pip install selenium==4.0.0a1 -i https://pypi.tuna.tsinghua.edu.cn/simple