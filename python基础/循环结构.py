# 作业1.1-100的和(循环)
num = 0
for i in range(100 + 1):
    num += i
print(num)
# 作业2.今天我想吃粽子了,去买粽子,店子关门了,去包子店去买,有粽子在问是甜的还是咸的,如果是甜的就买两个,咸的就买一个,要是没有就买两个豆沙包.(嵌套)
zongzi = input('请问粽子店有没有粽子:')
if zongzi == '没有':
    a = input('去包子店问有没有粽子买:')
    if a == '有':
        b = input('问粽子是甜的还是咸的:')
        if b == '甜的':
            print('我要买两个')
        elif b == '咸的':
            print('我只买一个')
    else:
        print('买两个豆沙包')
else:
    print('输入错误，请重新输入')
# 作业3.九九乘法表(不做要求)(嵌套循环用两个for循环)
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end="\t")
    print()
# 作业4.学生不听话,我要该学生抄20遍作业,抄到10遍的时候,我心软不让他抄了(break)
zuoye = 20  # 要罚抄的遍数
i = 0  # 现在抄的遍数
while i < zuoye:
    i += 1
    print('学生抄到第', i, '遍')
    if i == 10:
        print('我心软了，不让他抄了')
        break
# 作业5.学生不听话,我要该学生抄1遍(作业有20页),学生偷懒第5页,第11页,第16,第18页不抄(continue)
# 方法二 (参考答案)
for i in range(1, 21):
    if i == 5 or i == 11 or i == 16 or i == 18:
        print('我这页没抄')
        continue
    print('抄到第', i, '页')
