li = [1, 2, 3, 4, 5, 6, 1]
#  (1)求列表的长度
print(len(li))
#  (2)判断7 是否在列表中    # in not in  count(0)
print(7 in li)
print(7 not in li)
#  (3)在列表的末尾新增一个元素10
li.append(10)
print(li)
#  (4)删除第一个元素
li = [1, 2, 3, 4, 5, 6, 1]
li.pop(0)
print(li)
#  (5)在列表中在添加一个列表li1[10,14,17]
li = [1, 2, 3, 4, 5, 6, 1]
li.append([10, 14, 17])
print(li)
#  (6)在列表中在添加一个元组t(0,5,30)
li = [1, 2, 3, 4, 5, 6, 1]
li.append((0, 5, 30))
print(li)
#  (7)统计元素1在列表的次数
li = [1, 2, 3, 4, 5, 6, 1]
print(li.count(1))
#  (8)把元素5改成15
li[4] = 15
print(li)
#  (9)删除整个列表li  #全部删除
del li
