"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 判断字符
# @Software: PyCharm
# @Date : 2024/1/26 
"""

def check_input_type(input_char):
    if input_char.isupper():
        return "输入是大写字符"
    elif input_char.islower():
        return "输入是小写字符"
    elif input_char.isdigit():
        return "输入是数字"
    else:
        return "输入是特殊字符"

input_char = input("请输入一个字符：")
result = check_input_type(input_char)
print(result)