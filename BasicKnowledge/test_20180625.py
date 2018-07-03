# class MyClass:
#     '''A simple exa,ple class'''
#     i = 12345
#
#     def f(self):
#         return 'HelloWorld'
#
#
# print(MyClass.i)
# print(MyClass.f('x'))
# print(MyClass.__doc__)
'''类的实例化操作的参数传递给__init__().'''

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart  # 真实的
#         self.i = imagpart  # 想象的
# x = Complex(3.0, 2)
# print(x.r, x.i)
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# Carol = Student()  #创建Studnet的实例Carol
# Carol.name = 'Sir Carol'  # 给实例变量绑定name属性
# print(Carol.name)

# Carol = Student('Sir Carol', 90)
# print(Carol.name, "'s score is ", Carol.score)

# class Dog:
#     kind = 'canine'
#
#     def __init__(self, name):
#         self.name = name
#
#
# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.kind)
# print(e.kind)
# print(d.name)
# print(e.name)

'''9.3.5'''

# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
#
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)
# print(e.tricks)

# for element in [1, 2, 3]:
#     print(element)
#
# for element in (1, 2, 3):
#     print(element)

# for key in {'one': 1, 'two': 2}:
#     print(key)

# for char in "123":
#     print(char)

'''字符串和编码'''