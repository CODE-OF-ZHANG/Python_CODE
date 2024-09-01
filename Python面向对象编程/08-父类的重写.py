"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 08-父类的重写
# @Software: PyCharm
# @Date : 2024/1/26 
"""


# 定义父类
class Phone:
    IMEI = None  # 序列号
    producer = 'APPLE'  # 厂商

    def call_by_4g(self):
        print('4g通话')


# 定义子类
class MyPhone(Phone):
    producer = 'HUAWEI'  # 复写父类属性

    def call_by_4g(self):  # 复写父类方法
        print('可用5g通话')
        # 调用父类属性和方法
        # 方法一
        # print(f'调用父类属性[1]:{Phone.producer}')  # 调用父类属性
        # Phone.call_by_4g(self)  # 调用父类方法
        # 方法二
        print(f'调用父类属性[2]:{super().producer}')  # 调用父类属性
        super().call_by_4g()  # 调用父类方法


phone = MyPhone()
print(phone.producer)
phone.call_by_4g()



# # 定义父类
# class Phone:
#     IMEI = None  # 序列号
#     producer = 'APPLE'  # 厂商
#
#     def call_by_4g(self):
#         print('4g通话')
#
#
# # 定义子类
# class MyPhone(Phone):
#     producer = 'HUAWEI'  # 复写父类属性
#
#     def call_by_4g(self):  # 复写父类方法
#         print('可用5g通话')
#
#
# phone = MyPhone()
# print(phone.producer)  # 输出：HUAWEI
# phone.call_by_4g()  # 输出：可用5g通话
