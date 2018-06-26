'''
list是一种有序的集合，可以随时添加和删除其中的元素。
特点：
1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。
classmates = ['Michael', 'Bob', 'Tracy']

tuple是有序列表的元组，一旦初始化就不能修改。
classmates = ('Michael', 'Bob', 'Tracy')

字典：dict，使用键-值（key-value）存储，具有极快的查找速度，是用空间来换取时间的一种方法。
特点：
1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
 name_scores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

set是一组存储不重复key的集合，但不存储value,不可以放入可变对象。
set可以看成数学意义上的无序和无重复元素的集合。
要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
'''

# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print(t)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# age = int(input('Please enter your age:'))
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# else:
#     print('your age is ', age)
#     print('teenager')
'''
height = 1.75
weight = 80.5
bmi = weight / (height ** 2)
'''

# height = float(input('Please enter your height:'))
# weight = float(input('Please enter your weight:'))
# bmi = float(weight / (height ** 2))
# print(bmi)
# if bmi > 32:
#     print('严重肥胖')
# elif bmi >= 28:
#     print('肥胖')
# elif bmi >= 25:
#     print('过重')
# elif bmi >= 18.5:
#     print('正常')
# else:
#     print('过轻')

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in list(L):
#     print('Hello,%s!' % name)

# name_scores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(name_scores)
# name_scores.pop('Bob')
# print(name_scores)

# a = int('123')
# print(a)
# b = bool(1)
# print(b)
#
# a = abs
# print(a(-1))

# from abstest import my_abs
# print(my_abs(-1))
#
# import math
#
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# r = move(100, 100, 60, math.pi / 6)
# # Python的函数返回多值其实就是返回一个tuple
# print(r)

# import math
#
#
# def quadratic(a, b, c):
#     if not isinstance(a, (int, float)):
#         raise TypeError('bad operand type')
#     if not isinstance(b, (int, float)):
#         raise TypeError('bad operand type')
#     if not isinstance(c, (int, float)):
#         raise TypeError('bad operand type')
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         return '方程无解'
#     elif delta == 0:
#         x = -b / (2 * a)
#         return x
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
#
# print('请输入一元二次方程的三个参数:')
# a = float(input('a:'))
# b = float(input('b:'))
# c = float(input('c:'))
# print(quadratic(a, b, c))

# def power(x):
#     return x ** 2
#
#
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n -= 1
#         s *= x
#     return s
#
#
# print(power(5))

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
#
# enroll('Carol', 'F')
# enroll('Tom', 'F', 14)
# enroll('Jack', 'M', city='tianjin')

'''要设计str、None这样的不变对象'''


# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
#
# print(add_end())

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n ** 2
#     return sum
#
#
# nums = [1, 2, 3]
# print(calc([1, 2, 3]))
# print(calc((1, 3, 5, 7)))
# print(calc(1, 2, 3))
# print(calc(1, 3, 5, 7))
# print(calc())
# print(calc(1, 2))
# print(calc(nums[0], nums[1], nums[2]))
# *nums表示把nums这个list的所有元素作为可变参数传进去.
# print(calc(*nums))
'''函数->函数的参数->关键字参数'''
