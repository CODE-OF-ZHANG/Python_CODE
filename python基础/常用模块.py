# import time
# # 时间戳 1970-1-1到现在的秒数
# print(time.time())
#
# # 让程序进入休眠的方法
# # time.sleep(5) # 一般是放整秒
# print('雨墨老师')
#
# # 获取当前详细的时间
# print(time.localtime())
#
# # 打印时间
# print(time.asctime(time.localtime()))
#
# # 年月日 星期几 %A--星期几
# print(time.strftime('%Y-%m-%d %A',time.localtime()))
# # 时分秒 %p-上午或者下午
# print(time.strftime('%H:%M:%S %p',time.localtime()))

# import random
#
# # 生成一个大于0 小于1的随机数
# print(random.random())
#
# # 获取指定范围之间的随机整数  第一个值一定要比第二个值小
# a = random.randint(0, 5)  # 不是左闭右开区间
# print(a)
#
# # 获取指定范围之间的随机小数 第一个值可以第二个值大
# b = random.uniform(5.5, 1)
# print(b)
# print('%.1f' % b)
#
# # 打乱顺序
# li = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(li)
# print(li)

# import os
# # os.system('start cmd')  # 打开终端
# # os.system('start osk')  # 打开屏幕
# # os.system('start calc') # 打开计算器
#
# # 获取当前文件所在的路径目录
# print(os.getcwd())

# import sys
#
# # 获取项目和环境位置的
# print(sys.path)
#
# # 获取当前文件的位置
# print(sys.argv)
#
# # 获取python版本
# print(sys.version)
#
# # 获取当前操作系统
# print(sys.platform)
#
# # win32框架
