# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 03-使用 SpeechLib 实现文本转换语音
# @Software: PyCharm
# @Date : 2024/4/30

from comtypes.client import CreateObject
from comtypes.gen import SpeechLib  # 导入 SpeechLib
engine = CreateObject("SAPI.SpVoice")  # 创建 SAPI.SpVoice 对象的实例
stream = CreateObject("SAPI.SpFileStream")  # 创建 SAPI.SpFileStream 对象的实例
infile = 'demo.txt'
outfile = 'demo_audio.wav'
stream.Open(outfile, SpeechLib.SSFMCreateForWrite)  # 输出文件，准备写入音频数据
engine.AudioOutputStream = stream  # 音频输出流设置为 stream 对象
f = open('demo', 'r', encoding='utf-8')  # 打开输入文本文件
TheText = f.read()  # 读取文件
f.close()  # 关闭文件
engine.speak(TheText)  # 使用语音引擎将文本转换为语音并输出。
stream.close()  # 关闭音频流，完成音频文件的写入
