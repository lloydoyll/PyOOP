'''
定义一个学生类
'''
class Student():
    name = 'xixi'
    age = 18

    # 1. 注意缩进
    # 2. 默认有一个self参数
    def SayMyName(self):
        print('I\'m bitch')

xixi = Student()
print(xixi.name)
xixi.SayMyName()

