"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : selenium入门
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# 导包
from selenium import webdriver

# 加载驱动
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 网址
driver.get('https://www.csdn.net/')
