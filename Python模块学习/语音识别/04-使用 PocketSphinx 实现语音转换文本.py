# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 04-使用 PocketSphinx 实现语音转换文本
# @Software: PyCharm
# @Date : 2024/4/30


# import speech_recognition as sr
#
# r = sr.Recognizer()  # 调用识别器
# test = sr.AudioFile("demo_audio.wav")  # 导入语音文件
# with test as source:
#     # r.adjust_for_ambient_noise(source)
#     audio = r.record(source)  # 使用 record() 从文件中获取数据
# type(audio)
# # c=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
# c = r.recognize_sphinx(audio, language='en-US')  # 识别输出
# print(c)
import speech_recognition as sr

r = sr.Recognizer()

test = sr.AudioFile('demo_audio.wav')

with test as source:
    audio = r.record(source)

type(audio)

r.recognize_google(audio, language='zh-CN', show_all=True)

