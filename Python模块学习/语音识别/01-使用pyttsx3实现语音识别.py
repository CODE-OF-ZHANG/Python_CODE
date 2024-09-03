# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 01-使用pyttsx3实现语音识别
# @Software: PyCharm
# @Date : 2024/4/30
# pip install pocketsphinx -i https://pypi.tuna.tsinghua.edu.cn/simple some-package


import pyttsx3 as pyttsx

engine = pyttsx.init()
engine.say('独断万古荒天帝, 唯负罪州火桑女')
engine.runAndWait()
