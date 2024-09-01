"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 07-类的继承基础语法
# @Software: PyCharm
# @Date : 2024/1/26 
"""


# # 单继承演示
# #
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
# class Phone2022(Phone):
#     face_id = '10001'
#
#     def call_by_5g(self):
#         print('5g通话')
#
#
# phone = Phone2022()
# phone.call_by_4g()  # 输出：4g通话
# print(phone.producer)  # 输出：APPLE
# phone.call_by_5g()  # 输出：5g通话
# print(phone.face_id)  # 输出：10001


# 多继承演示
# 定义父类
class Phone:
    IMEI = None  # 序列号
    producer = 'HM'  # 厂商

    def call_by_4g(self):
        print('4g通话')


class NFCReader:
    nfc_type = '第五代'
    producer = 'HM'

    def read_card(self):
        print('读取NFC卡')

    def write_card(self):
        print('写入NFC卡')


class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print('红外遥控开启')


# 定义子类
class MyPhone(Phone, NFCReader, RemoteControl):
    pass


phone = MyPhone()
print(phone.producer)  # 输出：HM
print(phone.nfc_type)  # 输出：第五代
phone.read_card()  # 输出：读取NFC卡
phone.call_by_4g()  # 输出：4g通话
phone.control()  # 输出：红外遥控开启

