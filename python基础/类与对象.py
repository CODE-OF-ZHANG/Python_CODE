#定义一个狗类
class Dog:
    name = '小黑'
    age = 2
    set = '母'
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def eat(self):
        print(f'我给{self.name}喂了狗粮,导致它都胖一公斤了,它现在搜{self.weight + 1}公斤了')

    def sleep(self):
        print(f'{self.name}明年就{self.age + 1}岁了')

xaiohie = Dog('小黑', 2, 25)
print(xaiohie.name)
print(xaiohie.set)
xaiohie.eat()
xaiohie.sleep()

'''
self:代表类的实例，并非类；只有在类的方法中才会有
'''