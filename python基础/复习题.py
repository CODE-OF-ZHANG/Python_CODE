'''
1、3*1**3 ， 该表达式输出的结果为（ C ）

​	A、27	B、9	C、3	D、1

2、以下代码输出的结果是（C ）
if None:
    print('hello')
A、False	B、Hello	C、没有任何输出	D、语法错误

3、以下代码输出的结果是（B ） 错，改：A
for i in [1 , 0]:
    print(i + 1)

A、2
   1
B、[2 , 1]
C、2
D、0

4、以下哪个描述是正确的（ D）

A、break语句用于终止循环

B、continue语句用于跳过当前剩余要执行的代码 ， 执行下一次循环

C、break和continue语句通常与if ， if...else , if...elif...else语句一起使用

D、以上说法都是正确的。

5、以下代码输出的结果是（ A）
for char in 'PYTHON STRING':
  if char == ' ':
      break

  print(char, end='')

  if char == 'O':
      continue
A、PYTHON	B、PYTHONSTRING	C、PYTHN 	D、STRING

6、下列语句不正确的是（ C ） 错，改：B

​	A、x = y = z = 1

​	B、x = (y = z + 1)

​	C、x , y = y , x

​	D、x += y



## 二、填空题
1、以下代码输出的结果为—— (3)
x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

2、以下代码输出的结果为—— (10)
i = sum = 0

while i <= 4:
    sum += i
    i = i + 1
print(sum)

3、当函数中参数个数不确定是怎样定义形参—— (*args, **kwargs)

4、bool类型当作数值时，分别为哪两个数值—— (0, 1)

5、0 and 11 ， 输出的结果为—— (0)

6、0 or 11 ， 输出的结果为—— (1)

7、函数的参数传递形式分别为：—— (必须参数(位置参数) , 默认参数 , 关键字参数 , 可变长参数)

8、如何定义一个空集合A，—— (my_set = set())

三、判断题
1、以下代码自会执行一次。（ 错） 会无限循环下去
while 4 == 4:
    print('hello')

2、字典中值（value）不可以重复。（ 错） 值可以重复，键不可以

3、字典中的键（key）可以是列表。（ 错 ）

4、Python中main函数表示的是程序执行入口。（ 错 ）

5、a = {2 , 5 , 3  , [2 , 4 , 6 , 8] , 10}这个集合是正确的。（ 错） 集合中的元素不能有列表

6、以下代码输出的x为196。（错 ） x = 56
def func():
    global x
    x = 56

x = 196
func()
print(x)

## 四、问答题

1、写出Python中的数据类型（在每个数据类型后面用括号备注上可变或不可变）：

​	数值类型：整型(int,不可变) , 浮点型(float,不可变) , 布尔类型(bool,不可变)

​	序列类型：字符串(str,不可变) , 列表(list,可变) , 元组(tuple,不可变)

​	散列类型：字典(dict,可变) , 集合(set,可变)

2、序列类型跟散列类型的区别。散列类型(字典和集合)
序列类型：相邻有序，定位灵活
散列类型：分散无序，定位迅速
3、装饰器的作用
保持数据的同时，添加新的数据或功能
4、命名空间有几个
内置命名空间 , 全局命名空间 , 局部命名空间
5、什么是作用域
变量的使用范围 , 有全局跟局部
6、讲过几个常用模块
random， time， os， sys，re
7、什么是模块 ， 什么是包
模块是一个python文件；包是一个完成特定任务的工具箱
'''

# 1.在终端中录入一个疫情确诊人数,再录入一个治愈人数,打印治愈比例。格式：治愈比例为xx%
res = int(input('请输入疫情确诊人数:'))
res1 = int(input('请输入治愈人数:'))
a = int(res1 / res * 100)
print(f'治愈比例为%.2f' % a)

# 2.在终端中获取商品单价、购买的数量和支付金额。如果钱不够提示"金额不足"，否则提示"应找回：xx元"。
a = int(input('请输入商品价格:'))
b = int(input('请输入购买数量:'))
c = int(input('应支付金额:'))
if c < a * b:
    print('金额不足')
else:
    print(f'应招回:{c - (a * b)}元')
# 3.电梯设置规定：如果承载人不超过10人，且总重量不超过1000千克，可以正常使用，否则提示超载。
a = int(input('乘坐电梯人数:'))
b = int(input('总重量:'))
if a <= 10 and b <= 1000:
    print('可以正常使用')
else:
    print('已超载')
# 4.在终端中输入账户类型,消费金额,计算折扣.
# 如果是vip客户,消费小于等于500,享受85折。消费大于500，享受8折
# 如果不是vip客户,消费大于等于800,享受9折。消费小于800，原价
a = input('客户类型:')
b = int(input('消费金额:'))
if a == 'vip':
    if 0 < b <= 500:
        print('可以享受85折优惠')
    else:
        print('可以享受8折优惠')
