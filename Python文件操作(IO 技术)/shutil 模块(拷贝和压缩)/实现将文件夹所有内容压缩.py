"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 实现将文件夹所有内容压缩
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import shutil
import zipfile
# shutil.make_archive("音乐 2/movie", "zip", "电影/学习")
# 压缩:将指定的多个文件压缩到一个 zip 文件
z = zipfile.ZipFile("a.zip","w")
z.write("1.txt")
z.write("2.txt")
z.close()
