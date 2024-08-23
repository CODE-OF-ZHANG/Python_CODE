#作业1.给定一个字符串s，如何获取字符串中第一个字符？
s = "Hello, World!" # 切片
print(s[0])
#作业2.给定一个字符串s，请编写代码获取字符串中最后一个字符。
s = "Hello, World!"
print(s[-1])
#作业3.给定一个字符串s，请编写代码获取字符串中第2个到第5个字符（包含第2个和第5个）。
s = "Hello, World!"
print(s[1:5])
#作业4.给定一个字符串s，请编写代码反转字符串。
s = "Hello, World!"
print(s[::-1])
#作业5.给定一个字符串s，请编写代码将字符串中所有的字母变为大写。
s = "Hello, World!"
str1 = s.upper()
print(str1)
#作业6.给定一个字符串s，请编写代码将字符串中所有的字母变为小写。
s = "Hello, World!"
str2 = s.lower()
print(str2)
#作业7.给定一个字符串s，请编写代码将字符串中的空格替换为下划线。
s = "Hello, Worl d!"
str3 = s.replace(' ','_')
print(str3)
#作业8.给定一个字符串s，请编写代码获取字符串中第一个逗号(,)之前的子串。
s = "Hello, World!"
str4 = s.split(',')[0]
print(str4)
#作业9.给定一个字符串s，请编写代码判断字符串是否以此字符串"World!"结尾。
s = "Hello, World!"
str5 = s.endswith('World!')
print(str5)
#作业10.给定一个字符串s，请编写代码将字符串中的数字相加并输出结果。
s = "12345"
str6 = 0
for i in range(5+1):
    str6 += i
print(str6)
#改:
s = "12345"
str = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])
print(str)
#作业11.给定一个字符串s，请编写代码判断字符串是否以指定的子串"!"结尾。
s = "Hello, World!"
str7 = s.endswith('!')
print(str7)
#作业12.给定一个字符串s，请编写代码判断字符串是否以指定的子串"Hello"开头。
s = "Hello, World!" #这一题用startswith--> endswith()方法
str8 = s.startswith('Hello')
print(str8)
#作业13.给定一个字符串s，请编写代码移除字符串中的所有逗号(,)。
s = "Hello, Wor,ld,!"
str9 = s.replace(',','')
print(str9)
#作业14.给定一个字符串s，请编写代码将字符串中所有的空格替换为逗号(,)。
s = "Hello World, How are you?"
str10 = s.replace(' ',',')
print(str10)
#作业15.给定一个字符串s，请编写代码将字符串中所有的'1'替换为'one'
s = "I have 1 apple and 11 oranges."
str11 = s.replace('1','one')
print(str11)