"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 11-多态和抽象类
# @Software: PyCharm
# @Date : 2024/1/26 
"""


# # 多态
# # 定义父类
# class Animal:
#     def speak(self):
#         pass
#
#
# # 定义子类
# class Dog(Animal):
#     def speak(self):
#         print('汪汪汪')
#
#
# class Cat(Animal):
#     def speak(self):
#         print('喵喵喵')
#
#
# def make_noise(animal: Animal):
#     animal.speak()
#
#
# # 创建对象
# dog = Dog()
# cat = Cat()
#
# make_noise(dog)
# make_noise(cat)


# 抽象类
# 定义父类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print('美的空调制冷')

    def hot_wind(self):
        print('美的空调制热')

    def swing_l_r(self):
        print('美的空调左右摆风')


class GREE_AC(AC):
    def cool_wind(self):
        print('格力空调制冷')

    def hot_wind(self):
        print('格力空调制热')

    def swing_l_r(self):
        print('格力空调左右摆风')


def cool_wind(ac: AC):
    ac.cool_wind()


# 创建对象
midea = Midea_AC()
gree = GREE_AC()
cool_wind(midea)  # 输出：美的空调制冷
cool_wind(gree)  # 输出：格力空调制冷

