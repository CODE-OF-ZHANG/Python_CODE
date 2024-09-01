"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 03-面向对象的编程套路
# @Software: PyCharm
# @Date : 2024/1/26 
"""

"""
需求：设计一个闹钟类，创建两个闹钟对象并使其工作
"""


# 定义一个闹钟类
class Clock:
    id = None  # 闹钟编号
    price = None  # 闹钟价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


colck1 = Clock()
colck1.id = '00301'
colck1.price = 19.9
print(f'闹钟ID：{colck1.id},价格是{colck1.price}')
colck1.ring()

colck2 = Clock()
colck2.id = '00302'
colck2.price = 39.9
print(f'闹钟ID：{colck2.id},价格是{colck2.price}')
colck2.ring()
