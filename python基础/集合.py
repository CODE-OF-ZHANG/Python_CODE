# 1.创建一个空集合my_set。
my_set = set()
print(my_set)
# 2.向集合my_set中添加元素'apple'、'banana'和'orange'。
my_set.add('apple')
my_set.add('banana')
my_set.add('orange')
print(my_set)
# 3.从集合my_set中删除元素'banana'。
my_set.remove('banana')
print(my_set)
# 4.创建另一个集合my_set，包含元素'kiwi','orange'和'grape'。
my_set2 = {'kiwi', 'orange', 'grape'}
print(my_set2)
# 5.获取两个集合my_set和my_set2的并集。
print(my_set | my_set2)
# 6.获取两个集合my_set和my_set2的交集。
print(my_set & my_set2)
# 7.获取两个集合my_set和my_set2的差集。
print(my_set - my_set2)

