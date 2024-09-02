"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 实现将压缩包解压缩到指定文件夹
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import shutil
import zipfile
# 解压缩：
z2 = zipfile.ZipFile("a.zip", "r")
z2.extractall("d:/")  # 设置解压的地址
z2.close()
