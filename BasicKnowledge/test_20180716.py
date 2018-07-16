# class MyClass:
#     i = 123
#
#     def f(self):
#         return 'Hello World!'
#
#
# x = MyClass()
#
# print('MyClass类的属性i为：', x.i)
# print('MyClass类的方法f输出为：', x.f())
#
# class Complex:
#     def __init__(self, realpart, imagepart):
#         self.r = realpart
#         self.i = imagepart
#
#
# x = Complex(3.0, -4.5)
# print(x.r, x.i)

# class Test:
#     def prt(num):
#         print(num)
#         print(num.__class__)
#
#
# t = Test()
# t.prt()

# class People:
#
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.weight = w
#
#     def speak(self):
#         print('%s说：我%d岁了，体重是%d公斤。' % (self.name, self.age, self.weight))
#
#
# class Student(People):
#     def __init__(self, n, a, w, g):
#         People.__init__(self, n, a, w)
#         self.grade = g
#
#     def speak(self):
#         print('%s说：我%d岁了，体重是%d公斤，在读%d年级。' % (self.name, self.age, self.weight, self.grade))
#
#
# class Speaker():
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print('我叫%s，我演讲的主题是%s。' % (self.name, self.topic))
#
#
# class Sample(Speaker, Student):
#     def __init__(self, n, a, w, g, t):
#         Student.__init__(self, n, a, w, g)
#         Speaker.__init__(self, n, t)
#
#
# test = Sample('Carol', 10, 30, 3, 'Python')
# test.speak()

# class Parent:
#     def myMethod(self):
#         print('调用父类方法')
#
# class Child(Parent):
#     def myMethod(self):
#         print('调用子类方法')
#
# c = Child()
# c.myMethod()
# super(Child, c).myMethod()

# class JustCounter:
#     __secretCount = 0
#     publicCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)
# class Site:
#     def __init__(self, n, u):
#         self.name = n
#         self.__url = u
#
#     def who(self):
#         print('name:', self.name)
#         print('url:', self.__url)
#
#     def __foo(self):
#         print('这是私有方法')
#
#     def foo(self):
#         print('这是公共方法')
#
#
# test = Site('我的博客', 'dyfloveslife.github.io')
# test.who()
# test.foo()

import time

num = 1


def fun():
    t1 = time.time()
    global num  # 加了global后，在函数内部是可以改变外面的全局变量
    num = 123
    print('在函数中的num：', num)  # 这里输出内部的num=123
    t2 = time.time()
    # print('时间为：{}s'.format(t2 - t1))
    print(t2 - t1)


fun()
print('全局变量num：', num)
