# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 线性表-双链表的设计及基本算法
# @Software: PyCharm
# @Date : 2024/5/9


# 双链表结点类
class DLinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prior = None


# 双链表类
class DLinkList:
    def __init__(self):
        self.dhead = DLinkNode()
        self.dhead.next = None
        self.dhead.prior = None

    # 头插法
    def CreateListF(self, a):
        for i in range(0, len(a)):
            s = DLinkNode(a[i])
            s.next = self.dhead.next
            if self.dhead.next != None:
                self.dhead.next.prior = s
                self.dhead.next = s
                s.prior = self.dhead

    # 尾插法
    def CreateListR(self, a):
        t = self.dhead
        for i in range(0, len(a)):
            s = DLinkNode(a[i])
            t.next = s
            s.prior = t
            t = s
        t.next = None

    # 返回序号为i的值
    def geti(self, i):
        p = self.dhead
        j = -1
        while j < i and p is not None:
            j += 1
            p = p.next
        return p

    # 末尾添加元素e
    def Add(self, e):
        s = DLinkNode(e)
        p = self.dhead
        while p.next is not None:
            p = p.next
        p.next = s
        s.prior = p






