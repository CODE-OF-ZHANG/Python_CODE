# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 线性表-顺序表的设计及基本算法
# @Software: PyCharm
# @Date : 2024/4/2


# 顺序表类
class SqList:
    # 初始化
    def __init__(self):
        self.initcapacity = 5  # 初始容量设置为5
        self.capacity = self.initcapacity  # 容量设置为初始容量
        self.data = [None] * self.capacity  # 设置顺序表的空间
        self.size = 0  # 长度设为0

    # 扩容
    def resize(self, newcapacity):  # 改变顺序表的容量为newcapacity
        assert newcapacity >= 0
        oldata = self.data
        self.data = [None] * newcapacity
        self.capacity = newcapacity
        for i in range(self.size):
            self.data[i] = oldata[i]

    # 整体创建顺序表
    def CreateList(self, a):  # 有数组a中的元素整体建立顺序表
        for i in range(0, len(a)):
            if self.size == self.capacity:  # 出现上溢出时
                self.resize(2 * self.size)  # 扩容
            self.data[self.size] = a[i]
            self.size += 1  # 添加后元素增加1

    def Add(self, e):  # 在线性表的末尾添加一个元素
        if self.size == self.capacity:
            self.resize(2 * self.size)  # 顺序表空间满时倍增容量
        self.data[self.size] = e  # 添加元素e
        self.size += 1  # 长度加1

    def getsize(self):  # 返回长度
        return self.size

    def __getitem__(self, i):  # 求序号为i的元素
        assert 0 <= i < self.size
        return self.data[i]

    def __setitem__(self, i, value):  # 设置序号为i的元素
        assert 0 <= i < self.size
        self.data[i] = value

    def GetNo(self, e):  # 查找第一个为e的元素的下标
        i = 0
        while i < self.size and self.data[i] != e:  # 查找元素e
            i += 1
        if i >= self.size:
            return -1
        else:
            return i

    # 指定位置插入
    def Insert(self, i, e):  # 在线性表中序号为i的位置插入元素
        assert 0 <= i <= self.size
        if self.size == self.capacity:  # 满时扩容
            self.resize(2 * self.size)
        for j in range(self.size, i - 1, -1):  # 疆data[i]及后面的元素后移一位
            self.data[j] = self.data[j - 1]
        self.data[i] = e  # 插入元素e
        self.size += 1  # 长度加1

    def Delete(self, i):  # 在线性表中删除序号为i的元素
        assert 0 <= i <= self.size - 1
        for j in range(i, self.size - 1):
            self.data[j] = self.data[j + 1]  # 将data[j]之后的元素前移一位
        self.size -= 1  # 长度减一
        if self.capacity > self.initcapacity and self.size <= self.capacity / 4:
            self.resize(self.capacity // 2)  # 满足要求容量减半

    def display(self):  # 输出顺序表
        for i in range(0, self.size):
            print(self.data[i], end=' ')
        print()  # 换行


if __name__ == '__main__':
    L = SqList()  # 实例化
    print('建立空顺序表L, 其容量为 %d' % (L.capacity))
    a = [1, 2, 3, 4, 5]
    print('1~6创建L')
    L.CreateList(a)
    print('L[容量 = %d, 长度 = %d]:' % (L.capacity, L.getsize()), end=' '), L.display()
    print('插入6~10')
    for i in range(6, 11):
        L.Add(i)
    print('L[容量 = %d, 长度 = %d]:' % (L.capacity, L.getsize()), end=' '), L.display()
    print('序号为2的元素 = %d' % (L[2]))
    print('设置序号为2的元素为20')
    L[2] = 20
    print('L[容量 = %d, 长度 = %d]:' % (L.capacity, L.getsize()), end=' '), L.display()
    x = 6
    print('第一个值为%d的元素序号 = %d' % (x, L.GetNo(x)))
    n = L.getsize()
    for i in range(n - 2):
        print('删除首元素')
        L.Delete(0)
        print('L[容量 = %d, 长度 = %d]:' % (L.capacity, L.getsize()), end=' '), L.display()
