# 1.定义一个函数，可以用来求任意三个数的乘积
def cj(a, b, c):
    print(a * b * c)


cj(3, 4, 5)


# 2.定义一个函数，可以根据不同的用户名显示欢迎信息
def welcome(Username):
    print(f'欢迎{Username}光临')


welcome('张三')


# 3.编写一个函数，功能是输出2个数中较大的一个数
# 方法一
def bjdx(a, b):
    print(a if a > b else b)


bjdx(5, 6)


# 方法二
def bjdx(a, b):
    if a > b:
        print(a)
    else:
        print(b)


bjdx(9, 10)
# 一个整数，它加上 100 后是一个完全平方数，再加上 168 又是一个完全平方数，请问该数是多少
import math

for x in range(1, 1000):
    m = math.isqrt(x + 100)
    n = math.isqrt(x + 100 + 168)
    if m * m == (x + 100) and n * n == (x + 100 + 168):
        print("满足条件的整数为:", x)
        break
