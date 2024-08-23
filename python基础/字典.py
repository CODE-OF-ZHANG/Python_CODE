# 1. 创建一个空字典my_dict。
my_dict = {}
print(my_dict)
# 2. 向字典my_dict中添加键值对'apple': 3、'banana': 6和'orange': 4。
my_dict.update({'apple': 3, 'banana': 6, 'orange': 4})
print(my_dict)
# 3. 获取字典my_dict中键为'banana'的值，并将其存储在变量value中。
print(my_dict['banana'])
value = my_dict['banana']
print(value)
# 4. 将字典my_dict中键为'orange'的值增加2。
my_dict['orange'] += 2
print(my_dict)
# 5. 删除字典my_dict中键为'apple'的键值对。
my_dict.pop('apple')
print(my_dict)
# 6. 检查字典my_dict中是否存在键'grape'。
print('grape' in my_dict)
print('grape' not in my_dict)
# 7. 获取字典my_dict中所有键，并将其存储在列表keys中。
keys = list(my_dict.keys())
print(keys)
# 8. 获取字典my_dict中所有值，并将其存储在列表values中。
values = list(my_dict.values())
print(values)

