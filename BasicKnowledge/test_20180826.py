'''
import types


class Person(object):

    def __init__(self, new_name):
        self.name = new_name


def eat(self):
    print('---%s正在吃---' % self.name)


def run(self):
    print('---%s正在跑---' % self.name)


@staticmethod
def test():
    print('---static method-----')


@classmethod
def printNum(cls):
    print('---class method----')


p1 = Person('老王')
# p1.eat = eat()

xxx = types.MethodType(eat, p1)
p1.run = types.MethodType(run, p1)
Person.test = test
Person.printNum = printNum

xxx()
p1.run()
Person.test()
Person.printNum()
'''

'''
class Person(object):
    __slots__ = ('name', 'age')


p = Person()
p.name = '111'
p.age = 21
p.score = '2121'  # 添加额外的会出错
'''

