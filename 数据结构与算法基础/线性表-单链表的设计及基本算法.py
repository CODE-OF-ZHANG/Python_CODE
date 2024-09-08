# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 线性表-单链表的设计及基本算法
# @Software: PyCharm
# @Date : 2024/5/8


# 单链表结点类
class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# 单链表类
class LinkList:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = None

    # 头插法: 由数组a整体建立单链表
    def CreateListF(self, a):
        for i in range(0, len(a)):
            s = LinkNode(a[i])
            s.next = self.head.next
            self.head.next = s

    # 尾插法: 由数组a整体建立单链表
    def CreateListR(self, a):
        t = self.head
        for i in range(0, len(a)):
            s = LinkNode(a[i])
            t.next = s
            t = s
        t.next = None

    # 返回序号为i的结点
    def geti(self, i):
        p = self.head
        j = -1
        while j < i and p is not None:
            j += 1
            p = p.next
        return p

    # 在线性表的末尾添加一个元素e
    def Add(self, e):
        s = LinkNode(e)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = s

    # 返回长度
    def getsize(self):
        p = self.head
        cnt = 0
        while p.next is not None:
            cnt += 1
            p = p.next
        return cnt

    # 求序号i的元素
    def __getitem__(self, i):
        assert i >= 0
        p = self.geti(i)
        assert p is not None
        return p.data

    # 设置序号为i的元素
    def __setitem__(self, i, x):
        assert i >= 0
        p = self.geti(i)
        assert p is not None
        p.data = x

    # 查找第一个为e的元素的序号
    def GetNo(self, e):
        j = 0
        p = self.head.next
        while p is not None and p.data != e:
            j += 1
            p = p.next
        if p is None:
            return -1
        else:
            return j

    # 在线性表中序号为i的位置插入元素e
    def Insert(self, i, e):
        assert i >= 0
        s = LinkNode(e)
        p = self.geti(i - 1)
        assert p is not None
        s.next = p.next
        p.next = s

    # 在线性表中删除序号i的位置的元素
    def Delete(self, i):
        assert i >= 0
        p = self.geti(i - 1)
        assert p.next is not None
        p.next = p.next.next

    # 输出线性表
    def display(self):
        p = self.head.next
        while p is not None:
            print(p.data, end=' ')
            p = p.next
        print()


if __name__ == '__main__':
    L = LinkList()
    print('建立空单链表L')
    a = [1, 2, 3, 4, 5, 6]
    print('1~6创建L')
    L.CreateListR(a)
    print('L[长度 = %d]: ' % (L.getsize()), end=' '), L.display()
    print('插入6~10')
    for i in range(6, 11):
        L.Add(i)
    print('L[长度 = %d]: ' % (L.getsize()), end=' '), L.display()
    print('序号为2的元素 = %d' % (L[2]))
    print('设置序号为2的元素为20')
    L[2] = 20
    print('L[长度 = %d]: ' % (L.getsize()), end=' '), L.display()
    x = 6
    print('第一个值为%d的元素序号 = %d' % (x, L.GetNo(x)))
    n = L.getsize()
    for i in range(n - 2):
        print('删除首元素')
        L.Delete(0)
        print('L[长度 = %d]: ' % (L.getsize()), end=' '), L.display()
