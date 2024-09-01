"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 06-私有成员和私有方法
# @Software: PyCharm
# @Date : 2024/1/26 
"""


class Phone:
    # 构造方法
    def __init__(self, __is_5g_enable):
        # 设置私有变量
        self.__is_5g_enable = __is_5g_enable

    # 设置私有方法
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print('5G开启')
        else:
            print('5G关闭，使用4G网络')

    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中...')


phone = Phone(False)
phone.call_by_5g()


# class Phone:
#     IMEI = None  # 序列号
#     producer = None  # 厂商
#     __current_voltage = None  # 当前电压
#
#     def call_by_5g(self):
#         print('5g通话已开启')
#
#     def __keep_5g(self):
#         print('保持5g')
#
# phone = Phone()
# phone.__current_voltage = 3  # 不报错，但无效
# print(phone.__current_voltage)
