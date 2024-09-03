# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 02-使用SAPI实现语音识别
# @Software: PyCharm
# @Date : 2024/4/30

from win32com.client import Dispatch

msg = "独断万古荒天帝, 唯负罪州火桑女"
speaker = Dispatch('SAPI.SpVoice')
speaker.Speak(msg)
del speaker
