# 包含一个学生类
# 一个 sayHello 函数

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('my name is {0}'.format(self.name))

def sayHello():
    print('Hello bitches')

print('I\'m py1, what\'s up ')