else:
    if b >= 800:
        print('可以享受9折优惠')
    else:
        print('原价，不优惠')

# 5.用户登录如果账号的密码错误3次，提示锁定账户
# 不会（看了答案，还是不懂）
registered_accounts = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}
username = input("请输入账号：")
password = input("请输入密码：")

# 初始密码错误次数为0
wrong_password_count = 0
# 判断账号密码是否匹配
while True:
    if username in registered_accounts and password == registered_accounts[username]:
        print("登录成功")
        break
    else:
        wrong_password_count += 1
        if wrong_password_count >= 3:
            print("密码错误次数达到上限，账户已锁定")
            break
        else:
            print("密码错误，请重新输入")
            password = input("请输入密码：")
# 6.一张纸的厚度是0.01毫米，请计算，对折多少次超过珠穆朗玛峰(8844.43米)。
a = 0.00001  # 单位统一: 0.01mm = 0.00001m
b = 0  # 折叠的次数(初始次数为0)
while a * 2 ** b < 8848.43:
    b += 1
print(f'要折叠{b}次')
# 7.一家公司有如下岗位：
#     经理 ："曹操","刘备","孙权"
#     技术 ："曹操","刘备","张飞","关羽"
#
# 1. 使用集合存储以上信息.
# 2. 是经理也是技术的都有谁?
# 3. 是经理也不是技术的都有谁?
# 4. 不是经理是技术的都有谁?
# 5. 身兼一职的都有谁?
# 6. 公司总共有多少人数?
# 1.
a = {"曹操", "刘备", "孙权"}
b = {"曹操", "刘备", "张飞", "关羽"}
# 2.
print(f'是经理也是技术的有{a & b}')
# 3.
print(f'是经理也不是技术的是{a - b}')
# 4.
print(f'不是经理是技术的是{b - a}')
# 5.
a1 = a - b
b1 = b - a
print(f'身兼一职的是{a1 | b1}')
# 6.
print(f'公司总共有{len(a | b)}人')
# 8.用户输入一个数字,判断(1~12)属于哪个季节
a = int(input('请输入1至12范围内的任意整数:'))
if 1 <= a <= 3:
    print('该季节为春季')
elif 4 <= a <= 6:
    print('该季节为夏季')
elif 7 <= a <= 9:
    print('该季节为秋季')
elif 10 <= a <= 12:
    print('该季节为冬季')
else:
    pass

# 9.
dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}
# 1. 打印所有城市（一行一个）
# 2. 打印北京所有美食（一行一个）
# 3. 打印四川所有景区（一行一个）
# 4. 打印所有城市的所有景区（一行一个）
# 5. 为北京添加景区："天坛"
# 第1问.
for i in dict_travel_info.keys():
    print(i)
# 第2问.
for i in dict_travel_info["北京"]["美食"]:
    print(i)
# 第3问.
for i in dict_travel_info["四川"]["景区"]:
    print(i)
# 第4问.
for i in dict_travel_info["北京"]["景区"] and dict_travel_info["四川"]["景区"]:
    print(i)
# 第5问.
dict_travel_info["北京"]["景区"].append("天坛")
print(dict_travel_info)
# 10. 用循环画出一个4*4的空心矩形
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print('* ', end='')
        else:
            print(' ', end=' ')
    print()
# 11.定义一个函数 , 传入一个有重复元素列表 , 让函数返回的是一个无重复元素的列表
a = [1, 2, 3, 4, 5, 6, 2, 5, 6, 1, 7]


def fun():
    return list(set(a))


print(fun())
# 12.求1～100间所有奇数的和
sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)


# 13 . 用函数写一个计算器（有加减乘除的功能供用户选择计算）
def jia(num1, num2):
    return num1 + num2


def jian(num1, num2):
    return num1 - num2


def cheng(num1, num2):
    return num1 * num2


def chu(num1, num2):
    return num1 / num2


print('这是一个简单的计算器')
a = float(input('请输入第一个数:'))
b = float(input('请输入第二个数:'))
select = int(input('操作方式（输入1表示加法,输入2表示减法,输入3表示乘法,输入4表示除法）:'))
if select == 1:
    print(jia(a, b))
elif select == 2:
    print(jian(a, b))
elif select == 3:
    print(cheng(a, b))
elif select == 4:
    print(chu(a, b))


# 14 . 一个函数只有一个形参 ， 当要接收多个数字 ， 返回的是一个元组类型 ， 这个函数内部讲接收到的数字进行运算
#     返回一个元组 ， 并且元组的第一个数字是这些数字的平均值 ， 后面的数字是大于这个平均值的数。
def fun_1(*args):
    sum1 = 0
    for i in args:
        sum1 += i
    avg = sum1 / len(args)
    li = []
    for i in args:
        if i > avg:
            li.append(i)
    li.insert(0, avg)
    return tuple(li)


print(fun_1(1, 2, 3, 4, 5, 6, 7, 15, 20))
