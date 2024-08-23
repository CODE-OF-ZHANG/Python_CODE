#作业1.计算bim指数(多分支结构)
# h = float(input('请输入你的身高(单位/m):'))
# w = float(input('请输入你的体重(单位/kg):'))
# bmi = w/h**2
# print(bmi)
# if bmi > 0 and bmi <= 18.4:
#     print('偏廋')
# elif bmi >= 18.5 and bmi <=23.9:
#     print('正常')
# elif bmi >=24.0 and bmi <=27.9:
#     print('偏胖')
# else:
#     print('胖')

#作业2.分支机构(双分支结构)
boy = int(input('请输入你的年龄:'))   #男孩法定结婚年龄是不早于22周岁
girl = int(input('请输入你的年龄:'))  #女孩法定结婚年龄是不早于20周岁
print(boy,girl)
if boy > 22 and girl > 20:
    print('该男孩和女孩符合法定结婚年龄')
else:
    print('该男孩和女孩不符合法定结婚年龄')
