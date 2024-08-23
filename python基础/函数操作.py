# 1.编写一个函数，功能是返回2个数的和
# 方法一
def add(a, b):
    print(a + b)


add(4, 8)


# 方法二
def add1(num1, num2):
    add1 = num1 + num2
    return add1


ls1 = [add1(5, 10)]
print(ls1)
# 2.写函数，判断用户传入的对象（字符串、列表、元祖）长度是否大于5
list = [1, 2, 3, 4, 5, 6]


def fun(a):
    if len(a) > 5:
        print(True)
    else:
        print(False)


fun(list)


# 3.写函数，检查传入列表的长度[1,2,3,4,5]，如果大于2，那么仅保留前两个长度的内容，并返回新内容
def fun1(a):
    if len(a) > 2:
        return a[0:2]


print(fun1([1, 2, 3, 4, 5]))

li = [1, 2, 3, 4, 5]  # 迭代器
li1 = iter(li)
print(li1)  # <list_iterator object at 0x00000263D9C90FD0> 地址
